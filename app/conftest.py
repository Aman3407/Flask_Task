import pytest
from app import app
import db
import os

@pytest.fixture
def client():
    # Setup: Create a test client
    app.config['TESTING'] = True
    # Use an in-memory database for testing
    app.config['DATABASE'] = ':memory:'
    
    # Setup in-memory database
    db.connect()

    with app.test_client() as client:
        yield client

    # # Teardown: Remove the in-memory database file (if applicable)
    # if os.path.isfile('employees.db'):
    #     os.remove('employees.db')
