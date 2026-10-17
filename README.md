
# Q-Task: Kurumsal Görev, Kalite ve SLA Takip Sistemi

Bu proje, **Yazılım Kalite Standartları** dersi kapsamında kalite odaklı yazılım geliştirme yaşam döngüsü (SDLC), otomatik kalite kapıları (Quality Gates), güvenlik risk analizi, McCabe döngüsel karmaşıklık ölçümü ve DIR (Discover-Interact-Review) tabanlı Yapay Zeka yönetişimi ilkelerine uygun olarak geliştirilmektedir.

## 👥 Ekip Üyeleri ve Sorumlulukları (7 Kişi)
| Üye No | İsim Soyisim | Rol / Unvan | Sorumlu Olduğu Use Case |
| :--- | :--- | :--- | :--- |
| **Üye 1** | **Alperhan Karşı** | Ekip Lideri & Yazılım Mimarı | `UC-01`: Kullanıcı Kimlik Doğrulama ve RBAC |
| **Üye 2** | [Üye 2 Adı] | İş Analisti & Gereksinim Mühendisi | `UC-02`: Kurumsal Görev Oluşturma ve Atama |
| **Üye 3** | [Üye 3 Adı] | Scrum Master & Backend Geliştirici | `UC-03`: Dinamik Önceliklendirme ve Otomatik SLA Hesabı |
| **Üye 4** | [Üye 4 Adı] | Kalite Güvence (QA) ve Test Lideri | `UC-04`: Görev Durum İş Akışı (State Machine) ve Kalite Onayı |
| **Üye 5** | [Üye 5 Adı] | Güvenlik ve Risk Uzmanı (DevSecOps) | `UC-05`: SLA İhlal Tespiti ve Güvenlik Loglama (Audit Trail) |
| **Üye 6** | [Üye 6 Adı] | Backend Geliştirici & Beyaz Kutu Test Uzmanı | `UC-06`: Departman ve Personel Kalite Metrikleri Analizi |
| **Üye 7** | [Üye 7 Adı] | Ön Yüz (UI/UX) & Dokümantasyon Sorumlusu | `UC-07`: Gelişmiş Arama, Filtreleme ve Rapor Export |

## 🛠️ Teknoloji Yığını ve Kalite Araç Seti (Tech Stack)
* **Dil & Çatı:** Python 3.11+, FastAPI, Streamlit, SQLite, Pydantic
* **Kalite Güvence & Test:**
  * `pytest` & `pytest-cov`: Beyaz/Kara Kutu Birim Testleri ve Kod Kapsama (Coverage) Analizi
  * `radon`: McCabe Döngüsel Karmaşıklık (Cyclomatic Complexity) ve Maintainability Index Hesabı
  * `bandit`: Statik Güvenlik Zafiyeti Tarama (SAST)
  * `flake8` & `black`: PEP-8 Kodlama Standartları Kontrolü
* **Süreç Yönetimi:** Scrumban (GitHub Projects) & GitHub Actions CI/CD

## 📂 Proje Klasör Yapısı
* `docs/`: Faz raporları, gereksinim analizleri ve DIR beyanları
* `src/`: Uygulama kaynak kodları ve iş mantığı modülleri
* `tests/`: Beyaz kutu ve kara kutu test senaryoları

## 🚀 Kurulum ve Çalıştırma
```bash
git clone [https://github.com/alperhank/q-task-quality-system.git](https://github.com/alperhank/q-task-quality-system.git)
cd q-task-quality-system
pip install -r requirements.txt
pytest --cov=src tests/
radon cc src/ -a -s
