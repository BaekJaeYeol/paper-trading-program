@echo off
cd /d "%~dp0"
if exist .venv\Scripts\python.exe (
    .venv\Scripts\python.exe -m stockbot.gui
) else (
    echo Install first: py -3.12 -m venv .venv
    echo Then: .venv\Scripts\python.exe -m pip install -e .
    pause
)
