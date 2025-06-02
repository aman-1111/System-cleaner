# 🧹 System Cleanup Utility using Python

A lightweight and efficient Python application that helps clean unnecessary files such as temporary data, system cache, and unused logs to optimize your system's performance.

## 🚀 Features

- 🔍 Scans system for temporary files, logs, and cache
- 🧼 Automatically deletes unnecessary files
- 🪣 Clears Recycle Bin (Windows)
- 📊 Displays space saved after cleanup
- 🖥️ Optional GUI using Tkinter for easy interaction
- 🧱 Modular and easy to extend

## 🛠️ Technologies Used

- Python 3
- `os`, `shutil`, `tempfile`, `subprocess`
- `tkinter` (for GUI version)
- `psutil` (optional for resource stats)

## 📁 Project Structure

system-cleanup/
│
├── cleanup.py # Core cleanup script
├── gui.py # Optional GUI using Tkinter
├── utils.py # Helper functions
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## 🖥️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/system-cleanup-python.git
cd system-cleanup-python

2. (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Script

python cleanup.py          # For CLI version
python gui.py              # For GUI version (optional)

⚠️ Disclaimer

Use this utility carefully. Make sure to review which directories or file types are being deleted to avoid unintended loss of important data.
📄 License

This project is open-source and available under the MIT License.
🤝 Contributing

Pull requests and contributions are welcome! Feel free to fork this repo and submit improvements.
🔗 Connect with Me

Aman Chaurasia
📧 amanchaurasia687@gmail.com
