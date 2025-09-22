# 🖥 Aliviador de Disco - Windows


¿Tu disco está constantemente al **100%** y el PC se vuelve lento? **Aliviador de Disco** es una herramienta gratuita y de código abierto que aliviana tu sistema: detiene temporalmente servicios que generan carga, limpia carpetas de actualizaciones y temporales, y muestra en tiempo real lo que se elimina.


## Características


- 🛑 Detiene temporalmente los servicios:
- **BITS** (Servicio de transferencia inteligente en segundo plano)
- **wuauserv** (Windows Update)
- 🧹 Borra de forma segura:
- `C:\Windows\SoftwareDistribution\Download`
- `%TEMP%` (temporal del usuario)
- 📊 Interfaz gráfica con **Listbox/ScrolledText** que muestra cada archivo eliminado en tiempo real.
- 💾 Genera un log en `C:\AliviadorLogs` (archivo con timestamp).
- ✅ Resumen final con archivos eliminados y MB liberados.


## Requisitos


- Windows 10/11
- Python 3.8+ (si compilas desde código) o simplemente el `.exe` en `dist/`.
- Para maximizar la efectividad: **Ejecutar como Administrador** (necesario para detener servicios y borrar `SoftwareDistribution`).


## Cómo usar (usuario final)


1. Descarga el `.exe` desde la sección **Releases** del repo.
2. Clic derecho -> **Ejecutar como administrador** (recomendado).
3. Presiona **Iniciar**. Observa en la ventana los archivos que se van eliminando.
4. Presiona **Detener** si querés interrumpir la limpieza.
5. Al terminar verás un resumen y el log estará en `C:\AliviadorLogs`.


## Cómo compilar desde el código


1. Instalar dependencias (opcional):


```bash
python -m pip install pyinstaller
