import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import threading
import getpass
import os


import subprocess

def kube_apps():
    # Definizione dei comandi
    kubernetes_installation = 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"'
    kubernetes_validation = 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"'
    validation = 'echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check'
    finishing = 'chmod +x kubectl; mkdir -p ~/.local/bin; mv ./kubectl ~/.local/bin/kubectl; kubectl version --client'
    helm = 'sudo helm repo add bitnami https://charts.bitnami.com/bitnami; sudo kubectl create namespace kubeapps; sudo helm install kubeapps --namespace kubeapps bitnami/kubeapps'
    kubernetes = 'sudo kubectl create --namespace default serviceaccount kubeapps-operator; kubectl create clusterrolebinding kubeapps-operator --clusterrole=cluster-admin --serviceaccount=default:kubeapps-operator'
    configuration = "sudo kubectl get --namespace default secret kubeapps-operator-token -o go-template='{{.data.token | base64decode}}'"
    starting = 'sudo kubectl port-forward -n kubeapps svc/kubeapps 8080:8080'

    try:
        # Esecuzione dei comandi con subprocess.run
        subprocess.run(kubernetes_installation, shell=True, check=True)
        subprocess.run(kubernetes_validation, shell=True, check=True)
        subprocess.run(validation, shell=True, check=True)
        subprocess.run(finishing, shell=True, check=True)
        subprocess.run(helm, shell=True, check=True)
        subprocess.run(kubernetes, shell=True, check=True)
        subprocess.run(configuration, shell=True, check=True)
        subprocess.run(starting, shell=True, check=True)
        
        messagebox.showinfo("Kubeapps installation and configuration completed successfully.")
    
    except subprocess.CalledProcessError as e:
        messagebox.showerror(f"Error occurred during execution: {e}")



def lamp_server():
    def run_commands():
        commands = [
            'sudo apt install  apache2',
            'sudo apt install  ghostscript',
            'sudo apt install  libapache2-mod-php',
            'sudo apt install  postgresql',
            'sudo apt install -y postgresql-common sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh'
            'sudo apt install curl ca-certificates sudo install -d /usr/share/postgresql-common/pgdg sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc sudo sh -c "echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list sudo apt update sudo apt -y install postgresql'
            'sudo apt install  php',
            'sudo apt install  php-curl',
            'sudo apt install  php-imagick',
            'sudo apt install  php-bcmath',
            'sudo apt install  php-intl',
            'sudo apt install  php-json',
            'sudo apt install  php-mbstring',
            'sudo apt install  php-mysql',
            'sudo apt install  php-xml',
            'sudo apt install  php-yaml',
            'sudo apt install  php-zip',
            
        ]
        

        
        progress_bar['maximum'] = len(commands)
        progress_bar['value'] = 0
        
        try:
            for command in commands:
                process = subprocess.run(command, shell=True, check=True, text=True)
                print(process.stdout)  # Output di `subprocess.run`
                print(process.stderr)
                progress_bar['value'] += 1
                root.update_idletasks()  # Aggiorna l'interfaccia grafica
            messagebox.showinfo('Success', 'LAMP Server installed successfully!')
        except subprocess.CalledProcessError as e:
            messagebox.showerror('Error', f'Failed to install LAMP Server: {e}')
        
        finally:
            progress_bar.stop()

    # Esegui i comandi in un thread separato
    thread = threading.Thread(target=run_commands)
    thread.start()

def uninstall():
    def run_uninstall_commands():
        commands = [
            'sudo apt autoremove  apache2',
            'sudo apt autoremove  ghostscript',
            'sudo apt autoremove  libapache2-mod-php',
            'sudo apt autoremove  phpmyadmin',
            'sudo apt autoremove  php',
            'sudo apt autoremove  php-curl',
            'sudo apt autoremove  php-imagick',
            'sudo apt autoremove  php-bcmath',
            'sudo apt autoremove  php-intl',
            'sudo apt autoremove  php-json',
            'sudo apt autoremove  php-mbstring',
            'sudo apt autoremove  php-mysql',
            'sudo apt autoremove  php-xml',
            'sudo apt autoremove  php-yaml',
            'sudo apt autoremove  php-zip'
        ]
        
        
        
        progress_bar['maximum'] = len(commands)
        progress_bar['value'] = 0
        
        try:
            for command in commands:
                process = subprocess.run(command, shell=True, check=True, text=True)
                print(process.stdout)  # Output di `subprocess.run`
                print(process.stderr)
                progress_bar['value'] += 1
                root.update_idletasks()  # Aggiorna l'interfaccia grafica
            messagebox.showinfo('Success', 'LAMP Server uninstalled successfully!')
        except subprocess.CalledProcessError as e:
            messagebox.showerror('Error', f'Failed to uninstall LAMP Server: {e}')
        
        finally:
            progress_bar.stop()

    # Esegui i comandi in un thread separato
    thread = threading.Thread(target=run_uninstall_commands)
    thread.start()

def change_theme(theme):
    style.theme_use(theme)

# GUI code
root = tk.Tk()
root.title('CMS  LAMP STACK')

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

user_label = tk.Label(tab1, text="Username:")
user_label.pack(pady=(10, 0))
user_entry = tk.Entry(tab1)
user_entry.pack()

password_label = tk.Label(tab1, text="Password:")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(tab1, show="*")
password_entry.pack()

lamp_server_uninstall = ttk.Button(tab1, text="START KUBE APPS PROJECT", command=kube_apps)
lamp_server_uninstall.pack(padx=10, pady=5)

lamp_server_button = ttk.Button(tab1, text="INSTALL LAMP SERVER", command=lamp_server)
lamp_server_button.pack(padx=10, pady=5)

lamp_server_uninstall = ttk.Button(tab3, text="UNINSTALL LAMP SERVER", command=uninstall)
lamp_server_uninstall.pack(padx=10, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

root.geometry("400x400")
root.mainloop()
