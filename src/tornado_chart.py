import matplotlib.pyplot as plt

def plot_tornado(parameters, low_values, high_values):
    """
    Create a tornado chart for sensitivity analysis.

    parameters: list of parameter names
    low_values: list of low case results
    high_values: list of high case results
    """

    diffs = [high - low for low, high in zip(low_values, high_values)]

    # Sort for better visualization
    sorted_data = sorted(zip(diffs, parameters, low_values, high_values))
    diffs, parameters, low_values, high_values = zip(*sorted_data)

    y_pos = range(len(parameters))

    plt.figure(figsize=(8, 5))
    plt.barh(y_pos, diffs)
    plt.yticks(y_pos, parameters)
    plt.xlabel("Impact on Output")
    plt.title("Tornado Chart - Sensitivity Analysis")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    parameters = ["Porosity", "Sw", "NTG", "GR"]
    low_values = [100, 80, 90, 95]
    high_values = [150, 120, 110, 105]

    plot_tornado(parameters, low_values, high_values)
