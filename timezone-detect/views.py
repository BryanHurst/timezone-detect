from django.http import HttpResponse
from django.views.generic import View
from pytz import timezone as tz
from pytz import UnknownTimeZoneError
from django.conf import settings


class SetTimezoneView(View):
    http_method_names = ['post']

    @staticmethod
    def post(request, *args, **kwargs):
        timezone = request.POST.get('timezone', None)
        if not timezone:
            return HttpResponse("No 'timezone' parameter provided", status=400)

        try:
            if "None" in str(timezone).lower():
                timezone = tz(settings.TIME_ZONE)
            else:
                timezone = tz(str(timezone))
        except UnknownTimeZoneError:
            return HttpResponse("Invalid 'timezone' value provided", status=400)
        except:
            return HttpResponse("An unknown error occurred while trying to parse the timezone", status=500)

        print timezone
        request.session['detected_timezone'] = timezone

        return HttpResponse("OK")
