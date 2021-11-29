from django.urls import path

from .views import *

urlpatterns = [
    # function-based views HttpResponse
    path('direct', DirectResponseView.as_view(), name='direct'),
    path('direct-query-params', DirectResponseView.as_view(), name='direct-param'),

    # function-based views Response
    path('restframework/direct', DirectResponseApiView.as_view(), name='drf-direct'),
    path('restframework/direct-query-params', DirectResponseApiView.as_view(),  name='drf-direct-params'),

]