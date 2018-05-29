"""
surveymonty.client
------------------
"""
from typing import *
from datetime import datetime, timedelta
import json
import logging
import requests

from . import constants, utils
from .exceptions import SurveyMontyAPIError


_logger = logging.getLogger(__name__)


class BaseClient(object):
    """
    Light wrapper for convenient access to the SurveyMonkey API.

    Attributes:
        version (str): The SurveyMonkey API version, e.g. "v3".
        last_headers (dict): The last request headers received.
        last_request_at (datetime): The last time a request was sent.
    """

    version: str = ""

    def __init__(self, access_token: str):
        """
        Args:
            access_token: (str) your SurveyMonkey API access token

        Kwargs:
            version: (str) the SurveyMonkey API version e.g. "v3"
        """
        self.access_token: str = access_token

    def _request(self, method: str, endpoint: str, access_token: str, **request_kwargs) -> requests.Response:
        """
        Wrapper over requests.request.

        Args:
            - method: (str) e.g. "GET", "POST"
            - endpoint: (str) e.g. "/surveys"
            - access_token: (str) your SurveyMonkey API access token

        Kwargs: same as those of requests.request

        Returns: (dict) the JSON response for the given API endpoint
        """
        request_kwargs.setdefault('headers', {})
        request_kwargs['headers'].update({
            "Authorization": 'Bearer {}'.format(self.access_token),
            "Content-Type": "application/json",
        })

        url = utils.make_url(self.version, endpoint)
        resp = requests.request(method, url, **request_kwargs)

        if not resp.ok:
            raise SurveyMontyAPIError(resp)

        # try:
        #     payload = resp.json()
        # except ValueError:
        #     msg = 'unexpected SurveyMonkey API response, no JSON payload'
        #     raise SurveyMontyAPIError(resp, msg)

        _logger.debug('response for %s %s %r', method, endpoint, resp)
        return resp
