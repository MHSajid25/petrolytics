import matplotlib.pyplot as plt


def plot_gr_vsh(results):
    depths = [row["depth"] for row in results]
    gr_values = [row["gr"] for row in results]
    vsh_values = [row["vsh"] for row in results]

    plt.figure(figsize=(10, 6))

    plt.plot(gr_values, depths, label="GR")
    plt.plot(vsh_values, depths, label="Vsh")

    plt.gca().invert_yaxis()
    plt.xlabel("Value")
    plt.ylabel("Depth")
    plt.title("Gamma Ray and Vsh vs Depth")
    plt.legend()
    plt.grid(True)
    plt.show()
