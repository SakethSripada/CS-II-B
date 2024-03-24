import tkinter as tk
from tkinter import ttk
import psutil
import GPUtil as Gpu


class PCMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PC Monitoring")

        frame_width = 400
        frame_height = 200

        self.cpu_usage_panel = self.create_panel(self.root, 1, 0, frame_width, frame_height)
        self.gpu_usage_panel = self.create_panel(self.root, 1, 1, frame_width, frame_height)
        self.cpu_temp_panel = self.create_panel(self.root, 2, 0, frame_width, frame_height)
        self.gpu_temp_panel = self.create_panel(self.root, 2, 1, frame_width, frame_height)

        self.cpu_usage_label = ttk.Label(self.cpu_usage_panel, text="CPU Usage: N/A")
        self.cpu_usage_label.grid(row=0, column=0, padx=10, pady=10)

        self.cpu_temp_label = ttk.Label(self.cpu_temp_panel, text="CPU Temp: N/A")
        self.cpu_temp_label.grid(row=0, column=0, padx=10, pady=10)

        self.gpu_usage_label = ttk.Label(self.gpu_usage_panel, text="GPU Usage: N/A")
        self.gpu_usage_label.grid(row=0, column=0, padx=10, pady=10)

        self.gpu_temp_label = ttk.Label(self.gpu_temp_panel, text="GPU Temp: N/A")
        self.gpu_temp_label.grid(row=0, column=0, padx=10, pady=10)

        self.cpu_usage_progress = ttk.Progressbar(self.cpu_usage_panel, length=100, mode='determinate')
        self.cpu_usage_progress.grid(row=1, column=0, padx=10, pady=10)

        self.gpu_usage_progress = ttk.Progressbar(self.gpu_usage_panel, length=100, mode='determinate')
        self.gpu_usage_progress.grid(row=1, column=0, padx=10, pady=10)

        self.gpu_temp_progress = ttk.Progressbar(self.gpu_temp_panel, length=100, mode='determinate')
        self.gpu_temp_progress.grid(row=1, column=0, padx=10, pady=10)

        self.update_system_info()
        self.root.mainloop()

    @staticmethod
    def create_panel(parent, row, column, width, height):
        panel = ttk.Frame(parent, relief=tk.GROOVE, borderwidth=2, width=width, height=height)
        panel.grid(row=row, column=column, padx=10, pady=10, sticky=tk.NSEW)
        return panel

    def update_system_info(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_usage_label.config(text=f"CPU Usage: {cpu_percent}%")
        self.cpu_usage_progress['value'] = cpu_percent

        try:
            cpu_temp = self.get_cpu_temperature()
            self.cpu_temp_label.config(text=f"CPU Temp: {cpu_temp}°C" if cpu_temp else "CPU Temp: N/A")
        except Exception as e:
            self.cpu_temp_label.config(text="CPU Temp: N/A")
            print(f"Unable to fetch CPU temperature: {e}")

        gpus = Gpu.getGPUs()
        if gpus:
            gpu = gpus[0]
            gpu_percent = gpu.load * 100
            self.gpu_usage_label.config(text=f"GPU Usage: {gpu_percent:.2f}%")
            self.gpu_usage_progress['value'] = gpu_percent

            gpu_temp = gpu.temperature
            self.gpu_temp_label.config(text=f"GPU Temp: {gpu_temp}°C")
            self.gpu_temp_progress['value'] = gpu_temp
        else:
            self.gpu_usage_label.config(text="GPU Usage: N/A")
            self.gpu_usage_progress['value'] = 0
            self.gpu_temp_label.config(text="GPU Temp: N/A")
            self.gpu_temp_progress['value'] = 0

        self.root.after(1000, self.update_system_info)

    def get_cpu_temperature(self):
        try:
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                core_temps = temps['coretemp']
                return max(temp.current for temp in core_temps)
            return None
        except AttributeError:
            return None


PCMonitor()
