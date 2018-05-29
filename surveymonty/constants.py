"""
surveymonty.constants
---------------------
"""
DEFAULT_HOST = 'https://api.surveymonkey.net'
DEFAULT_VERSION = 'v3'
VERSIONS_MODULE = 'surveymonty.versions'


# Refer to: https://developer.surveymonkey.com/api/v3/#headers

HEADER_SCOPES_AVAILABLE = 'X-OAuth-Scopes-Available'
HEADER_SCOPES_GRANTED = 'X-OAuth-Scopes-Granted'

HEADER_PER_DAY_REQUEST_LIMIT = "X-Ratelimit-App-Global-Day-Limit"
HEADER_PER_DAY_REQUEST_LIMIT_RESET_TIME = "X-Ratelimit-App-Global-Day-Reset"
HEADER_PER_DAY_REQUEST_TOTAL_REMAINING = "X-Ratelimit-App-Global-Day-Remaining"

HEADER_PER_MINUTE_REQUEST_LIMIT = "X-Ratelimit-App-Global-Minute-Limit"
HEADER_PER_MINUTE_REQUEST_LIMIT_RESET_TIME = "X-Ratelimit-App-Global-Minute-Reset"
HEADER_PER_MINUTE_REQUEST_TOTAL_REMAINING = "X-Ratelimit-App-Global-Minute-Remaining"
