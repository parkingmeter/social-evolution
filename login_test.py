import unittest
import webapp2
import webtest

from google.appengine.api import users
from google.appengine.ext import testbed

import socialEvoMain

class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGIApplication.
        app = webapp2.WSGIApplication([('/', socialEvoMain.MainPage)])
        # Wrap the app with WebTest's TestApp.
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def loginUser(self, email='user@example.com', id='123', is_admin=False):
        self.testbed.setup_env(
            user_email=email,
            user_id=id,
            user_is_admin='1' if is_admin else '0',
            overwrite=True)

    def testLogin(self):
        self.assertFalse(users.get_current_user())
        self.loginUser()
        self.assertEquals(users.get_current_user().email(), 'user@example.com')
        self.loginUser(is_admin=True)
        self.assertTrue(users.is_current_user_admin())

    def testMainPageNoLogin(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)

    def testIdeaPageNoLogin(self):
        self.testapp.app.router.add(('/about/idea', socialEvoMain.IdeaPage))
        response = self.testapp.get('/about/idea')
        self.assertEqual(response.status_int, 200)

    def testBlogPageNoLogin(self):
        self.testapp.app.router.add(('/about/blog', socialEvoMain.BlogPage))
        response = self.testapp.get('/about/blog')
        self.assertEqual(response.status_int, 200)

    def testIdeaPageNoLogin(self):
        self.testapp.app.router.add(('/about/get-involved', socialEvoMain.GetInvolvedPage))
        response = self.testapp.get('/about/get-involved')
        self.assertEqual(response.status_int, 200)

    def testGamePageNoLogin(self):
        self.testapp.app.router.add(('/game', socialEvoMain.GamePage))
        response = self.testapp.get('/game')
        self.assertEqual(response.status_int, 200)
