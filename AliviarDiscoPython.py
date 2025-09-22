import os
import shutil
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time
import subprocess
import sys

stop_flag = False

# --- Carpeta de logs dentro de la carpeta del exe ---
if getattr(sys, 'frozen', False):
    # Ejecutable
    base_path = os.path.dirname(sys.executable)
else:
    # Script
    base_path = os.path.dirname(os.path.abspath(__file__))

LOG_FOLDER = os.path.join(base_path, "AliviadorLogs")
os.makedirs(LOG_FOLDER, exist_ok=True)

log_file_name = f"Log_Aliviador_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
log_file_path = os.path.join(LOG_FOLDER, log_file_name)

# --- Función para log ---
def logear(texto):
    root_window.after(0, lambda: _logear_gui(texto))

def _logear_gui(texto):
    listbox.insert(tk.END, texto)
    listbox.yview(tk.END)
    progreso.update_idletasks()
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

# --- Funciones de servicios ---
def detener_servicio(nombre):
    try:
        result = subprocess.run(["sc", "query", nombre], capture_output=True, text=True)
        if "RUNNING" in result.stdout:
            logear(f"Deteniendo {nombre}...")
            subprocess.run(["net", "stop", nombre], capture_output=True)
        else:
            logear(f"{nombre} ya estaba detenido. Omitiendo.")
    except Exception as e:
        logear(f"⚠ Error al detener {nombre}: {e}")

def reiniciar_servicio(nombre):
    try:
        logear(f"Reiniciando {nombre}...")
        subprocess.run(["net", "start", nombre], capture_output=True)
    except Exception as e:
        logear(f"⚠ Error al reiniciar {nombre}: {e}")

# --- Pausar proceso AggregatorHost ---
def pausar_aggregator():
    try:
        result = subprocess.run(["tasklist"], capture_output=True, text=True)
        if "AggregatorHost.exe" in result.stdout:
            logear("Pausando AggregatorHost.exe...")
            subprocess.run(["taskkill", "/f", "/im", "AggregatorHost.exe"], capture_output=True)
        else:
            logear("AggregatorHost.exe no se encuentra. Omitiendo.")
    except Exception as e:
        logear(f"⚠ Error al pausar AggregatorHost.exe: {e}")

# --- Función principal ---
def limpiar_carpetas():
    global stop_flag
    stop_flag = False
    archivos_eliminados = 0
    espacio_liberado = 0

    # Carpetas a limpiar
    carpetas = [
        os.path.join(os.environ.get("windir"), "SoftwareDistribution", "Download"),
        os.environ.get("TEMP")
    ]

    # Contar archivos totales
    archivos_totales = 0
    for carpeta in carpetas:
        if carpeta and os.path.exists(carpeta):
            for _, _, files in os.walk(carpeta):
                archivos_totales += len(files)
    if archivos_totales == 0:
        messagebox.showinfo("Aliviador de Disco", "No hay archivos para limpiar.")
        return

    progreso["maximum"] = archivos_totales
    progreso["value"] = 0
    listbox.delete(0, tk.END)

    logear("==============================")
    logear("   ALIVIAR USO DE DISCO HDD")
    logear("==============================\n")

    # Detener servicios
    detener_servicio("wuauserv")
    detener_servicio("BITS")
    pausar_aggregator()

    # Borrar archivos
    for carpeta in carpetas:
        if carpeta and os.path.exists(carpeta):
            logear(f"\nBorrando: {carpeta}")
            for root, dirs, files in os.walk(carpeta):
                for file in files:
                    if stop_flag:
                        logear("⏹ Limpieza detenida por el usuario.")
                        return
                    try:
                        ruta = os.path.join(root, file)
                        espacio_liberado += os.path.getsize(ruta)
                        os.remove(ruta)
                        archivos_eliminados += 1
                        logear(f"🗑 Eliminado: {ruta}")
                    except Exception as e:
                        logear(f"⚠ No se pudo eliminar: {ruta} ({e})")
                    progreso["value"] += 1
            # Eliminar carpetas vacías
            for root, dirs, _ in os.walk(carpeta, topdown=False):
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d))
                    except: pass

    # Reiniciar servicios
    reiniciar_servicio("wuauserv")
    reiniciar_servicio("BITS")

    # Mostrar resumen
    espacio_mb = espacio_liberado / (1024*1024)
    logear("\n==============================")
    logear("         RESUMEN FINAL")
    logear("==============================")
    logear(f"Archivos eliminados: {archivos_eliminados}")
    logear(f"Espacio liberado: {espacio_mb:.2f} MB")
    logear(f"Log guardado en: {log_file_path}")
    messagebox.showinfo(
        "Resumen de Limpieza",
        f"Archivos eliminados: {archivos_eliminados}\n"
        f"Espacio liberado: {espacio_mb:.2f} MB\n"
        f"Log guardado en: {log_file_path}"
    )

# --- Botones ---
def iniciar_limpieza():
    hilo = threading.Thread(target=limpiar_carpetas)
    hilo.daemon = True
    hilo.start()

def detener_limpieza():
    global stop_flag
    stop_flag = True

def cerrar_ventana():
    global stop_flag
    stop_flag = True
    root_window.destroy()

# --- GUI ---
root_window = tk.Tk()
root_window.title("Aliviador de Discos Duros")
root_window.geometry("750x450")
root_window.resizable(False, False)

titulo = tk.Label(root_window, text="🖥 Aliviador de Discos Duros", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

progreso = ttk.Progressbar(root_window, length=700, mode="determinate")
progreso.pack(pady=5)

frame_listbox = tk.Frame(root_window)
frame_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_listbox, width=110, height=20, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

frame_botones = tk.Frame(root_window)
frame_botones.pack(pady=5)

btn_iniciar = tk.Button(frame_botones, text="Iniciar", command=iniciar_limpieza, bg="#4CAF50", fg="white", width=15)
btn_iniciar.grid(row=0, column=0, padx=10)

btn_detener = tk.Button(frame_botones, text="Detener", command=detener_limpieza, bg="#F44336", fg="white", width=15)
btn_detener.grid(row=0, column=1, padx=10)

root_window.protocol("WM_DELETE_WINDOW", cerrar_ventana)
root_window.mainloop()
