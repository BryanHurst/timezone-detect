from django.conf.urls import patterns, url

from views import SetTimezoneView

urlpatterns = patterns('',
                       url(r'^set/$', SetTimezoneView.as_view(), name="timezone_detect__set"),
                       )
