import webapp2
import ee
import ee.oauth
from oauth2client.client import flow_from_clientsecrets

SCOPE = ee.oauth.SCOPE
flow = flow_from_clientsecrets('privatekey.json',
                               scope=SCOPE,
                               redirect_uri='http://localhost:8080/oauth2callback')
flow.approval_prompt = 'force'

class AuthHandler(webapp2.RequestHandler):
    """ Handle authorization """
    def get(self):
        auth_url = flow.step1_get_authorize_url()
        return webapp2.redirect(unicode.encode(auth_url))

class Main(webapp2.RequestHandler):
    """ Handle oauth2callback """
    def get(self):
        # get code
        cod = self.request.get('code')

        # get credentials
        credentials = flow.step2_exchange(cod)

        # initialize with credentials
        ee.Initialize(credentials)

        return webapp2.redirect("/redirected")

class Redirected(webapp2.RequestHandler):
    """ Main Handler. Here goes the main code for the page """
    def get(self):

        # Simple example code
        user = ee.data.getAssetRoots()[0]
        return self.response.out.write(user)

app = webapp2.WSGIApplication([
    webapp2.Route('/', AuthHandler),
    webapp2.Route(r'/oauth2callback', Main),
    webapp2.Route('/redirected', Redirected)
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()