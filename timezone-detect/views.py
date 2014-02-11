from django.http import HttpResponse
from django.views.generic import View
from pytz import UnknownTimeZoneError
from django.conf import settings
from django.shortcuts import render
from pytz import timezone as tz


class TimezoneView(View):
    http_method_names = ['post', 'get']

    def post(self, request, *args, **kwargs):
        timezone = request.POST.get('timezone', None)
        if not timezone:
            return HttpResponse("No 'timezone' parameter provided", status=400)

        try:
            if "none" in str(timezone).lower():
                timezone = settings.TIME_ZONE
            else:
                timezone = str(timezone)
            temp = tz(timezone)
        except UnknownTimeZoneError:
            return HttpResponse("Invalid 'timezone' value provided", status=400)
        except:
            return HttpResponse("An unknown error occurred while trying to parse the timezone", status=500)

        request.session['detected_timezone'] = timezone

        return HttpResponse(timezone, status=200)

    def get(self, request, *args, **kwargs):
        return render(request, 'timezone.html')