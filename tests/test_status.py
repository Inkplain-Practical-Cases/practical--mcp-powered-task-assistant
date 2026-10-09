# Pure unit test that can run with no external services.
from app.features.feature_status.services.service_read_status import service_read_status

def test_status_payload() -> None:
    assert service_read_status() == {"service": "northstar-task-assistant", "status": "ok"}
