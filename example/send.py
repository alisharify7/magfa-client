"""
* magfa client
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/magfa-client
"""

from magfa import Magfa

username = "your_username"
password = "your_password"
domain = "your_domain"
sender = "your_sender_number"  # شماره فرستنده (اختیاری)

magfa_client = Magfa(username=username, password=password, domain=domain, sender=sender, debug=True)

recipients = ["09123456789", "09876543210"]
messages = ["Hello, this is a test message.", "Second message."]

response = magfa_client.send(recipients, messages)

if response.status_code == 200:
    print("Messages sent successfully.")
else:
    print(f"Error: {magfa_client.get_error_message(response.json()['status'])}")
