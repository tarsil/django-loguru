from django.views.generic import View
from django.http import (
    HttpResponse,
)

from rest_framework.response import Response
from rest_framework.views import APIView


class DirectResponseView(View):
    """
    Direct responses
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("Ok")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Ok")

    def put(self, request, *args, **kwargs):
        return HttpResponse("Ok")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Ok")


class DirectResponseApiView(APIView):
    """
    Direct responses
    """
    def get(self, request, *args, **kwargs):
        return Response("Ok")

    def post(self, request, *args, **kwargs):
        return Response("Ok")

    def put(self, request, *args, **kwargs):
        return Response("Ok")

    def delete(self, request, *args, **kwargs):
        return Response("Ok")
