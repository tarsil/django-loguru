from django.contrib.auth.models import User


class MiddlewareConfig:
    """
    Needs to set request.user
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = User.objects.create_user(
            username='test',
            email='foo@bar.com',
            password='foo_bar'
        )
        response = self.get_response(request)
        return response