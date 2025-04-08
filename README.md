# 📡 MagfaSMS Python Client

A simple and clean Python client for interacting with the [Magfa SMS HTTP API v2](https://messaging.magfa.com/ui/?public/wiki/api/http_v2).  
This library allows you to send SMS messages, check message statuses, retrieve inbound messages, and monitor your account balance.


<img src="./doc/logo.png">


<a href="https://www.coffeete.ir/alisharify7">Donate/Support [Optional]</a>


<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size//alisharify7/magfa"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors//alisharify7/magfa"> <img alt="GitHub repo Licence" src="https://img.shields.io/pypi/l/flask_captcha2">

[![Latest version](https://img.shields.io/pypi/v/magfa)](https://pypi.python.org/pypi/magfa)[![Supported python versions](https://img.shields.io/pypi/pyversions/magfa)](https://pypi.python.org/pypi/magfa) [![Downloads](https://static.pepy.tech/badge/magfa)](https://pepy.tech/project/magfa) [![Downloads](https://static.pepy.tech/badge/magfa/month)](https://pepy.tech/project/magfa)
  

## 🚀 Features

- ✅ Send SMS messages to multiple recipients  
- 🔄 Track the delivery status of sent messages  
- 📥 Fetch inbound (received) messages  
- 💰 Check your Magfa account balance  
- 🧾 Error code mapping for human-readable error handling  
- 🔒 Built-in authentication with domain-based credentials

---

## 📦 Installation

```bash
pip install magfa
```


## 🛠️ Usage
## 🔐 Initialization

```python
from magfa_sms import MagfaSMS

client = MagfaSMS(
    username="your_username",
    password="your_password",
    domain="your_domain",
    sender="your_sender_number"
)
```

## ✉️ Send an SMS
```python
response = client.send(
    recipients=["09123456789"],
    messages=["Hello from Magfa!"]
)
print(response.json())
```

## 📊 Check Balance
```python
balance_response = client.balance()
print(balance_response.json())
 ```

## 📩 Get Inbound Messages
```python
inbound = client.messages(count=50)
print(inbound.json())
```


## 📡 Get Message Status
```python
status = client.statuses(mid="123456789")
print(status.json())
```

## 🧠 Error Code Mapping
```python
error_text = MagfaSMS.get_error_message(18)
print(error_text)  # Output: Invalid username or password.
```

## 📚 Resources

<a href="https://messaging.magfa.com/ui/?public/wiki/api/http_v2">Official API Docs</a>

<a href="https://messaging.magfa.com/ui/?public/wiki/api/http_v2#errors">Error Codes Documentation</a>


## 🧑‍💻 Author
Developed by <a href="https://github.com/alisahrify7">Ali Sharify</a>
