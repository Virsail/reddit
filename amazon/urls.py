from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.page, name='page'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^search/$', views.search_results, name='search_results'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
