import sys
import os
import ctypes
from ctypes import wintypes
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import random
from download import main, read_config
import json
from style import get_style


download_path = "C:/downloader/"
config_dir = os.path.join(download_path, 'config')
config_file = os.path.join(config_dir, 'config.json')

default_config = {"download_path": "C:/downloader/", "quality": "bestvideo+bestaudio/best"}

# Создание нужных папок, если они не существуют
os.makedirs(config_dir, exist_ok=True)

# Создание config.json, если его нет
if not os.path.exists(config_file):
    with open(config_file, 'w') as f:
        json.dump(default_config, f, indent=4)


# --- Структуры для блюра ---
class ACCENT_POLICY(ctypes.Structure):
    _fields_ = [("AccentState", ctypes.c_int), ("AccentFlags", ctypes.c_int), ("GradientColor", ctypes.c_int), ("AnimationId", ctypes.c_int),]


class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
    _fields_ = [("Attribute", ctypes.c_int), ("Data", ctypes.c_void_p), ("SizeOfData", ctypes.c_size_t),]


def enable_blur(hwnd):
    accent = ACCENT_POLICY()
    accent.AccentState = 3  # ACCENT_ENABLE_BLURBEHIND
    accent.GradientColor = 0xCC000000  # AARRGGBB: прозрачный чёрный

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 # WCA_ACCENT_POLICY
    data.Data = ctypes.addressof(accent)
    data.SizeOfData = ctypes.sizeof(accent)

    set_attr = ctypes.windll.user32.SetWindowCompositionAttribute
    set_attr(hwnd, ctypes.byref(data))


# --- Главное окно ---
class WinMain(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("‏‎")
        self.setStyleSheet(get_style())
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.init_ui()

        
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        
        def random_s():
            lst = ["乡", "☁", "🝳", "†", "✦"]
            x = random.randint(0,4)
            return lst[x]

        
        self.label = QLabel(f"Ⱥrchangel {random_s()}")
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText('Enter URL')
        self.lineedit.setStyleSheet(get_style())
        
        button = QPushButton("Download")
        button.setStyleSheet(get_style())
        
        button.clicked.connect(self.onclick_button)

        layout.addWidget(self.label)
        layout.addWidget(self.lineedit)
        layout.addWidget(button)


    def onclick_button(self):
        main(self.lineedit.text())
        

# --- Запуск приложения ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinMain()
    icon = QIcon("C:/downloader/config/icon.png")
    win.resize(400, 200)
    win.setMaximumSize(400, 200)
    win.setMinimumSize(200, 130)
    win.setWindowIcon(icon)
    hwnd = int(win.winId())
    enable_blur(hwnd)

    win.show()
    sys.exit(app.exec())