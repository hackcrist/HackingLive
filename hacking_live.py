
#!/usr/bin/env python3
# coded by HackCrist

import sys
import os
import webbrowser
import subprocess

def __limpiar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def abrir_url(url):
    if 'com.termux' in os.getenv('PREFIX', ''):
        subprocess.call(['termux-open-url', url])
    else:
        webbrowser.open(url)

def menu():
    while True:
        __limpiar()
        print("""

[1;31m                                ____            _
[1;31m                               |  _ \  _____  _(_)_ __   __ _
[1;37m                               | | | |/ _ \\ \/ / | '_ \\ / _` |
[1;37m                               | |_| | (_) >  <| | | | | (_| |
[1;31m                               |____/ \\___/_/\\_\\_|_| |_|\\__, |
[1;31m                                                        |___/

                          [1;31mHacking Live[1;m
              [1;34mHecho por:[1;m HackCrist

""")

        print('''
[1;32m 1. Pipl      [1;32m 7. Sis            [1;32m 13. Censo           [1;32m19. Sanciones   [1;32m 25. Direccion
[1;32m 2. Dni       [1;32m 8. FecNac         [1;32m 14. EstadoDoc    [1;32m   20. Sat      [1;32m 26. SkypeIp
[1;32m 3. EstCiv    [1;32m 9. Credito        [1;32m 15. BuscarDatos  [1;32m   21. Runt     [1;32m 27. Multas
[1;32m 4. Operdora  [1;32m 10. Sentinel      [1;32m 16. Certificados [1;32m   22. Libreta  [1;32m 28. Username
[1;32m 5. Ruc       [1;32m 11. ExifData      [1;32m 17. Licencia     [1;32m   23. StalkScan[1;32m 29. About
[1;32m 6. Tinfoleak [1;32m 12. Acreditacion  [1;32m 18. Curp         [1;32m   24. Colegiados[1;32m 30. Exit
''')

        d = input("\033[1;30m Doxing > ")

        urls = {
            "1": 'https://pipl.com/',
            "2": 'http://www.consultadni.info/',
            "3": 'https://cel.reniec.gob.pe/valreg/valreg.do',
            "4": 'http://www.deperu.com/celulares/',
            "5": 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias',
            "6": 'https://tinfoleak.com/',
            "7": 'http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx',
            "8": 'https://www.reniec.gob.pe/concer/concer.do',
            "9": 'https://www.icetex.gov.co/portalacces/tradicional/solicitar/cptConsultarEstado.asp?origen=portal',
            "10": 'https://misentinel.sentinelperu.com/misentinel/misentinel.aspx',
            "11": 'http://exifdata.com',
            "12": 'http://ww4.essalud.gob.pe:7777/acredita/index.jsp',
            "13": 'https://wsp.registraduria.gov.co/censo/_censoResultado.php',
            "14": 'https://wsp.registraduria.gov.co/estadodocs/',
            "15": 'http://buscardatos.com/',
            "16": 'http://certificados.sena.edu.co/',
            "17": 'http://web.mintransporte.gov.co/Consultas/transito/Consulta23122010.htm',
            "18": 'https://consultas.curp.gob.mx/',
            "19": 'https://consulta.simit.org.co/Simit/index.html',
            "20": 'https://www.sat.gob.pe/Websitev9',
            "21": 'https://www.runt.com.co/consultaCiudadana/#/consultaPersona',
            "22": 'https://www.libretamilitar.mil.co/Modules/Consult/MilitarySituation',
            "23": 'https://stalkscan.com/',
            "24": 'http://www.cipica.com/buscolegiado/buscolegiado.php',
            "25": 'http://www.midis.gob.pe/padron/',
            "26": 'http://mostwantedhf.info/',
            "27": 'http://aplicaciones007.jne.gob.pe/multas/',
            "28": 'https://namechk.com/',
            "29": 'https://www.facebook.com/HackingEnVivo/'
        }

        if d in urls:
            abrir_url(urls[d])
        elif d == "30":
            print("\nSaliendo...\n")
            sys.exit()
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            input("\nPresiona ENTER para continuar...")

menu()
