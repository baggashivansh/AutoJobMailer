import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import csv
import os
import time
from threading import Thread

LOG_FILE = "email_log.csv"
ERROR_FILE = "error_log.txt"

class AutoJobMailerApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoJobMailer")
        master.geometry("550x450")
        self.resume_path = ""
        self.csv_path = ""
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.interval_var = tk.IntVar(value=5)

        tk.Label(master, text="Gmail Email:").pack(pady=5)
        tk.Entry(master, textvariable=self.email_var, width=50).pack()

        tk.Label(master, text="App Password:").pack(pady=5)
        tk.Entry(master, textvariable=self.password_var, width=50, show="*").pack()

        tk.Label(master, text="Resume (PDF):").pack(pady=5)
        tk.Button(master, text="Select Resume", command=self.select_resume).pack()

        tk.Label(master, text="Company CSV:").pack(pady=5)
        tk.Button(master, text="Select CSV", command=self.select_csv).pack()

        tk.Label(master, text="Delay between emails (sec):").pack(pady=5)
        tk.Entry(master, textvariable=self.interval_var, width=10).pack()

        tk.Button(master, text="Start Sending", command=self.start_thread).pack(pady=20)

    def select_resume(self):
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            self.resume_path = path
            messagebox.showinfo("Selected", f"Resume selected:\n{os.path.basename(path)}")

    def select_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            self.csv_path = path
            messagebox.showinfo("Selected", f"CSV selected:\n{os.path.basename(path)}")

    def send_email(self, company, email, manager, custom_line):
        msg = EmailMessage()
        msg['From'] = self.email_var.get()
        msg['To'] = email
        msg['Subject'] = f"Application for Opportunities at {company}"
        msg.set_content(f"Dear {manager},\n\n{custom_line}\n\nBest regards,\nShivansh Bagga")

        with open(self.resume_path, "rb") as f:
            msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(self.resume_path))

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_var.get(), self.password_var.get())
                smtp.send_message(msg)
            with open(LOG_FILE, "a", newline='', encoding='utf-8') as log:
                writer = csv.writer(log)
                writer.writerow([company, email, manager, "Success", time.strftime("%Y-%m-%d %H:%M:%S")])
            print(f"Email sent to {company}")
        except Exception as e:
            with open(ERROR_FILE, "a", encoding='utf-8') as err:
                err.write(f"{company}, {email}, {manager} -> {str(e)}\n")
            print(f"Failed to send to {company}: {str(e)}")

    def start_sending(self):
        if not self.resume_path or not self.csv_path:
            messagebox.showwarning("Missing Files", "Please select both Resume and CSV first!")
            return
        with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.send_email(row['company_name'], row['email'], row['hiring_manager'], row['custom_line'])
                time.sleep(self.interval_var.get())
        messagebox.showinfo("Done", "Emails processed! Check logs for details.")

    def start_thread(self):
        Thread(target=self.start_sending, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoJobMailerApp(root)
    root.mainloop()
