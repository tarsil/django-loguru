# Settings

1. `DEFAULT_FORMAT` - Default `True` and it will use the default `MESSAGE_FORMAT`.
2. `MESSAGE_FORMAT` - Sets the format of the log messages. Defaults to
`<b><green>{time}</green> <blue>{message}</blue></b>`. More information about
your options on [loguru](https://loguru.readthedocs.io/en/stable/api/logger.html#color) docs.
3. `LOG_POST` - Default to `False` and it won't show POST data.
4. `LOG_PUT` - Default to `False` and it won't show PUT data.
5. `LOG_PATCH` - Default to `False` and it won't show PATCH data.
6. `LOG_DELETE` - Default to `False` and it won't show DELETE data.
7. `LOG_USER` - Default to `True` and tells which user did the request/response.
