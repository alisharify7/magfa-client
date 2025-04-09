"""
 * magfa client
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2025 - ali sharifi
 * https://github.com/alisharify7/magfa-client
"""

# build in
import typing
import logging

# lib
import requests


class LOG:
    @staticmethod
    def log(*args, **kwargs):
        logging.warning(*args, **kwargs)

    @staticmethod
    def info(*args, **kwargs):
        logging.info(*args, **kwargs)


class HttpMethodHelper:
    """Some useful Basic base HTTP methods"""

    def __init__(self, *args, **kwargs):
        self.__headers: typing.Dict[str, str] = {
            "accept": "application/json",
            "cache-control": "no-cache",
        }
        self.get_timeout: int = 10
        self.post_timeout: int = 10
        self.put_timeout: int = 10
        self.delete_timeout = 10
        self.proxy: dict | None = None

        super().__init__(*args, **kwargs)

    @property
    def request_headers(self) -> typing.Dict:
        """this property returns a dict for each request header
        headers contains authentication headers, etc,
        """
        return self.__headers

    def add_request_header(self, key: str, value: typing.Any) -> None:
        """
        update or adding a new header to headers repository

        :param key: the key of the new header
        :type key: str

        :param value: value of key param in the header
        :type key: any

        .. highlight:: python
        .. code-block:: python
            obj.add_request_header(key='auth', value='token')

        """
        self.__headers.update({str(key): value})

    def delete_request_header(self, key: str) -> bool:
        """
        deleting an existing header from headers list

        :param key: name of the header that should be deleted.
        :type key: str


        .. highlight:: python
        .. code-block:: python
            obj.delete_request_header(key='auth')

        """
        if key in self.__headers:
            self.__headers.pop(key)
            return True

        return False

    def _get(self, url: str, params: dict | None = None, **kwargs) -> requests.Response:
        """
        Send HTTP GET request with given params

        this method is a wrapper(proxy) for requests.get method

         :param url: just ``url path`` not whole url, the whole url is taken from self.endpoint
         :type url: str

         :param params: HTTP GET url parameters
         :type params: dict

         :param kwargs: optional arguments
         :type kwargs: dict


        doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
        """
        LOG.info("GET request: %s" % url)

        response = requests.get(
            url=url,
            params=params,
            **kwargs,
            headers=self.request_headers,
            timeout=self.get_timeout,
        )

        LOG.info(
            "GET request Response Code: %s %s" % (response.status_code, response.url)
        )
        return response

    def _post(self, url: str, data=None, json: dict | None = None, **kwargs):
        """
        Send HTTP POST request with given params

        this method is a wrapper(proxy) for requests.post method

         :param url: just ``url path`` not whole url, the whole url is taken from self.endpoint
         :type url: str

         :param data: data for POST request
         :type data: any

         :param json: json body for POST request
         :type json: dict

         :param kwargs: optional arguments
         :type kwargs: dict


        doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
        """
        LOG.info("POST request: %s" % url)

        response = requests.post(
            url=url,
            data=data,
            json=json,
            **kwargs,
            headers=self.request_headers,
            timeout=self.post_timeout,
        )

        LOG.info("POST request Response Code: %s" % response.status_code)
        return response

    def _delete(self, url: str, **kwargs):
        """
        Send HTTP DELETE request with given params

        this method is a wrapper(proxy) for requests.delete method

         :param url: just ``url path`` not whole url, the whole url is taken from self.endpoint
         :type url: str


         :param kwargs: optional arguments
         :type kwargs: dict


        doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
        """
        LOG.info("DELETE request: %s" % url)

        response = requests.delete(
            timeout=self.delete_timeout,
            url=url,
            **kwargs,
            headers=self.request_headers,
        )
        LOG.info("DELETE request Response Code: %s" % response.status_code)
        return response

    def _put(self, url: str, data=None, **kwargs):
        """
           Send HTTP PUT request with given params
           this method is a wrapper(proxy) for requests.put method

        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.

           doc: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
        """
        LOG.info("PUT request: %s" % url)
        response = requests.put(
            url=url,
            data=data,
            headers=self.request_headers,
            timeout=self.put_timeout,
            **kwargs,
        )

        LOG.info("PUT request Response Code: %s" % response.status_code)
        return response
