import pkg_resources

from .versions.client_v3 import ClientV3


__version__ = pkg_resources.resource_string(
    'surveymonty', 'VERSION'
).decode('utf-8').strip()
