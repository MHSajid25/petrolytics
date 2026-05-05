import pandas as pd
import numpy as np
from scipy.spatial import cKDTree

# STEP 2: Get wells
uwis = get_wells_uwi()

# Example:
horizontal_well = "42251330440000"
vertical_wells = [
    "A1",
    "A2"
] # subset for testing

# STEP 3: Load surveys
def load_well(uwi):
    survey = survey(uwi)
    header = header(uwi)

    surface_x = header["easting"].iloc[0]
    surface_y = header["northing"].iloc[0]

    # Convert offsets → absolute X/Y
    survey["X"] = survey["x_offset"] + surface_x
    survey["Y"] = survey["y_offset"] + surface_y
    survey["TVD"] = survey["tvd"]
    survey["MD"] = survey["md"]

    return survey[["MD", "X", "Y", "TVD"]]


def interpolate_well(df, step=10):
    md_new = np.arange(df["MD"].min(), df["MD"].max(), step)

    return pd.DataFrame({
        "MD": md_new,
        "X": np.interp(md_new, df["MD"], df["X"]),
        "Y": np.interp(md_new, df["MD"], df["Y"]),
        "TVD": np.interp(md_new, df["MD"], df["TVD"]),
    })


def find_min_distance(w1, w2):
    pts1 = w1[["X", "Y", "TVD"]].to_numpy()
    pts2 = w2[["X", "Y", "TVD"]].to_numpy()

    tree = cKDTree(pts2)
    dist, idx = tree.query(pts1, k=1)

    i1 = np.argmin(dist)
    i2 = idx[i1]

    return dist[i1], w1.iloc[i1], w2.iloc[i2]

# STEP 4: Process horizontal well
well1 = interpolate_well(load_well(horizontal_well), step=10)

results = []

# STEP 5: Loop through vertical wells
for uwi in vertical_wells:
    try:
        well2 = interpolate_well(load_well(uwi), step=10)
        d, p1, p2 = find_min_distance(well1, well2)

        results.append({
            "target_well": horizontal_well,
            "offset_well": uwi,
            "distance_ft": d,
            "md_target": p1["MD"],
            "md_offset": p2["MD"]
        })

    except Exception as e:
        print(f"Skipping {uwi}: {e}")

df_results = pd.DataFrame(results).sort_values("distance_ft")

print(df_results.head(10))