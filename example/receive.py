from magfa import Magfa

username = "your_username"
password = "your_password"
domain = "your_domain"

magfa_client = Magfa(username, password, domain)

response = magfa_client.messages(count=100)

if response.status_code == 200:
    messages = response.json().get('messages', [])
    for msg in messages:
        print(f"From: {msg['sender']}, Message: {msg['messageBody']}")
else:
    print(f"Error: {magfa_client.get_error_message(response.json()['status'])}")
