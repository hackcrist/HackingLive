#!/bin/bash
# Instalador Hacking Live — DOXING TOOL
# Autor: HackCrist

clear
echo "======================================="
echo "   🚀 Instalador de Hacking Live DOXING"
echo "======================================="

echo "[+] Actualizando paquetes..."
pkg update -y && pkg upgrade -y

echo "[+] Instalando Python..."
pkg install python -y

echo "[+] Instalando xdg-utils..."
pkg install xdg-utils -y

echo "[+] Clonando repositorio..."
git clone https://github.com/hackcrist/HackingLive.git
cd HackingLive

echo "[+] Dando permisos de ejecución..."
chmod +x hacking_live.py

echo ""
echo "✅ Instalación lista. Ejecuta:"
echo ""
echo "  python hacking_live.py"
echo ""
echo "Recuerda ver la portada banner.png en tu repositorio GitHub!"
