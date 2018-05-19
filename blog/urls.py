from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^post/$', views.posts_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.posts_detail),
    url(r'^comment/$', views.comments_list),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.comments_detail),
]
