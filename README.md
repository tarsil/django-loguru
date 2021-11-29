# Django Loguru Middleware

The extension was based on another one and added some extra flavours.
One of the biggest problems with the apps is the logging and that can be messy sometimes.

Since this serves as a middleware, it only depends on django (including django rest framework).

## Table of Contents

---

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Settings](#settings)
4. [License](#license)

---

## Requirements

1. Python >= 3.7
2. [Django](https://www.djangoproject.com/) >= 3.1

## Installation

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

## Settings

1. `DEFAULT_FORMAT` - Default `True` and it will use the default `MESSAGE_FORMAT`.
2. `MESSAGE_FORMAT` - Sets the format of the log messages. Defaults to
`<b><green>{time}</green> <blue>{message}</blue></b>`. More information about
your options on [loguru](https://loguru.readthedocs.io/en/stable/api/logger.html#color) docs.
3. `LOG_POST` - Default to `False` and it won't show POST data.
4. `LOG_PUT` - Default to `False` and it won't show PUT data.
5. `LOG_PATCH` - Default to `False` and it won't show PATCH data.
6. `LOG_DELETE` - Default to `False` and it won't show DELETE data.
7. `LOG_USER` - Default to `True` and tells which user did the request/response.

## License

MIT-License
