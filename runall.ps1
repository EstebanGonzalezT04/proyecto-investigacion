$ErrorActionPreference = "Stop"

Write-Host "[runall] Iniciando pipeline..." -ForegroundColor Green

# Raíz del proyecto (donde está este runall.ps1)
$PROJECT_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $PROJECT_ROOT

# Carpetas necesarias
Write-Host "[runall] Verificando carpetas..." -ForegroundColor Green
New-Item -ItemType Directory -Force -Path ".\data\raw" | Out-Null
New-Item -ItemType Directory -Force -Path ".\data\processed" | Out-Null
New-Item -ItemType Directory -Force -Path ".\results\figures" | Out-Null
New-Item -ItemType Directory -Force -Path ".\results\tables" | Out-Null

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
conda run -n $ENV_NAME python .\scripts\simulate_data.py

Write-Host "[runall] Ejecutando 01_limpieza.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\scripts\01_limpieza.py

Write-Host "[runall] Ejecutando 02_analisis.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\scripts\02_analisis.py

Write-Host "[runall] Ejecutando 03_graficos.py" -ForegroundColor Green
conda run -n $ENV_NAME python .\scripts\03_graficos.py

Write-Host "[runall] Listo. Outputs en .\results" -ForegroundColor Green