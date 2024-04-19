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

def xampp():
    # Definisci il percorso assoluto della cartella del progetto
    
    # Comandi per installare LAMP e XAMPP
    commands = [
        'sudo chmod +x ./xampp-linux-installer.run',
        'sudo ./xampp-linux-installer.run',
        'sudo /xampp/lampp start',
    ]
    
    try:
        # Esecuzione dei comandi
        for command in commands:
            process = subprocess.run(command, shell=True, check=True, text=True)
            logging.info(f"Eseguito comando: {command}\nOutput: {process.stdout}\n")
        
        messagebox.showinfo("Successo", "Installazione e configurazione di LAMP e XAMPP completata con successo.")
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Errore durante l'esecuzione dei comandi: {e}")
        messagebox.showerror("Errore", f"Errore durante l'esecuzione dei comandi: {e}")

def lamp_server():
    # Comandi per l'installazione del server LAMP
    commands = [
        'sudo apt update',
        'sudo apt --fix-broken install',
        'sudo apt clean',
        'sudo rm /var/lib/dpkg/lock-frontend',
        'sudo apt install apache2',
        'sudo apt install ghostscript',
        'sudo apt install libapache2-mod-php',
        'sudo apt install postgresql',
        'sudo apt install php',
        'sudo apt install php-curl',
        'sudo apt install php-imagick',
        'sudo apt install php-bcmath',
        'sudo apt install php-intl',
        'sudo apt install php-json',
        'sudo apt install php-mbstring',
        'sudo apt install php-mysql',
        'sudo apt install php-xml',
        'sudo apt install php-yaml',
        'sudo apt install php-zip',
    ]
    
    progress_bar['maximum'] = len(commands)
    progress_bar['value'] = 0

    def run_commands():
        try:
            for command in commands:
                process = subprocess.run(command, shell=True, check=True, text=True)
                logging.info(f"Eseguito comando: {command}\nOutput: {process.stdout}\n")
                
                progress_bar['value'] += 1
                root.update_idletasks()

            messagebox.showinfo("Successo", "Server LAMP installato con successo.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Errore durante l'installazione del Server LAMP: {e}")
            messagebox.showerror("Errore", f"Errore durante l'installazione del Server LAMP: {e}")

    # Avvia l'esecuzione dei comandi in un thread separato
    thread = threading.Thread(target=run_commands)
    thread.start()

def uninstall():
    # Comandi per la disinstallazione
    commands = [
        'sudo apt autoremove apache2',
        'sudo apt autoremove ghostscript',
        'sudo apt autoremove libapache2-mod-php',
        'sudo apt autoremove phpmyadmin',
        'sudo apt autoremove php',
        'sudo apt autoremove php-curl',
        'sudo apt autoremove php-imagick',
        'sudo apt autoremove php-bcmath',
        'sudo apt autoremove php-intl',
        'sudo apt autoremove php-json',
        'sudo apt autoremove php-mbstring',
        'sudo apt autoremove php-mysql',
        'sudo apt autoremove php-xml',
        'sudo apt autoremove php-yaml',
        'sudo apt autoremove php-zip',
    ]

    progress_bar['maximum'] = len(commands)
    progress_bar['value'] = 0

    def run_uninstall_commands():
        try:
            for command in commands:
                process = subprocess.run(command, shell=True, check=True, text=True)
                logging.info(f"Eseguito comando: {command}\nOutput: {process.stdout}\n")
                
                progress_bar['value'] += 1
                root.update_idletasks()

            messagebox.showinfo("Successo", "Server LAMP disinstallato con successo.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Errore durante la disinstallazione del Server LAMP: {e}")
            messagebox.showerror("Errore", f"Errore durante la disinstallazione del Server LAMP: {e}")

    # Avvia l'esecuzione dei comandi in un thread separato
    thread = threading.Thread(target=run_uninstall_commands)
    thread.start()

def change_theme(theme):
    style.theme_use(theme)

# Codice GUI
root = tk.Tk()
root.title('CMS LAMP STACK')

style = ThemedStyle(root)
style.set_theme('winxpblue')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='LAMP SERVER')
tab_control.add(tab3, text='UNINSTALL')
tab_control.pack(expand=1, fill="both")

# Crea widget per l'interfaccia utente
user_label = tk.Label(tab1, text="Username:")
user_label.pack(pady=(10, 0))
user_entry = tk.Entry(tab1)
user_entry.pack()

password_label = tk.Label(tab1, text="Password:")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(tab1, show="*")
password_entry.pack()

lamp_server_button = ttk.Button(tab1, text="INSTALL LAMP SERVER", command=lamp_server)
lamp_server_button.pack(padx=10, pady=5)

kube_apps_button = ttk.Button(tab1, text="START XAMPP PROJECT", command=xampp)
kube_apps_button.pack(padx=10, pady=5)

lamp_server_uninstall = ttk.Button(tab3, text="UNINSTALL LAMP SERVER", command=uninstall)
lamp_server_uninstall.pack(padx=10, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

root.geometry("400x400")
root.mainloop()
