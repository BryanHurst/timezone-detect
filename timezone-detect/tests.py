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

    def test_xhr_valid(self):
        from .views import SetTimezoneView
        request = self.factory.post('/abc', {'offset': '-60'})
        self.add_session(request)
        
        response = SetTimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('detected_tz', request.session)
        self.assertIsInstance(request.session['detected_tz'], BaseTzInfo)

    def test_xhr_bad_method(self):
        from .views import SetTimezoneView
        request = self.factory.get('/abc')
        self.add_session(request)

        response = SetTimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_xhr_no_offset(self):
        from .views import SetTimezoneView
        request = self.factory.post('/abc')
        self.add_session(request)

        response = SetTimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_xhr_bad_offset(self):
        from .views import SetTimezoneView
        request = self.factory.post('/abc', {'offset': '12foo34'})
        self.add_session(request)

        response = SetTimezoneView.as_view()(request)
        self.assertEqual(response.status_code, 400)