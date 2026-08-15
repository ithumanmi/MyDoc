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
$skinDir = Join-Path $root "personal/skincare/$y"
New-Item -ItemType Directory -Force -Path $dailyDir, $nutriDir, $skinDir | Out-Null

$dailySrc = Join-Path $root 'templates/personal/daily-entry.md'
$nutriSrc = Join-Path $root 'templates/personal/nutrition-day.md'
$skinSrc = Join-Path $root 'templates/personal/skincare-day.md'
$dailyDst = Join-Path $dailyDir "$Date.md"
$nutriDst = Join-Path $nutriDir "$Date.md"
$skinDst = Join-Path $skinDir "$Date.md"

function Copy-DayTemplate {
  param([string]$Src, [string]$Dst, [string]$Date)
  if (Test-Path $Dst) {
    Write-Host "Exists: $Dst"
    return
  }
  $text = [System.IO.File]::ReadAllText($Src)
  $text = $text.Replace('YYYY-MM-DD', $Date)
  $utf8NoBom = New-Object System.Text.UTF8Encoding $false
  [System.IO.File]::WriteAllText($Dst, $text, $utf8NoBom)
  Write-Host "Created $Dst"
}

Copy-DayTemplate -Src $dailySrc -Dst $dailyDst -Date $Date
Copy-DayTemplate -Src $nutriSrc -Dst $nutriDst -Date $Date
Copy-DayTemplate -Src $skinSrc -Dst $skinDst -Date $Date

Write-Host "Don't forget: append a row to personal/body/metrics.csv"
Write-Host "Sunday: python scripts/personal_week_summary.py --week YYYY-Www --write"
