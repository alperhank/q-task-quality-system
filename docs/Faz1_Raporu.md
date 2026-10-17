PROJE RAPORU: FAZ 1 ÇIKTILARI
Proje Adı: Q-Task: Kurumsal Görev, Kalite ve SLA (Hizmet Seviyesi) Takip Sistemi Ekip Büyüklüğü: 7 Kişi
1. Ekiplerin, Görevlerin ve Yapılacak Katkıların Belirlenmesi (Faz 1 - i)
Proje kapsamında iş yükü 7 ekip üyesi arasında dengeli ve birbirini tamamlayacak şekilde dağıtılmıştır. Her üye hem belirli bir yazılım yaşam döngüsü (SDLC) ve kalite rolünden hem de en az bir ana Kullanım Durumu (Use Case) ve ilgili modülün uçtan uca geliştirilmesinden sorumludur.
Üye No	Öğrenci Adı & No	Proje Rolü	Sorumlu Olduğu Faz Görevleri ve Katkılar	Sorumlu Olduğu Use Case
Üye 1	Alperhan Karşı(Öğrenci No)	Ekip Lideri & Yazılım Mimarı (Team Lead & Architect)	GitHub repo yönetimi, Faz 1 süreç/araç kurulumu, Faz 3 mimari tasarım kararları, Faz 4 CI/CD (Devreye alım) boru hattı kurulumu ve kod birleştirme (PR) onayları.	UC-01: Kullanıcı Kimlik Doğrulama ve Rol Tabanlı Erişim Kontrolü (RBAC)
Üye 2	Üye 2 Adı Soyadı(Öğrenci No)	İş Analisti & Gereksinim Mühendisi	Faz 1 fonksiyonel/fonksiyonel olmayan gereksinimlerin analizi, Faz 2 gereksinim gözden geçirme (review) liderliği, izlenebilirlik matrisi ve DIR beyanlarının konsolidasyonu.	UC-02: Kurumsal Görev (Task) Oluşturma, Kategorizasyon ve Atama Modülü
Üye 3	Üye 3 Adı Soyadı(Öğrenci No)	Çevik Süreç Yöneticisi (Scrum Master) & Backend Geliştirici	Sprint planlamaları, Kanban/Scrum panosu takibi, iş kuralları motorunun (SLA hesaplama algoritması) geliştirilmesi ve Faz 3 kod gözden geçirme (Code Review) organizasyonu.	UC-03: Dinamik Önceliklendirme ve Otomatik SLA (Hizmet Süresi) Hesaplama Modülü
Üye 4	Üye 4 Adı Soyadı(Öğrenci No)	Kalite Güvence (QA) ve Test Lideri	Faz 2 Kalite Kapılarının (Quality Gates) ve Test Planının hazırlanması, Faz 4 Kara Kutu (Black-Box) test senaryolarının (Denklik Payları, Sınır Değer Analizi) yürütülmesi.	UC-04: Görev Durum İş Akışı (State Machine) ve Kalite Onay (Review) Mekanizması
Üye 5	Üye 5 Adı Soyadı(Öğrenci No)	Güvenlik ve Risk Uzmanı (DevSecOps)	Faz 2 Güvenlik Risk Değerlendirmesi (OWASP Top 10 & STRIDE), Faz 3 güvenli kodlama denetimleri (Bandit/SonarCloud entegrasyonu) ve denetim izi (Audit Log) yapısı.	UC-05: SLA İhlal Tespiti, Eskalasyon (Üst Birime Aktarım) ve Güvenlik Loglama Modülü
Üye 6	Üye 6 Adı Soyadı(Öğrenci No)	Kıdemli Backend Geliştirici & Beyaz Kutu Test Uzmanı	Veritabanı şema tasarımı, Faz 4 Beyaz Kutu (White-Box) birim testlerinin (pytest) yazılması, kod kapsama (Coverage) analizi ve McCabe Döngüsel Karmaşıklıkhesaplamaları.	UC-06: Departman ve Personel Performans / Kalite Metrikleri Analiz Modülü
Üye 7	Üye 7 Adı Soyadı(Öğrenci No)	Ön Yüz (UI/UX) Geliştirici & Dokümantasyon Sorumlusu	Kullanıcı arayüzü geliştirme, Faz 4 Kullanıcı Kabul Testleri (UAT), Faz 5 nihai rapor formatlama, referans yönetimi ve sunum/demo hazırlığı.	UC-07: Gelişmiş Arama, Filtreleme ve Kurumsal Rapor Dışa Aktarma (CSV/PDF Export)
2. Tech Stack, Araç Seti, Süreç ve Zaman Planı (Faz 1 - ii)
2.1. Teknoloji Yığını (Tech Stack) ve Kalite Araç Seti
Projede, yazılım kalite standartlarının (ISO/IEC 25010) ölçülebilirliğini ve otomasyonunu en üst düzeye çıkarmak amacıyla Python tabanlı modern ve modüler bir mimari seçilmiştir:
	Programlama Dili ve Çatı (Framework): Python 3.11+, FastAPI (RESTful API ve İş Mantığı Katmanı), Streamlit (Hızlı ve Etkileşimli Kurumsal Arayüz Katmanı).
	Veritabanı ve ORM: SQLite (Geliştirme/Test ortamı için sıfır kurulum gereksinimi) ve SQLAlchemy ORM, Pydantic (Veri doğrulama ve şema kontratları).
	Versiyon Kontrol ve CI/CD: Git, GitHub, GitHub Actions (Otomatik test ve kalite kapısı kontrolü).
	Kalite Güvence, Test ve Statik Analiz Araçları:
	Pytest & Pytest-Cov: Beyaz kutu birim testleri ve satır/dal bazlı kod kapsama (Code Coverage) ölçümü.
	Radon: Faz 4'te modül bazında McCabe Döngüsel Karmaşıklık (Cyclomatic Complexity) ve Bakım Yapılabilirlik İndeksi (Maintainability Index) hesaplaması.
