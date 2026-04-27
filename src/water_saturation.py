def calculate_archie_sw(rw, rt, porosity, a=1, m=2, n=2):
    """
    Calculate water saturation using Archie's equation.
    """
    if rt == 0 or porosity == 0:
        return 0

    sw = ((a * rw) / (rt * (porosity ** m))) ** (1 / n)
    return max(0, min(sw, 1))


if __name__ == "__main__":
    sw = calculate_archie_sw(rw=0.08, rt=20, porosity=0.18)
    print(f"Water Saturation: {sw:.2f}")
