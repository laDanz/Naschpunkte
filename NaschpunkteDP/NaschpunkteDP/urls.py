"""NaschpunkteDP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import NaschpunkteApp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', NaschpunkteApp.views.index),
    url(r'^lsa/$', NaschpunkteApp.views.list_activities),
    url(r'^lsn/$', NaschpunkteApp.views.list_naschies),
    url(r'^cre/$', NaschpunkteApp.views.create_event),
    url(r'^lse/$', NaschpunkteApp.views.list_events),
    url(r'^cru/$', NaschpunkteApp.views.create_user),
    url(r'^login/$', NaschpunkteApp.views.login_user),
    url(r'^logout/$', NaschpunkteApp.views.logout_user),
    url(r'^rest/', NaschpunkteApp.views.rest),
]
