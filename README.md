# 🖥 Aliviador de Disco - Windows

🚀 ¿Disco al 100% y Windows lento?  
Libera espacio en segundos con **Aliviador de Disco**: detiene servicios que consumen recursos, limpia temporales y carpetas de actualización, y te muestra todo en tiempo real. **Gratis, seguro y open source**. ¡Mejorá el rendimiento de tu PC ahora!

¿Tu disco está constantemente al **100%** y tu PC se vuelve lenta?  
**Aliviador de Disco** es una herramienta **gratuita y de código abierto** que optimiza tu sistema:  
detiene temporalmente servicios que generan carga, limpia carpetas de actualizaciones y temporales,  
y muestra en **tiempo real** lo que se elimina.

---

## ✨ Características principales

- 🛑 **Detiene temporalmente servicios de Windows que consumen disco:**
  - `BITS` (Servicio de transferencia inteligente en segundo plano)
  - `wuauserv` (Windows Update)

- 🧹 **Elimina de forma segura archivos que ocupan espacio innecesario:**
  - `C:\Windows\SoftwareDistribution\Download`
  - `%TEMP%` (carpeta temporal del usuario)

- 📊 **Interfaz gráfica amigable:**
  - Ventana con `Listbox/ScrolledText` que muestra en tiempo real cada archivo eliminado.
  - Botones de **Iniciar** y **Detener** para controlar la limpieza.

- 💾 **Generación automática de logs:**
  - Carpeta `AliviadorLogs` dentro de la carpeta del `.exe`  
    (ejemplo: `dist/AliviadorLogs`) con fecha y hora para seguimiento.

- ✅ **Resumen final de limpieza:**
  - Cantidad de archivos eliminados
  - Espacio total liberado en MB

---

## 🖥 Requisitos del sistema

- **Windows 10 / 11**  
- **Python 3.8+** (solo si compilas desde código)  
- **Ejecutar como Administrador** para máxima efectividad
- ⚠️ Recomendado especialmente para PCs con discos mecánicos (HDD), donde liberar espacio puede mejorar notablemente el rendimiento. Para SSD también funciona, pero los beneficios en velocidad son menores.
---

## 🚀 Cómo usar (usuario final)

1. **Descarga** el `.exe` desde la sección **Releases** del repo.  
2. Haz **clic derecho** en el ejecutable y selecciona **"Ejecutar como administrador"**.  
3. Presiona **Iniciar** y observa los archivos eliminados en tiempo real.  
4. Si quieres interrumpir la limpieza, presiona **Detener**.  
5. Al finalizar:
   - Verás un **resumen final** en pantalla.  
   - Encontrarás un **log detallado** en `AliviadorLogs`.

> Ideal para solucionar problemas de disco lleno y mejorar el rendimiento de PCs con Windows.

---

## 🛠 Cómo compilar desde el código

1. **Clona este repositorio:**

   git clone https://github.com/juan27k/AliviarDiscoPython.git
   cd AliviadorDiscoPython
(Opcional) Instala dependencias:


python -m pip install pyinstaller
Genera el ejecutable:


pyinstaller --noconsole --onefile --icon=icono.ico AliviarDiscoPython.py
El .exe se generará en dist/.

📂 Estructura del proyecto
AliviadorDeDisco/
├── build/              # Carpeta generada por PyInstaller
├── dist/               # Ejecutable generado (.exe)
│   └── AliviadorDiscoPython.exe
├── AliviadorLogs/      # Carpeta de logs creada al ejecutar el exe
├── screenshots/        # Capturas de pantalla del programa
│   └── interfaz.png
├── icono.ico           # Icono del programa
├── AliviarDiscoPython.py # Código principal
├── README.md           # Este archivo
└── requirements.txt    # (Opcional) dependencias para compilar


📷 Capturas de Pantalla
<p align="center">
  <img src="screenshots/interfaz.png" alt="Interfaz Aliviador de Disco" width="600"/>
</p>
📢 Nota Importante
Esta herramienta no desactiva permanentemente servicios de Windows.

Los servicios BITS y wuauserv se reinician automáticamente después de la limpieza.

Usar bajo tu propia responsabilidad en entornos productivos.

📜 Licencia
Distribuido bajo la licencia MIT.
Eres libre de usar, modificar y compartir esta herramienta.

❤️ Contribuciones
¿Tenés ideas para mejorar la herramienta?
Abre un Issue o envía un Pull Request. ¡Toda contribución es bienvenida!

💰 Donaciones
Si querés apoyar el desarrollo y futuras mejoras, podés donar a mi alias: juan27k
