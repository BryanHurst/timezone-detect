from django.conf.urls import patterns, url

from views import SetOffsetView

urlpatterns = patterns('',
    url(r'^set/$', SetOffsetView.as_view(), name="timezone_detect__set"),
)
