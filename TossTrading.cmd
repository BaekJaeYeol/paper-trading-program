@echo off
setlocal
cd /d "%~dp0"
python "%~dp0start_toss.py"
if errorlevel 1 pause
endlocal
