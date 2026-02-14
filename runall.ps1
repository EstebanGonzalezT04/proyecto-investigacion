$ErrorActionPreference = "Stop"

Write-Host "[runall] Iniciando pipeline..." -ForegroundColor Green

# Raíz del proyecto (donde está este runall.ps1)
$PROJECT_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $PROJECT_ROOT

# Carpetas necesarias
Write-Host "[runall] Verificando carpetas..." -ForegroundColor Green
New-Item -ItemType Directory -Force -Path ".\datos\raw" | Out-Null
New-Item -ItemType Directory -Force -Path ".\datos\processed" | Out-Null
New-Item -ItemType Directory -Force -Path ".\resultados" | Out-Null

# Entorno conda
$ENV_NAME = "taller2_env"
Write-Host "[runall] Verificando entorno conda: $ENV_NAME" -ForegroundColor Green

$envExists = conda env list | Select-String -Pattern "^\s*$ENV_NAME\s"
if (-not $envExists) {
    Write-Host "[runall] Entorno no existe. Creándolo desde environment.yml..." -ForegroundColor Yellow
    conda env create -f environment.yml
} else {
    Write-Host "[runall] Entorno encontrado." -ForegroundColor Green
}

# Ejecutar scripts (sin activar manualmente)
Write-Host "[runall] Ejecutando simulate_data.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\codigo\simulate_data.py

Write-Host "[runall] Ejecutando 01_limpieza.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\codigo\01_limpieza.py

Write-Host "[runall] Ejecutando 02_analisis.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\codigo\02_analisis.py

Write-Host "[runall] Ejecutando 03_graficos.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\codigo\03_graficos.py

Write-Host "[runall] Listo. Outputs en .\resultados" -ForegroundColor Green