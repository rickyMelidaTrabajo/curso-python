from werkzeug.wrappers import Request, Response, ResponseStream

class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.username = 'Tony'
        self.password = 'IamIronMan'

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username']
        password = request.autorization['password']

        # these are hardcoded for demostration
        #verify the username and password from some database or env config variable
        if username == self.username and password == self.password:
            environ['user'] = { 'name': 'Tony' }
            return self.app(environ, start_response)
        
        res = Response(u'Authorization failed', mimetype='text/plain', status=401)
        return res(environ, start_response)


