from django.utils import timezone
from pytz import timezone as get_timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        tz = request.session.get('detected_timezone')
        if tz:
            # `request.timezone_active` is used in the template
            # tag to detect if the timezone has been activated
            request.timezone_active = True
            timezone.activate(get_timezone(tz))
        else:
            request.timezone_active = False
            timezone.deactivate()
