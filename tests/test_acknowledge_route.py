def test_when_acknowledge_route_is_hit_then_it_returns_okay(app):
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert 'OK' == response.data.decode()
