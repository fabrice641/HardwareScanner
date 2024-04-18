import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from sudo import run_as_sudo
import os
import sys






def lamp_server(dialog):
    server = [
        ['sudo', 'apt', 'install', 'apache2'],
        ['sudo', 'apt', 'install', 'ghostscript'],
        ['sudo', 'apt', 'install', 'libapache2-mod-php'],
        ['sudo', 'apt', 'install', 'phpmyadmin'],
        ['sudo', 'apt', 'install', 'php'],
        ['sudo', 'apt', 'install', 'php-curl'],
        ['sudo', 'apt', 'install', 'php-imagick'],
        ['sudo', 'apt', 'install', 'php-bcmath'],
        ['sudo', 'apt', 'install', 'php-intl'],
        ['sudo', 'apt', 'install', 'php-json'],
        ['sudo', 'apt', 'install', 'php-mbstring'],
        ['sudo', 'apt', 'install', 'php-mysql'],
        ['sudo', 'apt', 'install', 'php-xml'],
        ['sudo', 'apt', 'install', 'php-yaml'],
        ['sudo', 'apt', 'install', 'php-zip']
    ]
    
    progress_bar['maximum'] = len(server)
    progress_bar['value'] = 0
    
    try:
        for commands in server:
            subprocess.run(commands, check=True)
            progress_bar['value'] += 1
            root.update_idletasks()  # Aggiorna l'interfaccia grafica
        messagebox.showinfo('Success', 'LAMP Server installed successfully!')
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Error', f'Failed to install LAMP Server: {e}')

def uninstall(dialog):
    uninstall_commands = [
        ['sudo', 'apt', 'autoremove', '-y', 'apache2'],
        ['sudo', 'apt', 'autoremove', '-y', 'ghostscript'],
        ['sudo', 'apt', 'autoremove', '-y', 'libapache2-mod-php'],
        ['sudo', 'apt', 'autoremove', '-y', 'phpmyadmin'],
        ['sudo', 'apt', 'autoremove', '-y', 'php'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-curl'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-imagick'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-bcmath'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-intl'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-json'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-mbstring'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-mysql'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-xml'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-yaml'],
        ['sudo', 'apt', 'autoremove', '-y', 'php-zip']
    ]
    
    progress_bar['maximum'] = len(uninstall_commands)
    progress_bar['value'] = 0
    
    try:
        for command in uninstall_commands:
            subprocess.run(command, check=True)
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

lamp_server_button = ttk.Button(tab1, text="START LAMP SERVER", command=lamp_server)
lamp_server_button.pack(padx=10, pady=5)

lamp_server_uninstall = ttk.Button(tab3, text="UNINSTALL LAMP SERVER", command=uninstall)
lamp_server_uninstall.pack(padx=10, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

root.geometry("400x450")
root.mainloop()




# Restore stdout and stderr
sys.stdout.close()
sys.stderr.close()
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__


def dialog(login):
    tk.messagebox('You will next a new frame? ')


try:
    def login(cmd, sudo_user, root, access, user):
        cmd = password.get()
        sudo_user = user.get()
        run_as_sudo(sudo_user, cmd, shell=True, timeout=20)
        root = tk.Tk()
        password = tk.Entry(root)
        password.pack()
        user = tk.Entry(root)
        user.pack()

        access = tk.Button(root, text="SUDO PERMISSION", command=dialog)
        access.pack()

        root.geometry('600x600')
        root.mainloop()
        
        
except:
    root.destroy()

