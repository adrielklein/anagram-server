class RouteCreator(object):
    def __init__(self, app):
        self.app = app

    def set_up_routes(self):
        self.app.add_url_rule('/', 'acknowledge_route', self._acknowledge_route)

    def _acknowledge_route(self):
        return 'OK'
