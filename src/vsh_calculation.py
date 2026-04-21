from log_reader import read_log_data

def calculate_vsh(gr, gr_min, gr_max):
    """
    Calculate Volume of Shale (Vsh) using linear method.
    """
    if gr_max == gr_min:
        return 0

    vsh = (gr - gr_min) / (gr_max - gr_min)
    return max(0, min(vsh, 1))


def process_log(file_path, gr_min, gr_max):
    data = read_log_data(file_path)

    results = []

    for row in data:
        vsh = calculate_vsh(row["gr"], gr_min, gr_max)
        results.append({
            "depth": row["depth"],
            "gr": row["gr"],
            "vsh": vsh
        })

    return results


if __name__ == "__main__":
    file_path = "data/sample_logs.csv"
    results = process_log(file_path, 20, 120)

    for r in results[:5]:
        print(r)