DOCX
	Flake8 / Black: PEP-8 kodlama standartları ve stil kontrolü (Linter).
	Bandit: Python kodundaki güvenlik zafiyetlerinin statik analizi (SAST).
	Kullanılan Yapay Zeka Araçları: Google Gemini (Gereksinim analizi, mimari tartışma, test senaryosu üretimi ve kod refaktörिंग desteği — Tüm kullanımlar DIR metodolojisi ile kayıt altına alınmaktadır).
2.2. İş Yapış Şekli (Çevik Süreç - Hibrit Scrum/Kanban)
Ekip, dersin 2-3 haftalık faz teslim döngülerine uyum sağlamak amacıyla Scrumban (Scrum + Kanban) metodolojisini benimsemiştir:
DOCX
	Sprint Döngüleri: Her proje fazı (Faz 1 - Faz 5) bir Sprint (2-3 Hafta) olarak kabul edilir.
DOCX
	Kanban Panosu (GitHub Projects): İş kalemleri Backlog -> Ready -> In Progress -> Quality Gate / Code Review -> Testing-> Done sütunlarında takip edilir.
	Bitti Tanımı (Definition of Done - DoD): Bir görev (veya Use Case) ancak; kodu yazılıp PEP-8 standartlarına uyduğunda, en az 1 ekip arkadaşı tarafından gözden geçirildiğinde (Peer Review), birim testlerinden geçtiğinde ve ilgili DIR beyanı yazıldığında Done sütununa taşınabilir.
