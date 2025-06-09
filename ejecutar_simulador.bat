@echo off
echo Instalando dependencias necesarias...
python -m pip install --upgrade pip
pip install networkx matplotlib

echo.
echo Ejecutando simulador de Dijkstra...
python simulador.py

pause
