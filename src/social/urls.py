"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bro.views.home', name='home'),
    url(r'^index.html', 'bro.views.home', name='home'),
    url(r'^signup.html', 'bro.views.Signup', name='signup'),
    url(r'^auth.asp', 'bro.views.Auth', name='auth'),
    url(r'^create.asp', 'bro.views.Create', name='create'),
    url(r'^try.html', 'bro.views.Try', name='try'),
    url(r'^logout.html', 'bro.views.Logout', name='logout'),
    url(r'^received.html', 'bro.views.Received', name='received'),
    url(r'^accept', 'bro.views.Accept', name='accept'),
    url(r'^decline', 'bro.views.Decline', name='decline'),
    url(r'^add.html', 'bro.views.Add', name='add'),
    url(r'^yourbro.html', 'bro.views.Yourbro', name='yourbro'),
    url(r'^bpage.html', 'bro.views.Bpage', name='bpage'),
    url(r'^chat.html', 'bro.views.Chat', name='chat'),
    url(r'^createchat', 'bro.views.CreateChat', name='createchat'),
    url(r'^send', 'bro.views.Send', name='send'),
    url(r'^deletechat', 'bro.views.DeleteChat', name='deletechat'),
    url(r'^uplo', 'bro.views.Upload', name='uplo'),
    url(r'^contact.html', 'bro.views.Broadcast', name='broadcast'),
    url(r'^broappend.html', 'bro.views.Broappend', name='broappend'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

]
