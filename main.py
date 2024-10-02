# Імпорт бібліотек
import os
# Імпорт власних файлів
from virus import Virus

if __name__ == "__main__":
    try:
        virus = Virus()
        virus.start()
    except KeyboardInterrupt:
        virus.generate_report()
