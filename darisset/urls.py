from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
# from django.views.generic.base import TemplateView

from .views import home, home_files

urlpatterns = [
    path('<filename>', home_files, name='home-files'),
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('admin/', admin.site.urls),
)
