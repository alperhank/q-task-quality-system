"""
Q-Task Birim ve Sınır Değer Testleri (Pytest)
"""
from datetime import datetime
import pytest
from src.core_engine import (
    TaskStatus,
    calculate_priority_and_sla,
    hash_password,
    transition_task_state,
)


def test_hash_password_valid_and_short():
    hashed = hash_password("GuvenliSifre123")
    assert len(hashed) == 64
    with pytest.raises(ValueError):
        hash_password("123")


def test_calculate_priority_security_critical():
    now = datetime(2026, 10, 15, 10, 0)
    result = calculate_priority_and_sla("Security", impact=5, urgency=4, created_at=now)
    assert result["priority"] == "P1 - Kritik"
    assert result["sla_hours"] == 4


def test_calculate_priority_invalid_bounds():
    now = datetime(2026, 10, 15, 10, 0)
    with pytest.raises(ValueError):
        calculate_priority_and_sla("Bug", impact=6, urgency=2, created_at=now)


def test_quality_gate_blocks_direct_completion():
    with pytest.raises(PermissionError):
        transition_task_state(TaskStatus.IN_PROGRESS, TaskStatus.DONE, user_role="Specialist")


def test_quality_review_rejection_increments_rework():
    res = transition_task_state(
        TaskStatus.IN_REVIEW, TaskStatus.REOPENED, user_role="Lead", rework_count=0
    )
    assert res["new_state"] == TaskStatus.REOPENED
    assert res["rework_count"] == 1
    assert res["quality_approved"] is False
