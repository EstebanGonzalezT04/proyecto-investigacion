# Este archivo se encarga de la limpieza de los datos.

from pathlib import Path
import pandas as pd

def main():
    project_root = Path(__file__).resolve().parents[1]

    raw_path = project_root / "data" / "raw" / "raw_data.csv"
    processed_dir = project_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(raw_path)

    # 1) Missing values: eliminar filas con service_min faltante
    before = len(df)
    df = df.dropna(subset=["service_min"])
    after = len(df)

    # 2) Outliers: cap con percentil 99 (winsorize simple)
    cap = df["service_min"].quantile(0.99)
    df["service_min"] = df["service_min"].clip(upper=cap)

    out_path = processed_dir / "clean_data.csv"
    df.to_csv(out_path, index=False)

    print(f"[01_limpieza] Lei: {raw_path}")
    print(f"[01_limpieza] Filas antes: {before} | despues dropna: {after}")
    print(f"[01_limpieza] Cap outliers p99(service_min) = {cap:.3f}")
    print(f"[01_limpieza] Guardado: {out_path}")

if __name__ == "__main__":
    main()