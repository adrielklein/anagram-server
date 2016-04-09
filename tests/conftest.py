import pytest
from app.app import create_app
from app.corpus import Corpus


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def corpus():
    return Corpus()
