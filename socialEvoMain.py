import jinja2
import logging
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class BlogPage(webapp2.RequestHandler):
    def get(self):
        url, welcome_text, url_linktext = get_login(self.request.uri)

        template_values = {
                           'login_url': url,
                           'login_text': url_linktext,
                           'welcome_text': welcome_text,
                           }
        template = jinja_environment.get_template('blog.html')
        self.response.out.write(template.render(template_values))

class IdeaPage(webapp2.RequestHandler):
    def get(self):
        url, welcome_text, url_linktext = get_login(self.request.uri)

        template_values = {
                           'login_url': url,
                           'login_text': url_linktext,
                           'welcome_text': welcome_text,
                           }
        template = jinja_environment.get_template('idea.html')
        self.response.out.write(template.render(template_values))

class GamePage(webapp2.RequestHandler):
    def get(self):
        url, welcome_text, url_linktext = get_login(self.request.uri)

        template_values = {
                           'login_url': url,
                           'login_text': url_linktext,
                           'welcome_text': welcome_text,
                           }
        template = jinja_environment.get_template('game.html')
        self.response.out.write(template.render(template_values))

class GetInvolvedPage(webapp2.RequestHandler):
    def get(self):
        url, welcome_text, url_linktext = get_login(self.request.uri)

        template_values = {
                           'login_url': url,
                           'login_text': url_linktext,
                           'welcome_text': welcome_text,
                           }
        template = jinja_environment.get_template('get_involved.html')
        self.response.out.write(template.render(template_values))

class MainPage(webapp2.RequestHandler):
    def get(self):
        url, welcome_text, url_linktext = get_login(self.request.uri)

        template_values = {
            'login_url': url,
            'login_text': url_linktext,
            'welcome_text': welcome_text,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

def get_login(uri):
    if users.get_current_user():
        url = users.create_logout_url(uri)
        welcome_text = 'Hi %s, not you? ' % users.get_current_user().nickname()
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(uri)
        welcome_text = 'Welcome guest'
        url_linktext = 'Login'
    return (url, welcome_text, url_linktext)

def handle_404(request, response, exception):
    logging.exception(exception)
    template_values = {
        'exception': exception,
    }
    template = jinja_environment.get_template('default_error.html')
    response.write(template.render(template_values))
    response.set_status(404)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/game', GamePage),
                               ('/about/idea', IdeaPage),
                               ('/about/blog', BlogPage),
                               ('/about/get-involved', GetInvolvedPage),
                               ], debug=True)
app.error_handlers[404] = handle_404
