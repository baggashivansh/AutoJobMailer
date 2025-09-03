# AutoJobMailer
```markdown
# 🚀 AutoJobMailer

A **desktop automation app** that helps job seekers send resumes and personalized intro emails to multiple companies with just a few clicks.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Build-Production--Ready-brightgreen.svg)]()

---

## ✨ Features

- 📄 Upload your Resume (PDF)  
- 📊 Import Company CSVs with details  
- 🕵️ Folder Watcher (auto-detect new CSVs)  
- 📝 Customizable Email Templates  
- 📬 Automated Sending with delay to avoid spam filters  
- 🔁 Auto-Retry Failed Emails  
- 📂 Logs for success & errors (`email_log.csv` and `error_log.txt`)  
- 🔔 Notifications on success/failure  
- 🛡️ Gmail App Password supported  

---

## 📂 Project Structure

```

AutoJobMailer/
│── ultimate\_job\_app.py          # Main Tkinter desktop app
│── setup\_job\_app.py             # One-time setup script
│── csv\_watch/                   # Drop company CSVs here
│   └── sample\_companies.csv
│── resume/                      # Store your resume PDF here
│   └── Shivansh\_Resume.pdf
│── email\_log.csv                # Logs of sent emails
│── error\_log.txt                # Logs of errors
│── GMAIL\_APP\_PASSWORD\_GUIDE.txt # Gmail App Password instructions
│── LICENSE                      # MIT License
│── README.md
│── .gitignore

````

---

## 📊 CSV Format

```csv
company_name,email,hiring_manager,custom_line
ABC Corp,hr@abccorp.com,Mr. Sharma,I admire ABC Corp's cloud solutions.
XYZ Ltd,careers@xyzltd.com,Ms. Gupta,XYZ Ltd’s scalable apps match my expertise.
Tech Solutions,contact@techsolutions.com,Mr. Verma,Your backend projects excite me.
````

---

## 🚀 Usage

1. **Run setup once**:

```bash
python setup_job_app.py
```

2. **Launch the app**:

```bash
python ultimate_job_app.py
```

3. **In the GUI**:

* Upload your resume (PDF)
* Select CSV file(s) of company details
* Enter Gmail email + App Password
* Set interval between emails
* Edit templates if needed
* Click **Start Sending**

---

## 🔑 Gmail App Password

* Enable 2-Step Verification on Google Account
* Generate a 16-character App Password for “Mail”
* Use this password instead of your regular Gmail password

---

## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* smtplib (Email sending)
* watchdog (Folder monitoring)
* csv (Data handling & logging)

---

## 📜 License

MIT License – see [LICENSE](LICENSE).

---

👨‍💻 Built with ❤️ by **Shivansh Bagga**