2.3. Zaman Planı (Takvim)
Faz	Dönem / Süre	Temel Odak ve Teslimatlar	Sorumlu Lider
Faz 1	Hafta 1 - 3	Ekip kurulumu, Tech Stack, Süreç planı, Kapsam ve 7 Use Case tanımı.
DOCX	Üye 1 & Üye 2
Faz 2	Hafta 4 - 6	Faz 1 Review, Kalite Kapıları (Quality Gates), Test Planı, Güvenlik Risk Analizi.
DOCX	Üye 4 & Üye 5
Faz 3	Hafta 7 - 9	Faz 2 Review, Mimari alternatifler ve kararlar, Kodlama ve Code Review.
DOCX	Üye 1 & Üye 3
Faz 4	Hafta 10 - 12	Faz 3 Review, Beyaz/Kara Kutu Testleri, McCabe Karmaşıklık Analizi, Devreye Alım.
DOCX	Üye 6 & Üye 4
Faz 5	Hafta 13 - 14	Faz 4 Review, Nihai Rapor (Max 20 syf), DIR Beyanları, Canlı Demo ve Sunum.
DOCX	Üye 7 & Tüm Ekip
3. Proje Konusu, Kapsamı ve Gereksinimler (Faz 1 - iii)
3.1. Proje Konusu ve Amacı
Q-Task (Kurumsal Görev, Kalite ve SLA Takip Sistemi); yazılım ve teknoloji şirketlerinde departmanlar arası açılan görevlerin (hata kaydı, yeni özellik talebi, altyapı bakımı, güvenlik yaması vb.) yaşam döngüsünü yöneten, görevin kritiklik derecesine göre otomatik SLA (Hizmet Seviyesi Anlaşması - Çözüm Süresi) hesaplayan, kalite onay kapılarından geçmeyen görevlerin kapatılmasını engelleyen ve personel/departman bazlı kalite metrikleri üreten bir kurumsal web uygulamasıdır.
3.2. Temel Fonksiyonel Gereksinimler (FR) ve Fonksiyonel Olmayan Gereksinimler (NFR)
	FR-01: Sistem, kullanıcıları Admin, Takım Lideri (Reviewer) ve Uzman (Assignee) rollerine göre yetkilendirmelidir.
	FR-02: Görev oluşturulurken aciliyet, etki alanı ve departman bilgilerine göre dinamik bir öncelik skoru ve SLA bitiş tarihi (Deadline) otomatik hesaplanmalıdır.
	FR-03: Görevler belirli bir durum makinesi (State Machine: Açık -> İşlemde -> Kalite Kontrolünde -> Tamamlandı / Reddedildi) kurallarına göre ilerlemelidir.
	NFR-01 (Bakım Yapılabilirlik - Maintainability): Hiçbir fonksiyonun McCabe Döngüsel Karmaşıklık (Cyclomatic Complexity) değeri 10'u geçmemelidir (Hedef: ≤7).
	NFR-02 (Güvenilirlik & Test Edilebilirlik): İş mantığı (Business Logic) modüllerinde birim test kapsama oranı (Code Coverage) en az %80 olmalıdır.
	NFR-03 (Güvenlik): Parolalar düz metin olarak saklanmamalı (SHA-256 / Bcrypt ile özetlenmeli), tüm kritik durum geçişleri değiştirilemez denetim günlüğüne (Audit Log) kaydedilmelidir.
3.3. Kullanım Durumları (Use Cases) — (Kişi Başı 1 Adet, Toplam 7 Use Case)
UC-01: Kullanıcı Kimlik Doğrulama ve Rol Tabanlı Erişim Kontrolü (RBAC)
	Sorumlu Üye: Üye 1 (Alperhan Karşı)
	Aktörler: Tüm Kullanıcılar (Admin, Takım Lideri, Uzman)
	Ön Koşullar: Kullanıcının sistem veritabanında aktif bir hesabının bulunması.
	Temel Akış:
	Kullanıcı, kullanıcı adı ve şifresini girerek giriş talebinde bulunur.
	Sistem, girilen şifreyi kriptografik özet (hash) fonksiyonundan geçirerek veritabanındaki kayıtla karşılaştırır.
	Doğrulama başarılıysa, kullanıcının rolünü (Admin, Lead, Specialist) yükler ve oturum (Session/Token) başlatır.
	Kullanıcıya yalnızca kendi rolünün yetkili olduğu menü ve işlem butonları gösterilir.
	Alternatif / Hata Akışı (3a): Şifre hatalıysa sistem genel bir hata mesajı döner ("Geçersiz kimlik bilgileri"), başarısız giriş sayacını artırır. Арdışık 5 hatalı girişte hesabı 15 dakika kilitler ve güvenlik logu üretir.
	Son Koşullar: Kullanıcı güvenli bir şekilde sisteme erişir ve yetki sınırları uygulanır.
UC-02: Kurumsal Görev (Task) Oluşturma, Kategorizasyon ve Atama
	Sorumlu Üye: Üye 2
	Aktörler: Takım Lideri, Admin
	Ön Koşullar: Kullanıcının sisteme giriş yapmış ve görev oluşturma yetkisine sahip olması.
	Temel Akış:
	Kullanıcı "Yeni Görev Oluştur" formunu açar; Başlık, Açıklama, Kategori (Bug, Feature, Security, Maintenance), Etki Seviyesi (1-5) ve Aciliyet (1-5) bilgilerini girer.
	Görevin atanacağı uzmanı (Assignee) seçer ve kaydet butonuna basar.
	Sistem, veri şeması doğrulamasını (boş alan kontrolü, karakter sınırları) yapar.
	Doğrulama başarılıysa görev benzersiz bir ID ile AÇIK (OPEN) durumunda kaydedilir.
	Alternatif / Hata Akışı (3a): Başlık 5 karakterden kısaysa veya atanacak uzmanın üzerinde zaten maksimum kapasitede (örn. >5 aktif kritik görev) iş varsa sistem uyarı verir ve kaydı engeller.
	Son Koşullar: Görev veritabanına kaydedilir ve SLA hesaplama modülü (UC-03) tetiklenir.
