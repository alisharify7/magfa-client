"""
* magfa client
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/magfa-client
"""

import os
import re
import typing

from requests import Response

from magfa.error_codes import errors
from magfa.http_utils import HttpMethodHelper
from dotenv import load_dotenv

load_dotenv()

class Magfa(HttpMethodHelper):
    """
    Main interface class for interacting with the Magfa SMS HTTP API.

    This class provides methods to send SMS messages, check account balance,
    retrieve inbound messages, and track the delivery status of sent messages.
    Authentication is handled via HTTP Basic Auth using the provided credentials.

    Official documentation:
    - Main API docs: https://messaging.magfa.com/ui/?public/wiki/api/http_v2
    - Error codes: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#errors

    Attributes:
        username (str): Your Magfa account username.
        password (str): Your Magfa account password.
        domain (str): Your Magfa domain.
        endpoint (str): Base URL for the Magfa SMS API. Defaults to the official endpoint.
        sender (str | None): Default sender number for SMS messages.
        auth (tuple): A tuple for HTTP Basic Auth, combining username/domain and password.
        debug (bool): log the http requests to stdout or not.

    Methods:
        balance() -> Response:
            Fetches the account's remaining balance.

        send(recipients: List[str], messages: List[str]) -> Response:
            Sends one or more SMS messages to the specified recipient(s).

        messages(count: int = 100) -> Response:
            Retrieves up to 100 of the latest inbound messages.

        statuses(mid) -> Response:
            Checks the delivery status of a message using its Magfa message ID.

        mid(uid: str) -> Response:
            Retrieves the Magfa message ID corresponding to a user-defined UID.

        get_error_message(error_code: int) -> str:
            Maps an error code returned from the API to a human-readable message.

        normalize_data():
            Placeholder method for future data normalization implementation.
    """

    def __init__(
        self,
        username: str,
        password: str,
        domain: str,
        endpoint: str = "https://sms.magfa.com/api/http/sms/v2/",
        sender: str | None = None,
        debug: bool  = False,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.base_url = endpoint
        self.username = username
        self.password = password
        self.domain = domain
        self.sender = sender
        self.auth = (self.username + "/" + self.domain, self.password)
        self.debug = debug or (os.environ.get("MAGFA_DEBUG", "False") == "True")

    def balance(self) -> Response:
        """get account balance.
        doc : https://messaging.magfa.com/ui/?public/wiki/api/http_v2#balance

        `example` JSON response:
            ..code-block:: json

            {
                "status" : 0,
                "balance" : 1000
            }

            {
                "status" : 18,
                "balance" : null
            }
        """
        return self._get(url=self.base_url + "balance", auth=self.auth)

    def send(
        self,
        recipients: typing.List[str],
        messages: typing.List[str],
    ) -> Response:
        """send sms
        doc: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#send
        """

        return self._post(
            url=self.base_url + "send",
            auth=self.auth,
            json={
                "senders": [self.sender] * len(recipients),
                "recipients": recipients,
                "messages": messages,
            },
        )

    def messages(self, count: int = 100) -> Response:
        """get input messages
        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#messages
        """
        count = count if count <= 100 else 100
        return self._get(url=self.base_url + f"messages/{count}", auth=self.auth)

    def statuses(self, mid) -> Response:
        """status of send message

        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#statuses
        """
        return self._get(url=self.base_url + f"statuses/{mid}", auth=self.auth)

    def mid(self, uid: str) -> Response:
        """
        get
        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#mid
        """
        return self._get(url=self.base_url + f"mid/{uid}", auth=self.auth)

    @staticmethod
    def get_error_message(error_code: int) -> str:
        """this method map the error code to error message.
        error docs: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#errors
        """
        return errors.get(error_code, "error not found")

    @staticmethod
    def _is_valid_phone_number(number: str) -> bool:
        return bool(re.match(r"^09\d{9}$", number))

    def normalize_data(self):
        # TODO: add normalize method
        pass

    def __str__(self):
        return f"<Magfa SMS object {self.username}/{self.domain}>"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.domain!r}, {self.sender!r})"
