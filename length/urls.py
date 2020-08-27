from django.urls import path

from length.views import convert

app_name = 'length'

urlpatterns = [
    path('convert/', convert, name='convert')
]
