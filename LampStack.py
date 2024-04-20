import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import threading
import os
import logging

# Impostazione del logger
logging.basicConfig(filename='lamp_xampp_log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def execute_command(command):
    """Esegue un comando shell con subprocess.run e gestisce eventuali errori."""
    try:
        # Esecuzione del comando
        process = subprocess.run(command, shell=True, check=True, text=True)
        logging.info(f"Eseguito comando: {command}\nOutput: {process.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Errore durante l'esecuzione del comando: {command}\nErrore: {e}")
        messagebox.showerror("Errore", f"Errore durante l'esecuzione del comando: {e}")

def xampp():
    """Esegue i comandi per installare XAMPP."""
    commands = [
        'sudo chmod +x ./xampp-linux-installer.run',
        'sudo ./xampp-linux-installer.run',
        'sudo /xampp/lampp start',
    ]

    # Esecuzione dei comandi
    for command in commands:
        execute_command(command)

    messagebox.showinfo("Successo", "Installazione e configurazione di XAMPP completata con successo.")

def lamp_server():
    """Installa il server LAMP."""
    commands = [
        'sudo apt update',
        'sudo apt --fix-broken install',
        'sudo apt clean',
        'sudo rm /var/lib/dpkg/lock-frontend',
        'sudo apt install apache2 ghostscript libapache2-mod-php php php-curl php-imagick php-bcmath php-intl php-json php-mbstring php-mysql php-xml php-yaml php-zip',
    ]

    # Aggiornamento della progress bar
    progress_bar['maximum'] = len(commands)
    progress_bar['value'] = 0

    def run_commands():
        for command in commands:
            execute_command(command)
            progress_bar['value'] += 1
            root.update_idletasks()

        messagebox.showinfo("Successo", "Server LAMP installato con successo.")

    # Avvia l'esecuzione dei comandi in un thread separato
    thread = threading.Thread(target=run_commands)
    thread.start()

def uninstall():
    """Disinstalla il server LAMP."""
    commands = [
        'sudo apt autoremove apache2 ghostscript libapache2-mod-php phpmyadmin php php-curl php-imagick php-bcmath php-intl php-json php-mbstring php-mysql php-xml php-yaml php-zip',
    ]

    # Aggiornamento della progress bar
    progress_bar['maximum'] = len(commands)
    progress_bar['value'] = 0

    def run_uninstall_commands():
        for command in commands:
            execute_command(command)
            progress_bar['value'] += 1
            root.update_idletasks()

        messagebox.showinfo("Successo", "Server LAMP disinstallato con successo.")

    # Avvia l'esecuzione dei comandi in un thread separato
    thread = threading.Thread(target=run_uninstall_commands)
    thread.start()

def change_theme(theme):
    """Cambia il tema dell'interfaccia grafica."""
    style.theme_use(theme)

# Codice GUI
root = tk.Tk()
root.title('CMS LAMP STACK')

style = ThemedStyle(root)
style.set_theme('winxpblue')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Creazione di un controllo a schede (notebook)
tab_control = ttk.Notebook(root)

# Creazione delle schede
tab1 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# Aggiunta delle schede al notebook
tab_control.add(tab1, text='LAMP SERVER')
tab_control.add(tab3, text='UNINSTALL')
tab_control.pack(expand=1, fill="both")

# Creazione dei widget per l'interfaccia utente
user_label = tk.Label(tab1, text="Username:")
user_label.pack(pady=(10, 0))
user_entry = tk.Entry(tab1)
user_entry.pack()

password_label = tk.Label(tab1, text="Password:")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(tab1, show="*")
password_entry.pack()

# Pulsanti per installare e disinstallare
lamp_server_button = ttk.Button(tab1, text="INSTALL LAMP SERVER", command=lamp_server)
lamp_server_button.pack(padx=10, pady=5)

kube_apps_button = ttk.Button(tab1, text="START XAMPP PROJECT", command=xampp)
kube_apps_button.pack(padx=10, pady=5)

lamp_server_uninstall = ttk.Button(tab3, text="UNINSTALL LAMP SERVER", command=uninstall)
lamp_server_uninstall.pack(padx=10, pady=5)

# Progress bar per mostrare i progressi delle operazioni
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

# Imposta la dimensione della finestra principale
root.geometry("400x400")
root.mainloop()
