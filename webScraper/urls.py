from django.contrib import admin
from django.urls import path, include
from wiki import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls')),
]
