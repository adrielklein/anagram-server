from app.routes.front_end_route import FrontEndRoute


def test_when_front_end_route_is_hit_then_it_redirects_to_html(app):
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert 302 == response.status_code
        assert 'http://localhost/static/index.html' == response.location


def test_when_front_end_route_is_created_then_endpoint_has_same_name():
    assert 'front_end_route' == FrontEndRoute.endpoint
