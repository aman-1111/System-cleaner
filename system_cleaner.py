import os
import psutil
import shutil
from tkinter import *
from tkinter import messagebox, filedialog

class SystemCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("System Cleanup & Optimizer")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        self.file_list = []

        Label(root, text="System Cleaner", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        Button(root, text="Scan for Junk Files", command=self.scan_junk, width=25).pack(pady=5)
        Button(root, text="Find Large Files", command=self.find_large_files, width=25).pack(pady=5)
        Button(root, text="Delete Selected Files", command=self.delete_selected, width=25).pack(pady=5)

        self.file_box = Listbox(root, selectmode=MULTIPLE, width=80, height=15)
        self.file_box.pack(pady=10)

        Button(root, text="Refresh System Usage", command=self.refresh_usage, width=25).pack(pady=5)

        self.cpu_label = Label(root, text="CPU Usage: ", bg="#f0f0f0", font=("Helvetica", 12))
        self.cpu_label.pack()
        self.ram_label = Label(root, text="RAM Usage: ", bg="#f0f0f0", font=("Helvetica", 12))
        self.ram_label.pack()

        self.refresh_usage()

    def scan_junk(self):
        self.file_box.delete(0, END)
        self.file_list.clear()
        search_path = filedialog.askdirectory(title="Select folder to scan")

        if not search_path:
            return

        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file.endswith((".tmp", ".log", ".bak", ".old")):
                    full_path = os.path.join(root, file)
                    self.file_list.append(full_path)
                    self.file_box.insert(END, full_path)

        messagebox.showinfo("Scan Complete", f"Found {len(self.file_list)} junk files.")

    def find_large_files(self):
        self.file_box.delete(0, END)
        self.file_list.clear()
        search_path = filedialog.askdirectory(title="Select folder to scan for large files")

        if not search_path:
            return

        for root, dirs, files in os.walk(search_path):
            for file in files:
                try:
                    full_path = os.path.join(root, file)
                    size = os.path.getsize(full_path)
                    if size > 100 * 1024 * 1024:  # Files > 100 MB
                        self.file_list.append(full_path)
                        self.file_box.insert(END, f"{full_path} [{round(size/1024/1024)} MB]")
                except:
                    continue

        messagebox.showinfo("Scan Complete", f"Found {len(self.file_list)} large files.")

    def delete_selected(self):
        selected = self.file_box.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Select at least one file to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete selected files?")
        if not confirm:
            return

        deleted_count = 0
        for i in selected:
            try:
                file_path = self.file_list[i]
                os.remove(file_path)
                deleted_count += 1
            except:
                continue

        messagebox.showinfo("Deletion Complete", f"{deleted_count} files deleted.")
        self.scan_junk()  # Rescan to refresh the list

    def refresh_usage(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        self.cpu_label.config(text=f"CPU Usage: {cpu}%")
        self.ram_label.config(text=f"RAM Usage: {ram}%")


if __name__ == "__main__":
    root = Tk()
    app = SystemCleaner(root)
    root.mainloop()
