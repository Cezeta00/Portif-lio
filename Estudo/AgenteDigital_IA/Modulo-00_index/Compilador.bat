@echo off
cd C:\Users\Isaac\Estudo\AgenteDigital_IA\Modulo-00_index
python -m PyInstaller --onefile rastreador.py
python -m PyInstaller --onefile trancritor.py
python -m PyInstaller --onefile conversor.py
pause
