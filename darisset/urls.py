from django.contrib import admin
from django.urls import path
# from django.views.generic.base import TemplateView

from .views import home, home_files

urlpatterns = [
    path('', home, name='home'),
    path('<filename>', home_files, name='home-files'),
    path('admin/', admin.site.urls),
]
