# 🕵️‍♂️ StealthKeylogger

## 🔹 Overview
**StealthKeylogger** is a Python-based keylogger that runs in the background, silently capturing keystrokes and storing them in a log file. This project is intended for ethical use, such as cybersecurity testing and parental monitoring.

## 🚀 Features
✅ Runs in the background (hidden process)
✅ Logs all keystrokes and saves them to a file
✅ Auto-start functionality (Windows only)
✅ Optional email alerts for remote monitoring (Advanced feature)

## ⚠️ Disclaimer
This tool is **strictly for educational and ethical purposes**. Unauthorized use is illegal.

## 🛠️ Installation & Usage
### 1️⃣ Install Dependencies
```bash
pip install pynput
```

### 2️⃣ Run the Keylogger
```bash
python background_keylogger.py
```

### 3️⃣ Convert to an EXE (Optional for Windows)
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole background_keylogger.py
```

## 📂 Log File Location
Keystrokes are stored in:
```
hidden_keylog.txt
```

## 📧 Advanced: Send Logs via Email
Modify the script to send logs automatically using SMTP.

## 🔹 Future Enhancements
- [ ] Add clipboard monitoring
- [ ] Capture screenshots periodically
- [ ] Stealth mode improvements

## 📜 License
This project is licensed under the MIT License.
