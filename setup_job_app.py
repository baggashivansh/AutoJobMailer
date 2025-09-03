import os
import csv

# Create required folders
folders = ["csv_watch", "resume"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Sample CSV
csv_file = os.path.join("csv_watch", "sample_companies.csv")
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["company_name","email","hiring_manager","custom_line"])
        writer.writerow(["ABC Corp","hr@abccorp.com","Mr. Sharma","I admire ABC Corp's cloud solutions."])
        writer.writerow(["XYZ Ltd","careers@xyzltd.com","Ms. Gupta","XYZ Ltd’s scalable apps match my expertise."])
        writer.writerow(["Tech Solutions","contact@techsolutions.com","Mr. Verma","Your backend projects excite me."])

# Placeholder resume
resume_file = os.path.join("resume", "Shivansh_Resume.pdf")
if not os.path.exists(resume_file):
    with open(resume_file, "wb") as f:
        f.write(b"%PDF-1.4\n%Placeholder PDF for AutoJobMailer\n")

print("Setup complete! Folders, sample CSV, and placeholder resume created.")