UC-03: Dinamik Önceliklendirme ve Otomatik SLA Hesaplama
	Sorumlu Üye: Üye 3
	Aktörler: Sistem (Otomatik Tetiklenir), Takım Lideri
	Ön Koşullar: UC-02 kapsamında geçerli bir görev verisinin oluşturulmuş olması.
	Temel Akış:
	Sistem, görevin Kategori, Etki (1-5) ve Aciliyet (1-5) parametrelerini alır.
	Ağırlıklı algoritma ile Öncelik Skoru hesaplar (Örn: Kategori Security ise çarpan katsayısı artırılır).
	Hesaplanan skora göre görevi Kritik (P1), Yüksek (P2), Orta (P3) veya Düşük (P4) olarak sınıflandırır.
	Sınıfa karşılık gelen maksimum çözüm süresini (P1: 4 saat, P2: 24 saat, P3: 72 saat, P4: 168 saat) görevin oluşturulma zamanına ekleyerek SLA Bitiş Tarihini (Deadline) belirler.
	Alternatif / Hata Akışı (2a): Geçersiz bir parametre değeri (örn. aralık dışı sayı) gelirse sistem ValueError fırlatır ve işlemi güvenli varsayılan (P3) değerine çekerek uyarı logu yazar.
	Son Koşullar: Görevin öncelik seviyesi ve SLA hedef süresi veritabanına işlenir.
UC-04: Görev Durum İş Akışı (State Machine) ve Kalite Onay (Review) Mekanizması
	Sorumlu Üye: Üye 4
	Aktörler: Uzman (Assignee), Takım Lideri (Reviewer)
	Ön Koşullar: Görevin AÇIK veya İŞLEMDE durumunda olması.
	Temel Akış:
	Uzman, üzerinde çalıştığı görevi İŞLEMDE (IN_PROGRESS) durumuna alır.
	Çalışmayı bitirdiğinde çözüm açıklamasını ve harcanan süreyi girerek görevi KALİTE KONTROLÜNDE (IN_REVIEW) durumuna taşır (Uzman görevi doğrudan TAMAMLANDI yapamaz).
	Takım Lideri görevi inceler; kalite kriterlerini sağlıyorsa onaylayarak TAMAMLANDI (DONE) durumuna geçirir.
	Alternatif / Hata Akışı (3a - Kalite Reddi): Takım Lideri çözümü yetersiz bulursa ret gerekçesini yazar ve görevi REDDEDİLDİ / YENİDEN AÇILDI (REOPENED) durumuna çevirir; görevin "Yeniden İşleme (Rework) Sayacı" 1 artırılır.
	Son Koşullar: Görev yalnızca kalite onayından geçerek kapatılır ve kalite metriği güncellenir.
UC-05: SLA İhlal Tespiti, Eskalasyon ve Güvenlik/Denetim Loglama (Audit Trail)
	Sorumlu Üye: Üye 5
	Aktörler: Sistem, Güvenlik/Denetim Yöneticisi (Admin)
	Ön Koşullar: Sistemde aktif görevlerin ve kullanıcı işlemlerinin bulunması.
	Temel Akış:
	Sistem, aktif görevlerin mevcut zaman ile SLA Bitiş Tarihi (Deadline) arasındaki farkı kontrol eder.
	Süresi dolduğu halde TAMAMLANDI olmayan görevleri SLA İHLALİ (BREACHED) olarak işaretler ve üst yöneticiye eskalasyon uyarısı üretir.
	Sistemde gerçekleşen her durum değişikliği, yetki hatası ve SLA ihlali; Zaman Damgası, Kullanıcı ID, İşlem Tipi, Eski Değer ve Yeni Değer bilgileriyle değiştirilemez Denetim Günlüğüne (Audit Log) kaydedilir.
	Alternatif / Hata Akışı (2a): SLA süresinin dolmasına %20'den az süre kalmışsa sistem görevi RİSKLİ (AT_RISK)olarak işaretler.
	Son Koşullar: SLA ihlalleri görünür hale gelir ve tam izlenebilirlik (traceability) sağlanır.
