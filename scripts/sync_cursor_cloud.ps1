# Синхронизация agents/skills/rules → .cursor/ (после правок плагина)
$root = Split-Path $PSScriptRoot -Parent
Copy-Item "$root\agents\*" "$root\.cursor\agents\" -Force
Copy-Item "$root\skills\*" "$root\.cursor\skills\" -Recurse -Force
Copy-Item "$root\rules\*" "$root\.cursor\rules\" -Force
Write-Host "OK: .cursor synced from agents/skills/rules"
