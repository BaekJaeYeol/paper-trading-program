@echo off
setlocal
cd /d "%~dp0"
if not defined STOCKBOT_PYTHON (
  if exist "%USERPROFILE%\anaconda3\python.exe" (
    set "STOCKBOT_PYTHON=%USERPROFILE%\anaconda3\python.exe"
  ) else (
    set "STOCKBOT_PYTHON=python"
  )
)
"%STOCKBOT_PYTHON%" "%~dp0start_toss.py"
if errorlevel 1 pause
endlocal
