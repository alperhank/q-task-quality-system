"""
Q-Task: Kurumsal Görev, Kalite ve SLA Takip Sistemi
Çekirdek İş Mantığı (Core Business Logic) Prototipi - Faz 1 & Faz 2 Hazırlığı
"""
import hashlib
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Any


class TaskStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    IN_REVIEW = "IN_REVIEW"
    DONE = "DONE"
    REOPENED = "REOPENED"


class TaskCategory(str, Enum):
    BUG = "Bug"
    FEATURE = "Feature"
    SECURITY = "Security"
    MAINTENANCE = "Maintenance"


# UC-01: Güvenli Parola Özetleme (RBAC & Kimlik Doğrulama Altyapısı)
def hash_password(password: str, salt: str = "qtask_static_salt_2026") -> str:
    """Parolayı SHA-256 ve salt kullanarak güvenli özet (hash) haline getirir."""
    if not password or len(password) < 6:
        raise ValueError("Parola en az 6 karakter uzunluğunda olmalıdır.")
    salted = f"{password}:{salt}".encode("utf-8")
    return hashlib.sha256(salted).hexdigest()


# UC-03: Dinamik Önceliklendirme ve Otomatik SLA Hesaplama Motoru
def calculate_priority_and_sla(
    category: str, impact: int, urgency: int, created_at: datetime
) -> Dict[str, Any]:
    """
    Görevin kategori, etki (1-5) ve aciliyet (1-5) değerlerine göre
    öncelik seviyesini (P1-P4) ve SLA bitiş tarihini (Deadline) hesaplar.
    """
    if not (1 <= impact <= 5) or not (1 <= urgency <= 5):
        raise ValueError("Etki (impact) ve Aciliyet (urgency) 1 ile 5 arasında olmalıdır.")

    base_score = impact * urgency

    # Güvenlik ve Hata kayıtlarına ağırlık çarpanı uygulanır
    if category == TaskCategory.SECURITY.value:
        weighted_score = base_score * 1.5
    elif category == TaskCategory.BUG.value:
        weighted_score = base_score * 1.2
    else:
        weighted_score = float(base_score)

    # Öncelik sınıfı ve SLA hedef süresi (saat) belirleme
    if weighted_score >= 20:
        priority = "P1 - Kritik"
        sla_hours = 4
    elif weighted_score >= 12:
        priority = "P2 - Yüksek"
        sla_hours = 24
    elif weighted_score >= 6:
        priority = "P3 - Orta"
        sla_hours = 72
    else:
        priority = "P4 - Düşük"
        sla_hours = 168

    deadline = created_at + timedelta(hours=sla_hours)
    return {
        "priority": priority,
        "weighted_score": round(weighted_score, 2),
        "sla_hours": sla_hours,
        "deadline": deadline,
    }


# UC-04: Görev Durum İş Akışı (State Machine) ve Kalite Onay Kapısı
def transition_task_state(
    current_state: TaskStatus, target_state: TaskStatus, user_role: str, rework_count: int = 0
) -> Dict[str, Any]:
    """
    Görev durum geçişlerini kontrol eder. Kalite kontrolünden (IN_REVIEW) geçmeyen
    görevlerin doğrudan tamamlanmasını (DONE) engeller.
    """
    allowed_transitions = {
        TaskStatus.OPEN: [TaskStatus.IN_PROGRESS],
        TaskStatus.IN_PROGRESS: [TaskStatus.IN_REVIEW],
        TaskStatus.IN_REVIEW: [TaskStatus.DONE, TaskStatus.REOPENED],
        TaskStatus.REOPENED: [TaskStatus.IN_PROGRESS],
        TaskStatus.DONE: [],
    }

    if target_state not in allowed_transitions.get(current_state, []):
        raise PermissionError(
            f"Geçersiz durum geçişi: {current_state.value} -> {target_state.value}"
        )

    # Kalite Onay Kapısı: Sadece Takım Lideri (Lead) veya Admin onay/ret verebilir
    if current_state == TaskStatus.IN_REVIEW and user_role not in ("Lead", "Admin"):
        raise PermissionError("Kalite onay veya ret işlemi için 'Lead' veya 'Admin' rolü gereklidir.")

    if target_state == TaskStatus.REOPENED:
        rework_count += 1

    return {
        "new_state": target_state,
        "rework_count": rework_count,
        "quality_approved": target_state == TaskStatus.DONE,
    }
