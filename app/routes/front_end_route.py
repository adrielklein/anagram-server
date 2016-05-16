from werkzeug.utils import redirect


class FrontEndRoute(object):
    method = 'GET'
    path = '/'
    endpoint = 'front_end_route'

    def handle(self):
        return redirect('/static/index.html')
