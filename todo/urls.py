from django.contrib import admin
from django.urls import path
from new.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('register/', register),
    path('todo/ochirish/<int:pk>/', ochirish),
    path('', loginview),
    path('logout/', logoutview),
]