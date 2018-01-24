from django.conf.urls import url
from django.contrib import admin
from music import views




urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.UserFormView.as_view(), name='registration'),
    url(r'^(?P<album_id>[0-9]+)$', views.details, name='details'),
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    url(r'^album/add$', views.AlbumCreate.as_view(), name='detail-add'),
    url(r'^album/(?P<pk>[0-9]+)/update$', views.Albumupdate.as_view(), name='detail-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='detail-delete'),
]
