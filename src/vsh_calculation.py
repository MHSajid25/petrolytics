from log_reader import read_log_data
from net_pay import calculate_net_pay
from plot_logs import plot_gr_vsh

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

    vsh_values = [row["vsh"] for row in results]
    net_pay = calculate_net_pay(vsh_values)

    print("First 5 results:")
    for row in results[:5]:
        print(row)

    print(f"Net Pay Zones: {net_pay}")

    plot_gr_vsh(results)