# Este archivo se encarga del Analisis de los datos.

from pathlib import Path
import pandas as pd

def main():
    project_root = Path(__file__).resolve().parents[1]

    clean_path = project_root / "datos" / "processed" / "clean_data.csv"
    results_dir = project_root / "resultados"
    results_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(clean_path)

    # Tabla resumen
    summary = pd.DataFrame({
        "metric": [
            "n_observations",
            "mean_interarrival_min",
            "mean_service_min",
            "mean_demand_units",
            "p95_service_min",
            "utilization_proxy"
        ],
        "value": [
            len(df),
            df["interarrival_min"].mean(),
            df["service_min"].mean(),
            df["demand_units"].mean(),
            df["service_min"].quantile(0.95),
            df["service_min"].mean() / df["interarrival_min"].mean()
        ]
    })

    out_path = results_dir / "summary_table.csv"
    summary.to_csv(out_path, index=False)

    print(f"[02_analisis] Guardado: {out_path}")

if __name__ == "__main__":
    main()