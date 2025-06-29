#!/bin/bash
# Instalador HackCrist

clear
echo "======================================="
echo "   🚀 Instalador de Hacking Live Beta  "
echo "======================================="

echo "[+] Actualizando paquetes..."
pkg update -y && pkg upgrade -y

echo "[+] Instalando Python..."
pkg install python -y

echo "[+] Instalando xdg-utils..."
pkg install xdg-utils -y

echo "[+] Clonando repositorio..."
echo "Recuerda reemplazar el link por tu GitHub."
# git clone https://github.com/USUARIO/REPO.git

echo "[+] Dando permisos de ejecución..."
chmod +x hacking_live.py

echo ""
echo "✅ Instalación lista."
echo "Ejecuta: python hacking_live.py"
