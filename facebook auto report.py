class colors:
    BIGreen = "[\033[1;92m\]"
    cyan = "\033[1;36m"

print(colors.indigo + """
╔═══╦══╗─╔═══╦═══╦═══╦═══╦═══╦════╗╔════╦═══╦═══╦╗
║╔══╣╔╗║─║╔═╗║╔══╣╔═╗║╔═╗║╔═╗║╔╗╔╗║║╔╗╔╗║╔═╗║╔═╗║║
║╚══╣╚╝╚╗║╚═╝║╚══╣╚═╝║║─║║╚═╝╠╝║║╚╝╚╝║║╚╣║─║║║─║║║
║╔══╣╔═╗║║╔╗╔╣╔══╣╔══╣║─║║╔╗╔╝─║║────║║─║║─║║║─║║║─╔╗
║║──║╚═╝║║║║╚╣╚══╣║──║╚═╝║║║╚╗─║║────║║─║╚═╝║╚═╝║╚═╝║
╚╝──╚═══╝╚╝╚═╩═══╩╝──╚═══╩╝╚═╝─╚╝────╚╝─╚═══╩═══╩═══╝""")
print(colors.cyan + u'\033[40m' + """
            ▄▄▄▄
          ▄██████     ▄▄▄█▄
        ▄██▀░░▀██▄    ████████▄
       ███░░░░░░██     █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌       ▀█▄
     ███░░▐█░█▌░██    █▌         ▀▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████   ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████


 """)
print("[+]A FB Cookie Stealer Created By HAZKIE DEV[+]")

import requests
import time
from bs4 import BeautifulSoup

class FacebookAutoReport:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.login_url = 'https://www.facebook.com/login.php'
        self.report_url = 'https://www.facebook.com/report.php'

    def login(self):
        payload = {
            'email': self.username,
            'pass': self.password
        }
        response = self.session.post(self.login_url, data=payload)
        if "c_user" in self.session.cookies:
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False

    def report(self, report_id):
        payload = {
            'id': report_id,
            'reason': 'Spam',
            'submit': 'Report'
        }
        response = self.session.post(self.report_url, data=payload)
        if response.status_code == 200 and "Thank you for your report" in response.text:
            print(f"Report submitted for ID: {report_id}")
        else:
            print(f"Failed to report ID: {report_id}")

    def auto_report(self, report_ids):
        for report_id in report_ids:
            self.report(report_id)
            time.sleep(2)  # Avoid rate limiting

if __name__ == "__main__":
    username = input("Enter your Facebook username: ")
    password = input("Enter your Facebook password: ")
    report_ids = input("Enter IDs to report (comma-separated): ").split(',')

    fb_auto_report = FacebookAutoReport(username, password)
    if fb_auto_report.login():
        fb_auto_report.auto_report(report_ids)
