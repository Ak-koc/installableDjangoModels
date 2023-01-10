# receipts/urls.py
from django.urls import re_path

from receipts import views

urlpatterns = [
    re_path(r'^receipt_json/$', views.receipt_json),
]