from django.contrib import admin
from django.urls import path
from new.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('register/', register),
    path('ochirish/<int:son>/', ochirish),
    path('', loginview),
    path('logout/', logoutview),
]