from django.http import HttpResponse
from django.views.generic import View


class SetOffsetView(View):
    http_method_names = ['post']

    @staticmethod
    def post(request, *args, **kwargs):
        offset = request.POST.get('offset', None)
        if not offset:
            return HttpResponse("No 'offset' parameter provided", status=400)

        try:
            offset = int(offset)
        except ValueError:
            return HttpResponse("Invalid 'offset' value provided", status=400)

        tz = offset_to_timezone(int(offset))
        print tz
        request.session['detected_tz'] = tz

        return HttpResponse("OK")
