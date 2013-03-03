import webapp2
import jinja2
import os
import americanize

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        # get name to be translated
        name = self.request.get("name")
        sex = self.request.get("sex")

        # find similar names
        similar_names = []
        if name and sex:
            similar_names = americanize.americanize(name, sex)

        # render template
        template_values = {
            'similar_names': similar_names,
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
