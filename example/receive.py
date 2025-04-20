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

magfa_client = Magfa(username, password, domain)

response = magfa_client.messages(count=100)

if response.status_code == 200 and response.json()["status"] == 0:
    messages = response.json().get("messages", [])
    for msg in messages:
        print(f"From: {msg['sender']}, Message: {msg['messageBody']}")
else:
    print(f"Error: {magfa_client.get_error_message(response.json()['status'])}")
