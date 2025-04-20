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

magfa_client = Magfa(username=username, password=password, domain=domain, debug=True)

mid = "your_message_id"

response = magfa_client.statuses(mid)

if response.status_code == 200:
    status = response.json().get("status")
    print(f"Message status: {magfa_client.get_error_message(status)}")
