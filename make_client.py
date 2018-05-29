from argparse import ArgumentParser

from surveymonty import constants, utils

parser = ArgumentParser(
    description=(
        'Generates a full SurveyMonkey client class file from an API spec.'
    )
)
parser.add_argument(
    'name',
    type=str,
    help='The class name for the generated client',
)
parser.add_argument(
    'version',
    type=str,
    help='The API version for the generated client',
)

CLASS_TEMPLATE = """
from surveymonty import utils
from surveymonty.client import BaseClient

class {class_name}(BaseClient):
    version = '{version}'
"""

FUNCTION_TEMPLATE = """
    def {function_name}(self, {function_args}):
        endpoint = '{endpoint}'.format(**locals())

        return self._request('{http_method}', endpoint, self.access_token, **request_kwargs)
"""


def list_to_str(value):
    return '[{}]'.format(', '.join(['\'{}\''.format(item) for item in value]))


def make_client(class_name, version=constants.DEFAULT_VERSION):
    buffer = CLASS_TEMPLATE.format(class_name=class_name, version=version)

    config = utils.load_version_config(version)
    for api_spec in config['endpoints']:
        params = utils.parse_url_params(api_spec['endpoint'])
        function_name = api_spec['name']
        http_method = api_spec['method']
        endpoint = api_spec['endpoint']

        if len(params) > 0:
            function_args = ', '.join(params) + ', **request_kwargs'
        else:
            function_args = '**request_kwargs'

        buffer += FUNCTION_TEMPLATE.format(
            function_name=function_name,
            function_args=function_args,
            http_method=http_method,
            endpoint=endpoint,
            params=list_to_str(params),
        )

    return buffer


if __name__ == '__main__':
    args = parser.parse_args()

    buffer = make_client(args.name, args.version)
    filepath = 'surveymonty/versions/client_{}.py'.format(args.version)

    with open(filepath, 'w') as f:
        f.write(buffer)
