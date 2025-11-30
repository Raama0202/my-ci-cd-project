import pytest
from app import app, tasks


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Reset tasks before each test
        tasks.clear()
        yield client


def test_index_page(client):
    """Test if the index page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List" in response.data


def test_add_task(client):
    """Test adding a new task."""
    response = client.post("/add", data={"task": "My New Task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"My New Task" in response.data
    assert len(tasks) == 1
    assert tasks[0]["text"] == "My New Task"
    assert not tasks[0]["done"]


def test_toggle_task(client):
    """Test toggling a task's status."""
    # First, add a task
    client.post("/add", data={"task": "Test Toggle"}, follow_redirects=True)
    assert not tasks[0]["done"]

    # Now, toggle it
    response = client.post("/toggle/0", follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]["done"]
