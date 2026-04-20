# petrolytics

A structured toolkit for petrophysical analysis, focused on well log interpretation, reservoir evaluation, and subsurface data processing.

## Overview

This repository is designed to build analytical tools used in petrophysics for evaluating reservoir properties from well log data. It combines data processing, mathematical modeling, and domain-specific workflows to simulate real-world subsurface analysis.

## Repository Structure
src/
vsh_calculation.py
data/


## Modules

### Volume of Shale (Vsh) Calculation
- Computes Vsh using Gamma Ray (GR) logs
- Supports linear and normalized methods
- Handles basic log preprocessing
- Designed for integration into petrophysical workflows

### Tornado Chart (Sensitivity Analysis)
- Visualizes impact of key parameters on output
- Supports reservoir and petrophysical uncertainty analysis
- Helps identify dominant variables in evaluation workflows

## Use Cases

- Well log interpretation and analysis
- Reservoir characterization workflows
- Estimating shale volume from GR logs
- Preprocessing subsurface data for modeling

## Techniques Used

- Numerical calculations and normalization
- Data transformation and cleaning
- Domain-specific formulas (GR-based Vsh)
- Python-based data processing

## Domain Context — Petrophysics

Petrophysics involves analyzing well log and subsurface data to estimate key reservoir properties such as shale volume, porosity, and fluid saturation. These properties are critical for understanding reservoir quality and production potential.

## Extensibility

This toolkit is designed to evolve into a broader petrophysical analysis system, with additional modules such as:

- Porosity estimation
- Water saturation (Sw) calculations
- Net pay determination
- Multi-log data integration

## Roadmap

- Support for multiple Vsh calculation methods
- Integration with CSV/log file inputs
- Visualization of log curves
- Expansion to full petrophysical workflows

## Purpose

To develop practical tools that bridge software engineering and petrophysical analysis, enabling scalable and reproducible subsurface data workflows.
