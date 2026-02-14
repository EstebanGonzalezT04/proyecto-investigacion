# Este archivo se encarga de los Graficos generados a partir de los datos.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    project_root = Path(__file__).resolve().parents[1]

    clean_path = project_root / "data" / "processed" / "clean_data.csv"
    results_dir = project_root / "results" / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(clean_path)

    # Grafico simple y claro: dispersion interarrival vs service
    plt.figure()
    plt.scatter(df["interarrival_min"], df["service_min"], alpha=0.5)
    plt.xlabel("Interarrival time (min)")
    plt.ylabel("Service time (min)")
    plt.title("Synthetic data: interarrival vs service time")

    out_path = results_dir / "plot.png"
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()

    print(f"[03_graficos] Guardado: {out_path}")

if __name__ == "__main__":
    main()