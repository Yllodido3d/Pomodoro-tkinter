import tkinter as tk
from tkinter import messagebox
import time
import threading

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Visual")
        self.root.geometry("450x500")
        self.root.configure(bg="#f5f0e1")

        self.mode = tk.StringVar(value="convencional")
        self.running = False
        self.paused = False
        self.time_left = 0
        self.total_focus_time = 0
        self.is_break = False
        self.focus_time = 25*60
        self.break_time = 5*60

        # Frame para modo
        mode_frame = tk.Frame(root, bg="#f5f0e1")
        mode_frame.pack(pady=10)
        tk.Label(mode_frame, text="Modo:", bg="#f5f0e1", font=("Helvetica", 14, "bold")).pack(anchor="w")
        tk.Radiobutton(mode_frame, text="Convencional (customizável)", variable=self.mode, value="convencional", bg="#f5f0e1", font=("Helvetica", 12)).pack(anchor="w", padx=20)
        tk.Radiobutton(mode_frame, text="Foco (contínuo até parar)", variable=self.mode, value="foco", bg="#f5f0e1", font=("Helvetica", 12)).pack(anchor="w", padx=20)

        # Frame para entradas
        time_frame = tk.Frame(root, bg="#f5f0e1")
        time_frame.pack(pady=10)
        tk.Label(time_frame, text="Tempo de Foco (min):", bg="#f5f0e1", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.focus_time_entry = tk.Entry(time_frame, width=5, justify="center", font=("Helvetica", 12))
        self.focus_time_entry.insert(0, "25")
        self.focus_time_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(time_frame, text="Tempo de Descanso (min):", bg="#f5f0e1", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.break_time_entry = tk.Entry(time_frame, width=5, justify="center", font=("Helvetica", 12))
        self.break_time_entry.insert(0, "5")
        self.break_time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Canvas para barra circular
        self.canvas = tk.Canvas(root, width=220, height=220, bg="#f5f0e1", highlightthickness=0)
        self.canvas.pack(pady=15)
        self.arc = self.canvas.create_arc(10, 10, 210, 210, start=90, extent=0, width=20, outline="#7fb77e", style="arc")

        # Label do tempo
        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 32, "bold"), bg="#f5f0e1", fg="#333333")
        self.time_label.place(x=165, y=180)

        # Frame para botões
        button_frame = tk.Frame(root, bg="#f5f0e1")
        button_frame.pack(pady=10)
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, bg="#7fb77e", fg="white", width=14, bd=0, font=("Helvetica", 12, "bold"), activebackground="#95c695")
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.toggle_pause, bg="#f0ad4e", fg="white", width=14, bd=0, font=("Helvetica", 12, "bold"), state="disabled", activebackground="#f2c16d")
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_timer, bg="#e57373", fg="white", width=14, bd=0, font=("Helvetica", 12, "bold"), state="disabled", activebackground="#f28b8b")
        self.stop_button.grid(row=0, column=2, padx=5, pady=5)

        # Hover
        self.start_button.bind("<Enter>", lambda e: self.start_button.config(bg="#95c695"))
        self.start_button.bind("<Leave>", lambda e: self.start_button.config(bg="#7fb77e"))
        self.pause_button.bind("<Enter>", lambda e: self.pause_button.config(bg="#f2c16d"))
        self.pause_button.bind("<Leave>", lambda e: self.pause_button.config(bg="#f0ad4e"))
        self.stop_button.bind("<Enter>", lambda e: self.stop_button.config(bg="#f28b8b"))
        self.stop_button.bind("<Leave>", lambda e: self.stop_button.config(bg="#e57373"))

    # --------- Funções de timer ----------
    def start_timer(self):
        if self.running:
            return
        self.running = True
        self.paused = False
        self.start_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.stop_button.config(state="normal")

        if self.mode.get() == "convencional":
            try:
                focus_minutes = int(self.focus_time_entry.get())
                break_minutes = int(self.break_time_entry.get())
                if focus_minutes <= 0 or break_minutes <= 0:
                    raise ValueError
                self.focus_time = focus_minutes * 60
                self.break_time = break_minutes * 60
                self.time_left = self.focus_time
                self.is_break = False
                threading.Thread(target=self.run_conventional).start()
            except ValueError:
                messagebox.showerror("Erro!", "Digite tempos válidos (números inteiros positivos).")
                self.running = False
                self.start_button.config(state="normal")
                self.pause_button.config(state="disabled")
                self.stop_button.config(state="disabled")
        elif self.mode.get() == "foco":
            self.time_left = 0
            self.total_focus_time = 0
            threading.Thread(target=self.run_focus).start()

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_button.config(text="Continue" if self.paused else "Pause")

    def stop_timer(self):
        self.running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        self.stop_button.config(state="disabled")
        if self.mode.get() == "foco":
            messagebox.showinfo("Foco Parado", f"Tempo total focado: {self.format_time(self.total_focus_time)}")

    def run_conventional(self):
        while self.running:
            if not self.paused:
                if self.time_left > 0:
                    self.time_left -= 1
                    self.update_ui(self.time_left, self.focus_time if not self.is_break else self.break_time)
                    time.sleep(1)
                else:
                    if not self.is_break:
                        messagebox.showinfo("Tempo Acabou!", f"Hora do descanso! {self.break_time // 60} minutos.")
                        self.time_left = self.break_time
                        self.is_break = True
                    else:
                        messagebox.showinfo("Descanso Acabou!", "Volte ao trabalho!")
                        self.time_left = self.focus_time
                        self.is_break = False
            else:
                time.sleep(0.1)

    def run_focus(self):
        while self.running:
            if not self.paused:
                self.total_focus_time += 1
                self.update_ui(self.total_focus_time, self.total_focus_time+1)
                time.sleep(1)
            else:
                time.sleep(0.1)

    def update_ui(self, current, total):
        self.time_label.config(text=self.format_time(current))
        extent = 360 * (current / total)
        self.canvas.itemconfig(self.arc, extent=-extent)

        # Cor de fundo suave
        target_bg = "#dce6f0" if self.is_break else "#f5f0e1"
        target_arc = "#6fa8dc" if self.is_break else "#7fb77e"
        self.root.configure(bg=target_bg)
        self.time_label.config(bg=target_bg)
        self.canvas.configure(bg=target_bg)
        self.canvas.itemconfig(self.arc, outline=target_arc)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
