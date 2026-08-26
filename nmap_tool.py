import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess


def scan_target():
    target = target_entry.get().strip()

    if not target:
        messagebox.showwarning("Warning", "Please enter an IP address.")
        return

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Scanning... Please wait.\n\n")
    window.update()

    try:
        result = subprocess.run(
            ["nmap", "-sV", target],
            capture_output=True,
            text=True,
            timeout=120
        )

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result.stdout)
        status_label.config(text="Status: Scan completed successfully")
        if result.returncode != 0:
            output_box.insert(tk.END, "\n\nError:\n" + result.stderr)

    except subprocess.TimeoutExpired:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Scan timed out.")

    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")


window = tk.Tk()
window.title("Nmap Recon Tool")
window.geometry("800x600")

title = tk.Label(
    window,
    text="NMAP RECON TOOL",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

target_label = tk.Label(
    window,
    text="Target IP Address:"
)
target_label.pack()

target_entry = tk.Entry(
    window,
    width=40,
    font=("Arial", 12)
)
target_entry.pack(pady=8)

target_entry.insert(0, "192.168.56.10")

scan_button = tk.Button(
    window,
    text="START SCAN",
    command=scan_target,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8
)
scan_button.pack(pady=10)

status_label = tk.Label(
    window,
    text="Status: Ready",
    font=("Arial", 10)
)
status_label.pack(pady=5)

output_box = scrolledtext.ScrolledText(
    window,
    width=90,
    height=25,
    font=("Courier", 10)
)
output_box.pack(padx=10, pady=10, fill="both", expand=True)
clear_button = tk.Button(
    window,
    text="CLEAR",
    command=lambda: output_box.delete("1.0", tk.END),
    font=("Arial", 10),
    padx=15,
    pady=5
)
clear_button.pack(pady=5)
window.mainloop()


