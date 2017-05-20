import jinja2
import os
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class ErrorPage(webapp2.RequestHandler):
    def get(self):

        template_values = {
            'exception': "404 Not Found",
        }

        template = jinja_environment.get_template('default_error.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/.*', ErrorPage)], debug=True)
