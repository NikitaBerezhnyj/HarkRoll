# Імпорт бібліотек
import os
import sys
import time
import random
import threading
import webbrowser
import tkinter as tk
from tkinter import messagebox
# Імпорт власних файлів
from file_utils import File_Utils
from gui_utils import GUI_Utils
from config import MIN_FOLDER_NUMBER, MAX_FOLDER_NUMBER, FILE_CREATION_CHANCE, MIN_RICKROLL_INTERVAL, MAX_RICKROLL_INTERVAL, RICKROLL_PAUSE, MIN_RICKROLL_CYCLE, MAX_RICKROLL_CYCLE

class Virus:
    def __init__(self):
        # Створення об'єктів класів File_Utils та GUI_Utils
        self.file_utils = File_Utils()
        self.gui_utils = GUI_Utils()

    def start(self):
        # Запуск засмічення файлової системи в окремому потоці
        base_dir = os.path.expanduser("~")  # Приклад шляху до домашньої директорії користувача
        threading.Thread(target=self.file_utils.create_folders_and_files, args=(base_dir,), daemon=True).start()

        # Запуск старту вірусу
        threading.Thread(target=self.gui_utils.show_start_message, daemon=True).start()
        threading.Thread(target=self.gui_utils.create_random_windows, daemon=True).start()

        # Запуск GUI атак у окремих потоках
        functions = [
            self.gui_utils.show_stop_prompt, self.gui_utils.show_like_prompt, self.gui_utils.get_random_file_path, 
            self.gui_utils.show_broken_text, self.gui_utils.show_random_jokes, self.gui_utils.show_random_facts, 
            self.gui_utils.display_infinite_popups, self.gui_utils.create_moving_window, 
            self.gui_utils.create_random_background_color_window, self.gui_utils.create_random_windows
        ]
        
        def run_gui_utils():
            while True:
                func = random.choice(functions)
                threading.Thread(target=func).start()
                time.sleep(random.randint(5, 10))  # Випадковий інтервал між запуском функцій

        # Запуск потоку з "вірусною" симуляцією
        threading.Thread(target=run_gui_utils, daemon=True).start()

        # Основний потік просто спить, щоб програма не завершувалася
        while True:
            time.sleep(1)

    def generate_report(self):
        report_content = f'''
        Virus report:
        Folders created: {self.file_utils.folder_counter}
        Files created: {self.file_utils.file_counter}
        Windows are open: {self.gui_utils.windows_counter}
        Rickrolls played: {self.gui_utils.rickroll_counter}
        __________________________
        Have a fun evening :)
        '''
        report_file_path = os.path.join(os.path.expanduser("~"), "virus_report.txt")
        try:
            with open(report_file_path, 'w') as report_file:
                report_file.write(report_content)
            print(f"Report generated at {report_file_path}")
        except Exception as e:
            print(f"Error writing report: {e}")
