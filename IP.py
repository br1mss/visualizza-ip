import socket
import requests
import tkinter as tk
import psutil
from tkinter import font


def get_local_ip():
    """Ottiene l'indirizzo IP locale escludendo le interfacce virtuali."""
    try:
        # Ottieni tutte le interfacce di rete attive
        for interface, addrs in psutil.net_if_addrs().items():
            # Escludi le interfacce virtuali tipiche (VirtualBox, VPN, Docker, etc.)
            if 'veth' not in interface and 'docker' not in interface and 'VirtualBox' not in interface:
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        # Se l'indirizzo non appartiene alla rete virtuale, restituiscilo
                        if '192.168.56' not in addr.address:  # Ignora gli indirizzi della rete virtuale
                            return addr.address
        return "Impossibile ottenere l'IP locale"
    except Exception as e:
        return f"Errore: {e}"

def get_public_ip():
    """Ottiene l'indirizzo IP pubblico."""
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        response.raise_for_status()  # Solleva un'eccezione per errori HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Impossibile ottenere l'IP pubblico: {e}"

def show_ips():
    """Crea e visualizza la finestra con gli indirizzi IP."""
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    window = tk.Tk()
    window.title("I Tuoi Indirizzi IP")

    # Imposta le dimensioni della finestra
    window_width = 400
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.resizable(False, False)  # Rende la finestra non ridimensionabile

    # Definisci un font più grande e visivamente gradevole
    ip_font = font.Font(family="Helvetica", size=16, weight="bold")

    local_label = tk.Label(window, text=f"IP Locale:", font=ip_font)
    local_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")

    local_ip_value = tk.Label(window, text=local_ip, font=ip_font)
    local_ip_value.grid(row=0, column=1, padx=20, pady=15, sticky="e")

    public_label = tk.Label(window, text=f"IP Pubblico:", font=ip_font)
    public_label.grid(row=1, column=0, padx=20, pady=15, sticky="w")

    public_ip_value = tk.Label(window, text=public_ip, font=ip_font)
    public_ip_value.grid(row=1, column=1, padx=20, pady=15, sticky="e")

    ok_button = tk.Button(window, text="OK", command=window.destroy, padx=20, pady=10)
    ok_button.grid(row=2, column=0, columnspan=2, pady=15)

    window.grid_columnconfigure(0, weight=1)  # Permette al testo a sinistra di allinearsi
    window.grid_columnconfigure(1, weight=1)  # Permette al valore a destra di allinearsi

    window.mainloop()

if __name__ == "__main__":
    show_ips()
