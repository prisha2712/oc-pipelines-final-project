from app import app


def test_index_returns_project_and_status():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "application": "oc-pipelines-final-project",
        "status": "running",
    }


def test_health_endpoint_is_healthy():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
