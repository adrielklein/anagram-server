class AcknowledgeRoute(object):
    method = 'GET'
    path = '/'
    endpoint = 'acknowledge_route'

    def handle(self):
        return 'OK'
