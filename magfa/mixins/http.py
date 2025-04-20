"""
* magfa client
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/magfa-client
"""

import json
import typing
import requests
from magfa.mixins.logger import LoggerMixin


class HttpMixin(LoggerMixin):

    def __init__(self, *args, **kwargs):
        self._headers: dict[str, str] = {
            "accept": "application/json",
            "cache-control": "no-cache",
        }

        self.get_timeout = 10
        self.post_timeout = 10
        self.put_timeout = 10
        self.delete_timeout = 10
        self.proxy: dict | None = None
        self.debug: bool = kwargs.get("debug", False)
        super().__init__(*args, **kwargs)

    @property
    def request_headers(self) -> dict[str, str]:
        """Return request headers for each HTTP request."""
        return self._headers

    def add_request_header(self, key: str, value: typing.Any) -> None:
        """Add or update a header."""
        self._headers[str(key)] = str(value)

    def delete_request_header(self, key: str) -> bool:
        """Remove a header if it exists."""
        return self._headers.pop(key, None) is not None

    def _send_request(
        self,
        method: str,
        url: str,
        timeout: int,
        **kwargs,
    ) -> requests.Response:
        self.log(f"{method.upper()} request to: {url}")

        response = requests.request(
            method=method.upper(),
            url=url,
            headers=self.request_headers,
            timeout=timeout,
            **kwargs,
        )

        try:
            body = response.json()
            body_str = json.dumps(body, indent=4)
        except Exception:
            body_str = response.text

        self.log(
            f"{method.upper()} Response: {response.status_code} {response.url}\n{body_str}"
        )

        return response

    def _get(self, url: str, params: dict | None = None, **kwargs) -> requests.Response:
        return self._send_request("get", url, self.get_timeout, params=params, **kwargs)

    def _post(
        self, url: str, data=None, json: dict | None = None, **kwargs
    ) -> requests.Response:
        return self._send_request(
            "post", url, self.post_timeout, data=data, json=json, **kwargs
        )

    def _put(self, url: str, data=None, **kwargs) -> requests.Response:
        return self._send_request("put", url, self.put_timeout, data=data, **kwargs)

    def _delete(self, url: str, **kwargs) -> requests.Response:
        return self._send_request("delete", url, self.delete_timeout, **kwargs)
