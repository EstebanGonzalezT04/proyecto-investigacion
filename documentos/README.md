# Taller 2 – Automatizacion y Reproducibilidad (Python)

## Estructura del proyecto
- `datos/raw/`: datos sinteticos crudos (`raw_data.csv`)
- `datos/processed/`: datos limpios (`clean_data.csv`)
- `codigo/`: scripts del flujo de trabajo
- `resultados/`: outputs finales (tabla y figura)
- `environment.yml`: definicion del entorno conda
- `runall.ps1`: ejecuta todo el pipeline automaticamente

## Como ejecutar
Desde PowerShell, en la raiz del proyecto:

```powershell
.\runall.ps1