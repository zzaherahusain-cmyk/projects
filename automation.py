import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

print("=== CodeAlpha Task 3 Started ===")

# Task 1: Move JPG files to jpg_folder
os.makedirs("jpg_folder", exist_ok=True)
for f in os.listdir("input_files"):
    if f.lower().endswith((".jpg", ".jpeg")):
        shutil.move(f"input_files/{f}", f"jpg_folder/{f}")
        print(f"Moved: {f}")
print("Task 1 Done: JPG files moved")

# Task 2: Extract emails from data.txt
with open("input_files/data.txt", "r") as file:
    text = file.read()
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
with open("extracted_emails.txt", "w") as f:
    f.write("\n".join(emails))
print(f"Task 2 Done: {len(emails)} emails saved")

# Task 3: Scrape website title
response = requests.get("https://www.google.com")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string
with open("website_title.txt", "w") as f:
    f.write(f"Website Title: {title}")
print(f"Task 3 Done: Title = {title}")

print("=== All Tasks Completed Successfully ===")
