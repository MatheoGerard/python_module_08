import importlib.metadata as il
import numpy as np
import pandas as ps
import matplotlib.pyplot as mpl

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    for pack, message in packages.items():
        try:
            ver: str = il.version(pack)
            print(f"[OK] {pack} ({ver}) - {message}")
        except il.PackageNotFoundError as e:
            print(e)
    width: int = 8
    height: int = 4
    print("Analyzing Matrix data...")
    data_matrix = np.random.randint(low=0, high=100, size=(height, width))
    print(f"Processing {height * width} data points...")
    data_frame = ps.DataFrame(data_matrix)
    print("Generating visualization...")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
    data_frame.plot()
    mpl.savefig("matrix_analysis.png", dpi=300)
