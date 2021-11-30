import sys

from django.conf import settings as app_settings
from loguru import logger

from .configs import Configs


configs = Configs(app_settings)
logger.remove(0)
logger.add(sys.stderr, colorize=True, format=configs.MESSAGE_FORMAT)


class DjangoLoguruMiddleware:
    """
    Logs all the requests and responses from the application
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed on every request/response call.
        """
        logger.info(f"URL: {request.get_raw_uri()}")
        logger.info(f"Method: {request.method}")

        if request.method == 'GET':
            logger.info(f"Data: {request.method.GET}")

        if configs.LOG_POST and request.method == 'POST':
            logger.info(f"Data: {request.method.POST}")

        if configs.LOG_PUT and request.method == 'PUT':
            logger.info(f"Data: {request.method.PUT}")

        if configs.LOG_PATCH and request.method == 'PATCH':
            logger.info(f"Data: {request.method.PATCH}")

        if configs.LOG_DELETE and request.method == 'DELETE':
            logger.info(f"Data: {request.method.DELETE}")

        response = self.get_response(request)
        logger.info(f"Status Code: {response.status_code}")

        if configs.LOG_USER:
            logger.info(f"User: {request.user}")

        return response
