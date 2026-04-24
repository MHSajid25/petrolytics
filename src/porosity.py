def calculate_density_porosity(rhob, matrix_density=2.65, fluid_density=1.0):
    """
    Calculate density porosity using bulk density log.

    rhob: bulk density from log
    matrix_density: matrix density, default sandstone = 2.65 g/cc
    fluid_density: fluid density, default water = 1.0 g/cc
    """
    if matrix_density == fluid_density:
        return 0

    porosity = (matrix_density - rhob) / (matrix_density - fluid_density)
    return max(0, min(porosity, 1))


if __name__ == "__main__":
    rhob = 2.35
    porosity = calculate_density_porosity(rhob)

    print(f"Density Porosity: {porosity:.2f}")