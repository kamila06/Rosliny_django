from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index, name='index'),
    url(r'^katalog$', views.catalog, name='katalog'),
    # url(r'^kontakt', views.contact, name='kontakt'),
    url('kontakt', views.contact, name='kontakt'),
    url('success/', views.successView, name='success'),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
]