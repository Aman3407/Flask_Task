from flask import Flask
import pytest

from app import create_app  # Replace with the path to your app factory

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True  # Enable testing mode
    yield app

@pytest.fixture
def client(app):
    return app.test_client()