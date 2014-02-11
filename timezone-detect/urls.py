from django.conf.urls import patterns, url

from views import TimezoneView

urlpatterns = patterns('',
                       url(r'^set-timezone/$', TimezoneView.as_view(), name="timezone_detect__set"),
                       url(r'^get-timezone$', TimezoneView.as_view(), name="timezone_detect__get"),
                       )
