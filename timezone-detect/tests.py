from datetime import datetime

from pytz.tzinfo import BaseTzInfo

from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware


class ViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def add_session(self, request):
        SessionMiddleware().process_request(request)

    def test_set_timezone(self):
        from .views import TimezoneView
        from pytz import timezone as tz

        request = self.factory.post('/abc', {'timezone': 'America/Denver'})
        self.add_session(request)
        
        response = TimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('detected_timezone', request.session)
        self.assertTrue(tz(request.session['detected_timezone']))
        temp = tz(request.session['detected_timezone'])
        self.assertIsInstance(temp, BaseTzInfo)

    def test_get_timezone(self):
        from .views import TimezoneView

        request = self.factory.get('/abc')
        self.add_session(request)

        response = TimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Timezone is:")

    def test_no_timezone(self):
        from .views import TimezoneView

        request = self.factory.post('/abc')
        self.add_session(request)

        response = TimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_none_timezone(self):
        from .views import TimezoneView

        request = self.factory.post('/abc', {'timezone': 'None'})
        self.add_session(request)

        response = TimezoneView.as_view()(request)
        self.assertContains(response, "America/Chicago")
        self.assertEqual(response.status_code, 200)

    def test_bad_timezone(self):
        from .views import TimezoneView

        request = self.factory.post('/abc', {'timezone': '12foo34'})
        self.add_session(request)

        response = TimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 400)