UC-06: Departman ve Personel Performans / Kalite Metrikleri Analizi
	Sorumlu Üye: Üye 6
	Aktörler: Takım Lideri, Admin
	Ön Koşullar: Sistemde tamamlanmış veya işlem görmüş görev kayıtlarının bulunması.
	Temel Akış:
	Yönetici "Kalite ve Performans Analitiği" ekranını açar.
	Sistem; tamamlanan görev sayısı, SLA Uyum Oranı (%), İlk Seferde Doğru Yapma Oranı (First Time Right % - Rework görmeden kapanan görevler) ve ortalama çözüm süresini (MTTR) hesaplar.
	Hesaplanan metrikler departman ve personel bazında kalite skor kartı olarak ekranda gösterilir.
	Alternatif / Hata Akışı (2a): Seçilen dönemde hiç tamamlanmış görev yoksa sıfıra bölünme (ZeroDivisionError) hatasını önleyerek tüm metrikleri "Veri Yok (0%)" olarak güvenli şekilde döner.
	Son Koşullar: Kurumsal kalite durumu matematiksel metriklerle raporlanır.
UC-07: Gelişmiş Arama, Filtreleme ve Kurumsal Rapor Dışa Aktarma (Export)
	Sorumlu Üye: Üye 7
	Aktörler: Tüm Kullanıcılar
	Ön Koşullar: Kullanıcının oturum açmış olması.
	Temel Akış:
	Kullanıcı görev listesi ekranında Durum, Öncelik (P1-P4), Kategori, SLA Durumu veya Anahtar Kelime filtrelerini seçer.
	Sistem, SQL enjeksiyonuna karşı parametrik sorgular kullanarak eşleşen görevleri listeler.
	Kullanıcı "Raporu Dışa Aktar (CSV/JSON)" butonuna tıklar; sistem filtrelenmiş listeyi ve özet kalite istatistiklerini indirilebilir dosya olarak sunar.
	Alternatif / Hata Akışı (2a): Filtre kriterlerine uyan kayıt bulunamazsa kullanıcıya bilgilendirme mesajı gösterilir ve dışa aktarma butonu pasif hale getirilir.
	Son Koşullar: Kullanıcı aradığı görev verilerine ulaşır ve dışa aktarır.
4. Faz 1 İçin DIR Yöntemi ile YZ Kullanım Beyanı
DOCX+ 4
(Raporun 6. Bölümüne eklenecek olan Faz 1 DIR Beyanı - Paylaştığın sunumdaki formül ve kriterlere tam uyumlu):
DOCX+ 2
İş / Görev 1: Faz 1 - Proje Kapsamı, 7 Kişilik Görev Dağılımı ve Use Case Tasarımı
	Kullanılan YZ Aracı: Google Gemini
	Keşfet (D - Discover) [Puan: 5 / 5]: Üretim başlamadan önce yapay zekaya proje yönergesindeki tüm yapısal kısıtlamalar (7 kişilik ekip zorunluluğu, kişi başı en az 1 özgün Use Case, kopyala-yapıştır yasağı, ilerleyen fazlarda McCabe karmaşıklığı ve beyaz/kara kutu testlerine uygunluk gereksinimi) açıkça tanımlanmıştır. Konu olarak "Kurumsal Görev ve SLA Takip Sistemi" insan iradesiyle seçilmiş ve kabul kriterleri baştan belirlenmiştir.
DOCX+ 2
	Etkileş (I - Interact) [Puan: 4 / 5]: İlk aşamada 6 kişi üzerinden kurgulanan ekip taslağına müdahale edilerek ekip sayısı 7'ye çıkarılmış, her üyeye yazılım kalite yaşam döngüsüne (QA Lead, DevSecOps, Beyaz Kutu Test Uzmanı vb.) uygun spesifik roller atanması yönünde iteratif yönlendirme yapılmıştır. Use Case'lerin sadece basit CRUD işlemleri olmaması, Faz 4'te McCabe döngüsel karmaşıklık analizine veri sağlayacak algoritmik iş kuralları (dinamik SLA hesaplama, durum makinesi, rework sayacı) içermesi sağlanmıştır.
PDF+ 2
	Gözden Geçir (R - Review) [Puan: 5 / 5]: Üretilen 7 Use Case ve gereksinimler; IEEE 830 / ISO/IEC/IEEE 29148 gereksinim mühendisliği standartlarına göre (belirsizlikten uzak olma, test edilebilirlik, izlenebilirlik) ekipçe incelenmiştir. Her Use Case'in alternatif/hata akışlarının Faz 4'teki sınır değer ve kara kutu testlerine doğrudan girdi oluşturduğu doğrulanmıştır.
PDF+ 2
	DIR Puan Hesaplaması:
DIR%=(D×I×R)×0.8=(5×4×5)×0.8=100×0.8=80.0%

DIR%=(D×I×R)×0.8=(5×4×5)×0.8=100×0.8=80.0%
(Teşhis Matrisi Karşılığı: Senaryo B - İnsan Gözetimli Yazılım Mühendisliği, R=5≥4 Veto Kuralı başarılı).
