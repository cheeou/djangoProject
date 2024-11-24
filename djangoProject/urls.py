from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls), # path(route, view)
    path("polls/", include("polls.urls")), # "polls/" route로 시작하는 모든 url 요청은 polls 앱 urls.py로
]
