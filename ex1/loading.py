try:
    import importlib.metadata as il
except ImportError:
    il = None
try:
    import numpy as np
except ImportError:
    np = None
try:
    import pandas as ps
except ImportError:
    ps = None
try:
    import matplotlib.pyplot as mpl
except ImportError:
    mpl = None

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    for pack, message in packages.items():
        try:
            ver: str = il.version(pack)
            print(f"[OK] {pack} ({ver}) - {message}")
        except il.PackageNotFoundError as e:
            print(f"\n{e}")
    if np and il and ps and mpl:
        width: int = 8
        height: int = 4
        print("Analyzing Matrix data...")
        try:
            data_matrix = np.random.randint(
                low=0, high=100, size=(height, width)
            )
            print(f"Processing {height * width} data points...")
            data_frame = ps.DataFrame(data_matrix)
            print("Generating visualization...")
            print("\nAnalysis complete!")
            data_frame.plot()
            print("Results saved to: matrix_analysis.png")
            mpl.savefig("matrix_analysis.png", dpi=300)
        except Exception as e:
            print(e)
    else:
        print(
            "\nAnalysis skipped because one or more dependencies are missing."
        )
        print(
            "To install packages use 'pip install -r requirements' or 'poetry install'"
        )
