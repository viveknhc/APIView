from django.contrib import admin
from django.urls import path
from web.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/',StudentAPIView.as_view()),
    path('api/student/<int:pk>/',StudentAPIView.as_view()),
]
