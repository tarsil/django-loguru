# Installation

- `pip install django-loguru`
- Add `django_loguru` to `INSTALLED_APPS` settings.

```python
INSTALLED_APPS = [
    ...
    'django_loguru'
]
```

- Add `DJANGO_LOGURU_MIDDLEWARE` to your settings.

```python
DJANGO_LOGGING_MIDDLEWARE = {
    'DEFAULT_FORMAT': True,
    'MESSAGE_FORMAT': "<b><green>{time}</green> <cyan>{message}</cyan></b>",
    'LOG_USER': False
}
```

- Add `django_loguru.middleware.DjangoLoguruMiddleware` as the very last in the list of `MIDDLEWARE`.

The logs should be now activated for every request/response of you application.

If you desire to override what is shown on the screen.

```python
from django_loguru.middleware import DjangoLoguruMiddleware

class MyCustomMiddleware(DjangoLoguruMiddleware):

    def __call__(self, request):
        """
        Code to be executed on every request/response call.
        """
        logger.info(f"URL: {request.get_raw_uri()}")
        logger.info(f"Method: {request.method}")
        ...
        ...

```
