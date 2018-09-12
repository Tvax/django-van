from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^latest/$', views.application_download_last, name='application_download_last'),
    url(r'^versions/$', views.application_list, name='application_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)