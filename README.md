
# 🎙️ AltA-Assistant (MyAlexa.py)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Xubuntu](https://img.shields.io/badge/Xubuntu-blue?style=for-the-badge&logo=xfce&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A lightweight, custom-built voice assistant designed specifically for **Xubuntu/XFCE**. 

Built with the philosophy that **developers should own their tools**, this script allows you to launch applications and automate tasks using voice commands triggered by a simple global hotkey.

## ✨ Features
- **Zero Background Bloat**: Only listens when you trigger it (Alt+A).
- **Native Integration**: Uses XFCE's `notify-send` for system-level feedback.
- **Custom Mapping**: Easily map any voice trigger to any shell command or Flatpak.
- **Privacy First**: Local control with a 20-second timeout.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Voice Engine:** SpeechRecognition (Google API backend)
- **OS Integration:** XFCE/Xubuntu (Shell commands & Notify-send)

## 🚀 Installation

1. **Clone the repo:**
   
```bash
   git clone [https://github.com/votre-nom/Xubuntu-Voice-Assistant.git](https://github.com/votre-nom/Xubuntu-Voice-Assistant.git)
   cd Xubuntu-Voice-Assistant
```

2. **Install dependencies:**
```bash
pip install speechrecognition pyaudio

```


3. **Configure the Global Shortcut:**
* Go to `Settings -> Keyboard -> Application Shortcuts`.
* Add a new shortcut.
* Command: `python3 /path/to/myalexa.py`
* Assign to: `Alt + A`



## 📖 How it works

The script initializes a 20-second listening window. It adjusts for ambient noise and waits for specific keywords defined in the `commandes` dictionary. Once a keyword is detected, it executes the linked command and sends a native desktop notification.

> **Why I built this:** Off-the-shelf assistants are often too heavy or intrusive. This project proves that with a few lines of Python, you can create a tool that perfectly fits your professional workflow.

## 📝 License

MIT


    ```

