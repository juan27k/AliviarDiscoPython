# 🖥 Aliviador de Disco - Windows

¿Tu disco está constantemente al **100%** y tu PC se vuelve lenta?  
**Aliviador de Disco** es una herramienta **gratuita y de código abierto** que optimiza tu sistema:  
detiene temporalmente servicios que generan carga, limpia carpetas de actualizaciones y temporales,  
y muestra en **tiempo real** lo que se elimina.

---

## ✨ Características

- 🛑 **Detiene temporalmente los servicios:**
  - `BITS` (Servicio de transferencia inteligente en segundo plano)
  - `wuauserv` (Windows Update)

- 🧹 **Borra de forma segura:**
  - `C:\Windows\SoftwareDistribution\Download`
  - `%TEMP%` (carpeta temporal del usuario)

- 📊 **Interfaz gráfica amigable:**
  - Ventana con `Listbox/ScrolledText` que muestra en tiempo real cada archivo eliminado.
  - Botones de **Iniciar** y **Detener** para controlar el proceso.

- 💾 **Genera logs automáticos:**
  - Se crean en `AliviadorLogs` dentro de la carpeta donde se ejecuta el `.exe`  
    (por ejemplo, `dist/AliviadorLogs`) con fecha y hora para futuras revisiones.

- ✅ **Resumen final:**
  - Cantidad de archivos eliminados
  - Espacio total liberado en MB

---

## 🖥 Requisitos

- **Sistema Operativo:** Windows 10 / 11
- **Python 3.8+** (solo si vas a compilar desde código)
- Para maximizar la efectividad: **Ejecutar como Administrador**  
  (necesario para detener servicios y borrar `SoftwareDistribution`)

---

## 🚀 Cómo usar (usuario final)

1. **Descarga** el `.exe` desde la sección **Releases** del repo.
2. Haz **clic derecho** en el ejecutable y selecciona  
   **"Ejecutar como administrador"** (recomendado).
3. Presiona **Iniciar** y observa en tiempo real los archivos eliminados.
4. Si deseas interrumpir la limpieza, presiona **Detener**.
5. Al finalizar:
   - Verás un **resumen final** en pantalla.
   - Encontrarás un log detallado en `AliviadorLogs` dentro de la carpeta del `.exe`.

---

## 🛠 Cómo compilar desde el código

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/TU-USUARIO/AliviadorDeDisco.git
   cd AliviadorDeDisco
(Opcional) Instala dependencias:

bash
Copiar código
python -m pip install pyinstaller
Genera el ejecutable:

bash
Copiar código
pyinstaller --noconsole --onefile --icon=icono.ico AliviarDiscoPython.py
El ejecutable se generará en la carpeta dist/.

📂 Estructura del Proyecto
bash
Copiar código
AliviadorDeDisco/
│
├── build/                   # Carpeta generada por PyInstaller
├── dist/                    # Ejecutable generado (.exe)
│   └── AliviarDiscoPython.exe
├── AliviadorLogs/           # Carpeta de logs creada al ejecutar el exe
├── screenshots/             # Capturas de pantalla del programa
│   └── interfaz.png
├── icono.ico                # Icono del programa
├── AliviarDiscoPython.py    # Código principal
├── README.md                # Este archivo
└── requirements.txt         # (Opcional) dependencias para compilar
📷 Capturas de Pantalla
(Agrega aquí una o más imágenes de la interfaz en acción para que el usuario vea cómo luce.)
<img width="959" height="622" alt="image" src="https://github.com/user-attachments/assets/ad32ba59-aaec-4c4b-8f26-92b4990e3dc4" />

📢 Nota Importante
Esta herramienta no desactiva permanentemente servicios de Windows.
Después de la limpieza, los servicios BITS y wuauserv se reinician automáticamente.

Usar bajo tu propia responsabilidad en entornos productivos.

📜 Licencia
Distribuido bajo la licencia MIT.
¡Eres libre de usar, modificar y compartir esta herramienta!

❤️ Contribuciones
¿Tienes ideas para mejorar la herramienta?
Puedes abrir un Issue o enviar un Pull Request.
¡Toda contribución es bienvenida!

💰 Donaciones
Si querés apoyar el desarrollo y futuras mejoras, podés hacer donaciones a mi alias:
juan27k

markdown
Copiar código

Si querés, puedo también agregar un pequeño **banner gráfico de donaciones** para que quede más visual en GitHub.  

¿Querés que haga eso?






