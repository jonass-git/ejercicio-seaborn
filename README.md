# Penguin Data Visualization

This project uses Python, seaborn, and matplotlib to create a multi-plot visualization of the Palmer Penguins dataset.

## Description

The script `ejercicio.py` loads the 'penguins' dataset, preprocesses it by dropping rows with missing values, and then uses `seaborn.FacetGrid` to create a grid of scatter plots.

The visualization displays the relationship between:
- **X-axis:** Flipper Length (mm)
- **Y-axis:** Body Mass (g)

The data is faceted by:
- **Columns:** Species
- **Rows:** Sex
- **Hue:** Island

The resulting plot provides a comprehensive view of how these variables interact across different penguin species, sexes, and their native islands.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install seaborn matplotlib
    ```
2.  **Execute the script:**
    ```bash
    python ejercicio.py
    ```

This will display a window with the generated plot.
