def calculate_vsh(gr, gr_min, gr_max):
    """
    Calculate Volume of Shale (Vsh) using linear method.

    Parameters:
    gr (float): Gamma Ray value
    gr_min (float): Clean sand GR value
    gr_max (float): Shale GR value

    Returns:
    float: Vsh value
    """
    if gr_max == gr_min:
        return 0

    vsh = (gr - gr_min) / (gr_max - gr_min)
    return max(0, min(vsh, 1))


if __name__ == "__main__":
    # Example values
    gr = 85
    gr_min = 20
    gr_max = 120

    vsh = calculate_vsh(gr, gr_min, gr_max)
    print(f"Calculated Vsh: {vsh:.2f}")