Tú dijiste:
dale y reducime un 50% el tamaño de el screenshot


ChatGPT Plus
Perfecto, Juan. Te hice el README actualizado con:

Screenshot reducido al 50% de tamaño.

Banner visual de donaciones agregado.

markdown
Copiar código
# 🖥 Aliviador de Disco - Windows

¿Tu disco está constantemente al **100%** y tu PC se vuelve lenta?  
**Aliviador de Disco** es una herramienta **gratuita y de código abierto** que optimiza tu sistema:  
detiene temporalmente servicios que generan carga, limpia carpetas de actualizaciones y temporales,  
y muestra en **tiempo real** lo que se elimina.

---

## ✨ Características

- 🛑 **Detiene temporalmente los servicios:**
  - `BITS` (Servicio de transferencia inteligente en segundo plano)
  - `wuauserv` (Windows Update)

- 🧹 **Borra de forma segura:**
  - `C:\Windows\SoftwareDistribution\Download`
  - `%TEMP%` (carpeta temporal del usuario)

- 📊 **Interfaz gráfica amigable:**
  - Ventana con `Listbox/ScrolledText` que muestra en tiempo real cada archivo eliminado.
  - Botones de **Iniciar** y **Detener** para controlar el proceso.

- 💾 **Genera logs automáticos:**
  - Se crean en `AliviadorLogs` dentro de la carpeta donde se ejecuta el `.exe`  
    (por ejemplo, `dist/AliviadorLogs`) con fecha y hora para futuras revisiones.

- ✅ **Resumen final:**
  - Cantidad de archivos eliminados
  - Espacio total liberado en MB

---

## 🖥 Requisitos

- **Sistema Operativo:** Windows 10 / 11
- **Python 3.8+** (solo si vas a compilar desde código)
- Para maximizar la efectividad: **Ejecutar como Administrador**  
  (necesario para detener servicios y borrar `SoftwareDistribution`)

---

## 🚀 Cómo usar (usuario final)

1. **Descarga** el `.exe` desde la sección **Releases** del repo.
2. Haz **clic derecho** en el ejecutable y selecciona  
   **"Ejecutar como administrador"** (recomendado).
3. Presiona **Iniciar** y observa en tiempo real los archivos eliminados.
4. Si deseas interrumpir la limpieza, presiona **Detener**.
5. Al finalizar:
   - Verás un **resumen final** en pantalla.
   - Encontrarás un log detallado en `AliviadorLogs` dentro de la carpeta del `.exe`.

---

## 🛠 Cómo compilar desde el código

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/TU-USUARIO/AliviadorDeDisco.git
   cd AliviadorDeDisco
(Opcional) Instala dependencias:

bash
Copiar código
python -m pip install pyinstaller
Genera el ejecutable:

bash
Copiar código
pyinstaller --noconsole --onefile --icon=icono.ico AliviarDiscoPython.py
El ejecutable se generará en la carpeta dist/.

📂 Estructura del Proyecto
bash
Copiar código
AliviadorDeDisco/
│
├── build/                   # Carpeta generada por PyInstaller
├── dist/                    # Ejecutable generado (.exe)
│   └── AliviadorDiscoPython.exe
├── AliviadorLogs/           # Carpeta de logs creada al ejecutar el exe
├── screenshots/             # Capturas de pantalla del programa
│   └── interfaz.png
├── icono.ico                # Icono del programa
├── AliviarDiscoPython.py    # Código principal
├── README.md                # Este archivo
└── requirements.txt         # (Opcional) dependencias para compilar
📷 Capturas de Pantalla
(Agrega aquí una o más imágenes de la interfaz en acción para que el usuario vea cómo luce.)
<img width="480" height="311" alt="image" src="https://github.com/user-attachments/assets/ad32ba59-aaec-4c4b-8f26-92b4990e3dc4" />

📢 Nota Importante
Esta herramienta no desactiva permanentemente servicios de Windows.
Después de la limpieza, los servicios BITS y wuauserv se reinician automáticamente.

Usar bajo tu propia responsabilidad en entornos productivos.

📜 Licencia
Distribuido bajo la licencia MIT.
¡Eres libre de usar, modificar y compartir esta herramienta!

❤️ Contribuciones
¿Tienes ideas para mejorar la herramienta?
Puedes abrir un Issue o enviar un Pull Request.
¡Toda contribución es bienvenida!

💰 Donaciones
Si querés apoyar el desarrollo y futuras mejoras, podés hacer donaciones a mi alias:
juan27k
