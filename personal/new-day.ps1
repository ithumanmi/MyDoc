# Usage:
#   .\personal\new-day.ps1
#   .\personal\new-day.ps1 -Date 2026-08-08

param(
  [string]$Date = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot

$y = $Date.Substring(0, 4)
$dailyDir = Join-Path $root "personal/daily/$y"
$nutriDir = Join-Path $root "personal/nutrition/$y"
New-Item -ItemType Directory -Force -Path $dailyDir, $nutriDir | Out-Null

$dailySrc = Join-Path $root 'templates/personal/daily-entry.md'
$nutriSrc = Join-Path $root 'templates/personal/nutrition-day.md'
$dailyDst = Join-Path $dailyDir "$Date.md"
$nutriDst = Join-Path $nutriDir "$Date.md"

if (Test-Path $dailyDst) {
  Write-Host "Exists: $dailyDst"
} else {
  (Get-Content $dailySrc -Raw) -replace 'YYYY-MM-DD', $Date | Set-Content -Path $dailyDst -Encoding UTF8
  Write-Host "Created $dailyDst"
}

if (Test-Path $nutriDst) {
  Write-Host "Exists: $nutriDst"
} else {
  (Get-Content $nutriSrc -Raw) -replace 'YYYY-MM-DD', $Date | Set-Content -Path $nutriDst -Encoding UTF8
  Write-Host "Created $nutriDst"
}

Write-Host "Don't forget: append a row to personal/body/metrics.csv"
