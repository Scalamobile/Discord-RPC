# pip install pypresence
import tkinter as tk
from tkinter import messagebox, ttk
from pypresence import Presence
import time
import threading
from datetime import datetime
import json
import os

rpc = None
running = False
presence_data = {}
profile_file = "rpc_profiles.json"

# Load profiles if they exist
if os.path.exists(profile_file):
    with open(profile_file, "r") as f:
        profiles = json.load(f)
else:
    profiles = {}

def save_profiles():
    with open(profile_file, "w") as f:
        json.dump(profiles, f, indent=4)

def parse_timestamp(value):
    if not value.strip():
        return int(time.time())
    try:
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return int(dt.timestamp())
    except ValueError:
        try:
            return int(value)
        except ValueError:
            messagebox.showwarning("Warning", "Invalid timestamp, using current time instead.")
            return int(time.time())

def update_timer_label():
    if running:
        elapsed = int(time.time() - presence_data.get("start", time.time()))
        minutes, seconds = divmod(elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        label_timer.config(text=f"Elapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer_label)

def start_presence():
    global rpc, running, presence_data

    def connect_and_start():
        client_id = entry_client_id.get().strip()
        if not client_id:
            messagebox.showerror("Error", "You must enter the Client ID!")
            return

        try:
            rpc_local = Presence(client_id)
            rpc_local.connect()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to connect to Discord:\n{e}")
            return

        # Read data from GUI
        details = entry_details.get()
        state = entry_state.get()
        large_img = combo_large.get()
        small_img = combo_small.get()
        btn1_label = entry_btn1_label.get()
        btn1_url = entry_btn1_url.get()
        btn2_label = entry_btn2_label.get()
        btn2_url = entry_btn2_url.get()
        start_time = parse_timestamp(entry_start.get())

        # Prepare presence_data
        presence_data_local = {
            "details": details if details else None,
            "state": state if state else None,
            "start": start_time,
            "large_image": large_img if large_img else None,
            "small_image": small_img if small_img else None,
        }

        buttons = []
        if btn1_label and btn1_url:
            buttons.append({"label": btn1_label, "url": btn1_url})
        if btn2_label and btn2_url:
            buttons.append({"label": btn2_label, "url": btn2_url})
        if buttons:
            presence_data_local["buttons"] = buttons

        try:
            rpc_local.update(**presence_data_local)
        except Exception as e:
            messagebox.showerror("Error", f"Update failed:\n{e}")
            return

        # Update globals safely
        global rpc, presence_data, running
        rpc = rpc_local
        presence_data = presence_data_local
        running = True
        threading.Thread(target=keep_alive, daemon=True).start()
        root.after(0, update_timer_label)
        messagebox.showinfo("Started", "Rich Presence activated!")

    # Avvia solo il thread
    threading.Thread(target=connect_and_start, daemon=True).start()

    global rpc, running, presence_data

    def connect_and_start():
        client_id = entry_client_id.get().strip()
        if not client_id:
            messagebox.showerror("Error", "You must enter the Client ID!")
            return

        try:
            rpc_local = Presence(client_id)
            rpc_local.connect()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to connect to Discord:\n{e}")
            return

        # Read data from GUI
        details = entry_details.get()
        state = entry_state.get()
        large_img = combo_large.get()
        small_img = combo_small.get()
        btn1_label = entry_btn1_label.get()
        btn1_url = entry_btn1_url.get()
        btn2_label = entry_btn2_label.get()
        btn2_url = entry_btn2_url.get()
        start_time = parse_timestamp(entry_start.get())

        # Prepare presence_data
        presence_data_local = {
            "details": details if details else None,
            "state": state if state else None,
            "start": start_time,
            "large_image": large_img if large_img else None,
            "small_image": small_img if small_img else None,
        }

        buttons = []
        if btn1_label and btn1_url:
            buttons.append({"label": btn1_label, "url": btn1_url})
        if btn2_label and btn2_url:
            buttons.append({"label": btn2_label, "url": btn2_url})
        if buttons:
            presence_data_local["buttons"] = buttons

        try:
            rpc_local.update(**presence_data_local)
        except Exception as e:
            messagebox.showerror("Error", f"Update failed:\n{e}")
            return

        # Update global variables
        global rpc, presence_data, running
        rpc = rpc_local
        presence_data = presence_data_local
        running = True
        threading.Thread(target=keep_alive, daemon=True).start()
        root.after(0, update_timer_label)
        messagebox.showinfo("Started", "Rich Presence activated!")

    # Run everything in a separate thread
    threading.Thread(target=connect_and_start, daemon=True).start()

    global rpc, running, presence_data
    client_id = entry_client_id.get().strip()
    if not client_id:
        messagebox.showerror("Error", "You must enter the Client ID!")
        return

    try:
        rpc = Presence(client_id)
        rpc.connect()
    except Exception as e:
        messagebox.showerror("Error", f"Unable to connect to Discord:\n{e}")
        return

    details = entry_details.get()
    state = entry_state.get()
    large_img = combo_large.get()
    small_img = combo_small.get()
    btn1_label = entry_btn1_label.get()
    btn1_url = entry_btn1_url.get()
    btn2_label = entry_btn2_label.get()
    btn2_url = entry_btn2_url.get()
    start_time = parse_timestamp(entry_start.get())

    presence_data = {
        "details": details if details else None,
        "state": state if state else None,
        "start": start_time,
        "large_image": large_img if large_img else None,
        "small_image": small_img if small_img else None,
    }

    buttons = []
    if btn1_label and btn1_url:
        buttons.append({"label": btn1_label, "url": btn1_url})
    if btn2_label and btn2_url:
        buttons.append({"label": btn2_label, "url": btn2_url})
    if buttons:
        presence_data["buttons"] = buttons

    try:
        rpc.update(**presence_data)
    except Exception as e:
        messagebox.showerror("Error", f"Update failed:\n{e}")
        return

    running = True
    threading.Thread(target=keep_alive, daemon=True).start()
    update_timer_label()
    messagebox.showinfo("Started", "Rich Presence activated!")

def keep_alive():
    global presence_data
    while running and rpc:
        try:
            rpc.update(**presence_data)  # metodo sincrono
        except Exception as e:
            print(f"Errore keep_alive: {e}")
            break
        time.sleep(15)

def stop_presence():
    global running, rpc
    running = False
    try:
        if rpc:
            rpc.clear()
    except:
        pass
    label_timer.config(text="Elapsed time: 00:00:00")
    messagebox.showinfo("Stopped", "Rich Presence deactivated.")

def save_profile():
    name = entry_profile_name.get().strip()
    if not name:
        messagebox.showwarning("Warning", "Enter a name for the profile")
        return
    profiles[name] = {
        "client_id": entry_client_id.get(),
        "details": entry_details.get(),
        "state": entry_state.get(),
        "large_image": combo_large.get(),
        "small_image": combo_small.get(),
        "btn1_label": entry_btn1_label.get(),
        "btn1_url": entry_btn1_url.get(),
        "btn2_label": entry_btn2_label.get(),
        "btn2_url": entry_btn2_url.get(),
        "start": entry_start.get()
    }
    save_profiles()
    combo_profiles['values'] = list(profiles.keys())
    messagebox.showinfo("Saved", f"Profile '{name}' saved!")

def load_profile(event=None):
    name = combo_profiles.get()
    if name not in profiles:
        return
    profile = profiles[name]
    entry_client_id.delete(0, tk.END)
    entry_client_id.insert(0, profile.get("client_id",""))
    entry_details.delete(0, tk.END)
    entry_details.insert(0, profile.get("details",""))
    entry_state.delete(0, tk.END)
    entry_state.insert(0, profile.get("state",""))
    combo_large.set(profile.get("large_image",""))
    combo_small.set(profile.get("small_image",""))
    entry_btn1_label.delete(0, tk.END)
    entry_btn1_label.insert(0, profile.get("btn1_label",""))
    entry_btn1_url.delete(0, tk.END)
    entry_btn1_url.insert(0, profile.get("btn1_url",""))
    entry_btn2_label.delete(0, tk.END)
    entry_btn2_label.insert(0, profile.get("btn2_label",""))
    entry_btn2_url.delete(0, tk.END)
    entry_btn2_url.insert(0, profile.get("btn2_url",""))
    entry_start.delete(0, tk.END)
    entry_start.insert(0, profile.get("start",""))

# === GUI ===
root = tk.Tk()
root.title("Advanced Discord RPC GUI")

# Profile
tk.Label(root, text="Profile:").grid(row=0, column=0, sticky="w")
combo_profiles = ttk.Combobox(root, values=list(profiles.keys()), state="readonly")
combo_profiles.grid(row=0, column=1)
combo_profiles.bind("<<ComboboxSelected>>", load_profile)

entry_profile_name = tk.Entry(root, width=20)
entry_profile_name.grid(row=0, column=2)
btn_save_profile = tk.Button(root, text="Save profile", command=save_profile)
btn_save_profile.grid(row=0, column=3)

# Client ID
tk.Label(root, text="Client ID:").grid(row=1, column=0, sticky="w")
entry_client_id = tk.Entry(root, width=40)
entry_client_id.grid(row=1, column=1)

# Details
tk.Label(root, text="Details:").grid(row=2, column=0, sticky="w")
entry_details = tk.Entry(root, width=40)
entry_details.grid(row=2, column=1)

# State
tk.Label(root, text="State:").grid(row=3, column=0, sticky="w")
entry_state = tk.Entry(root, width=40)
entry_state.grid(row=3, column=1)

# Large Image Key
tk.Label(root, text="Large Image Key:").grid(row=4, column=0, sticky="w")
combo_large = ttk.Combobox(root, values=["big_logo", "logo2", "alt_image"])  # replace with your assets
combo_large.grid(row=4, column=1)

# Small Image Key
tk.Label(root, text="Small Image Key:").grid(row=5, column=0, sticky="w")
combo_small = ttk.Combobox(root, values=["small_logo", "icon2"])  # replace with your assets
combo_small.grid(row=5, column=1)

# Start Timestamp
tk.Label(root, text="Start Time (YYYY-MM-DD HH:MM:SS or UNIX):").grid(row=6, column=0, sticky="w")
entry_start = tk.Entry(root, width=40)
entry_start.grid(row=6, column=1)

# Button 1
tk.Label(root, text="Button 1 Label:").grid(row=7, column=0, sticky="w")
entry_btn1_label = tk.Entry(root, width=40)
entry_btn1_label.grid(row=7, column=1)
tk.Label(root, text="Button 1 URL:").grid(row=8, column=0, sticky="w")
entry_btn1_url = tk.Entry(root, width=40)
entry_btn1_url.grid(row=8, column=1)

# Button 2
tk.Label(root, text="Button 2 Label:").grid(row=9, column=0, sticky="w")
entry_btn2_label = tk.Entry(root, width=40)
entry_btn2_label.grid(row=9, column=1)
tk.Label(root, text="Button 2 URL:").grid(row=10, column=0, sticky="w")
entry_btn2_url = tk.Entry(root, width=40)
entry_btn2_url.grid(row=10, column=1)

# Live Timer
label_timer = tk.Label(root, text="Elapsed time: 00:00:00", font=("Arial", 12))
label_timer.grid(row=11, column=0, columnspan=2)

# Start/Stop Buttons
btn_start = tk.Button(root, text="Start RPC", command=start_presence)
btn_start.grid(row=12, column=0, pady=10)
btn_stop = tk.Button(root, text="Stop RPC", command=stop_presence)
btn_stop.grid(row=12, column=1, pady=10)

root.mainloop()
