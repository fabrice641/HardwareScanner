import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import os
import sys


def lamp_server():
    username = user_entry.get()
    password = password_entry.get()

    server = [
        f'echo {password} | sudo -S apt install apache2',
        f'echo {password} | sudo -S apt install ghostscript',
        f'echo {password} | sudo -S apt install libapache2-mod-php',
        f'echo {password} | sudo -S apt install phpmyadmin',
        f'echo {password} | sudo -S apt install php',
        f'echo {password} | sudo -S apt install php-curl',
        f'echo {password} | sudo -S apt install php-imagick',
        f'echo {password} | sudo -S apt install php-bcmath',
        f'echo {password} | sudo -S apt install php-intl',
        f'echo {password} | sudo -S apt install php-json',
        f'echo {password} | sudo -S apt install php-mbstring',
        f'echo {password} | sudo -S apt install php-mysql',
        f'echo {password} | sudo -S apt install php-xml',
        f'echo {password} | sudo -S apt install php-yaml',
        f'echo {password} | sudo -S apt install php-zip'
    ]
    
    progress_bar['maximum'] = len(server)
    progress_bar['value'] = 0
    
    try:
        for command in server:
            subprocess.run(command, shell=True, check=True)
            progress_bar['value'] += 1
            root.update_idletasks()  # Aggiorna l'interfaccia grafica
        messagebox.showinfo('Success', 'LAMP Server installed successfully!')
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Error', f'Failed to install LAMP Server: {e}')

def uninstall():
    username = user_entry.get()
    password = password_entry.get()

    uninstall_commands = [
        f'echo {password} | sudo -S apt autoremove -y apache2',
        f'echo {password} | sudo -S apt autoremove -y ghostscript',
        f'echo {password} | sudo -S apt autoremove -y libapache2-mod-php',
        f'echo {password} | sudo -S apt autoremove -y phpmyadmin',
        f'echo {password} | sudo -S apt autoremove -y php',
        f'echo {password} | sudo -S apt autoremove -y php-curl',
        f'echo {password} | sudo -S apt autoremove -y php-imagick',
        f'echo {password} | sudo -S apt autoremove -y php-bcmath',
        f'echo {password} | sudo -S apt autoremove -y php-intl',
        f'echo {password} | sudo -S apt autoremove -y php-json',
        f'echo {password} | sudo -S apt autoremove -y php-mbstring',
        f'echo {password} | sudo -S apt autoremove -y php-mysql',
        f'echo {password} | sudo -S apt autoremove -y php-xml',
        f'echo {password} | sudo -S apt autoremove -y php-yaml',
        f'echo {password} | sudo -S apt autoremove -y php-zip'
    ]
    
    progress_bar['maximum'] = len(uninstall_commands)
    progress_bar['value'] = 0
    
    try:
        for command in uninstall_commands:
            subprocess.run(command, shell=True, check=True)
            progress_bar['value'] += 1
            root.update_idletasks()  # Aggiorna l'interfaccia grafica
        messagebox.showinfo('Success', 'LAMP Server uninstalled successfully!')
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Error', f'Failed to uninstall LAMP Server: {e}')

def change_theme(theme):
    style.theme_use(theme)

# Redirect stdout and stderr to a log file
log_file = open("output_log.txt", "w")
sys.stdout = log_file
sys.stderr = log_file

# GUI code
root = tk.Tk()
root.title('CMS  LAMP STACK')

style = ThemedStyle(root)
style.set_theme('yaru')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='LAMP SERVER')
tab_control.add(tab3, text='UNINSTALL')
tab_control.pack(expand=1, fill="both")

user_label = tk.Label(tab1, text="Username:")
user_label.pack(pady=(10, 0))
user_entry = tk.Entry(tab1)
user_entry.pack()

password_label = tk.Label(tab1, text="Password:")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(tab1, show="*")
password_entry.pack()

lamp_server_button = ttk.Button(tab1, text="START LAMP SERVER", command=lamp_server)
lamp_server_button.pack(padx=10, pady=5)

lamp_server_uninstall = ttk.Button(tab3, text="UNINSTALL LAMP SERVER", command=uninstall)
lamp_server_uninstall.pack(padx=10, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

root.geometry("400x400")
root.mainloop()

# Restore stdout and stderr
sys.stdout.close()
sys.stderr.close()
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
