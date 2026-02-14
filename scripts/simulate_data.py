from pathlib import Path
import numpy as np
import pandas as pd

def main():
    # Semilla fija = misma simulacion siempre (reproducibilidad)
    rng = np.random.default_rng(42)

    # project_root es la carpeta raiz: .../proyecto_investigacion
    project_root = Path(__file__).resolve().parents[1]

    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    n = 500  # numero de observaciones

    # Datos sinteticos:
    df = pd.DataFrame({
        "order_id": np.arange(1, n + 1),
        "interarrival_min": rng.exponential(scale=2.0, size=n),  # tiempo entre llegadas
        "service_min": rng.gamma(shape=2.0, scale=1.5, size=n),  # tiempo de servicio
        "demand_units": rng.poisson(lam=20, size=n)              # demanda (unidades)
    })

    # "Suciedad" intencional para que tenga sentido limpiar:
    # missing values en service_min
    missing_idx = rng.choice(df.index, size=20, replace=False)
    df.loc[missing_idx, "service_min"] = np.nan

    # outliers (tiempos exagerados)
    outlier_idx = rng.choice(df.index, size=5, replace=False)
    df.loc[outlier_idx, "service_min"] *= 20

    out_path = raw_dir / "raw_data.csv"
    df.to_csv(out_path, index=False)

    print(f"[simulate_data] Guardado: {out_path}")

if __name__ == "__main__":
    main()