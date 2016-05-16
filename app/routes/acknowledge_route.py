from flask import redirect
class AcknowledgeRoute(object):
    method = 'GET'
    path = '/'
    endpoint = 'acknowledge_route'

    def handle(self):
        return redirect('/static/index.html')
