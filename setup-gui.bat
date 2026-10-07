@echo off
cd /d "%~dp0"
if exist .venv\Scripts\python.exe goto install
py -3 -m venv .venv
if not errorlevel 1 goto install
python -m venv .venv
if errorlevel 1 goto failed
:install
.venv\Scripts\python.exe -c "import sys; assert sys.version_info >= (3,11)"
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m pip install -e .
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m stockbot.gui
if errorlevel 1 goto failed
exit /b 0
:failed
echo Setup or launch failed. Python 3.11+ and internet are required.
pause
exit /b 1
