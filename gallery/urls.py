from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.home, name = 'home'),
    path('search/', views.search_by_category, name='search_by_category'),
    url(r'^locations/(\d+)', views.photos_by_location, name='photosByLocation')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)