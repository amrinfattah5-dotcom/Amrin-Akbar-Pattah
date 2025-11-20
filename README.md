# Amrin-Akbar-Pattah
UTS Komputasi Pararel pada computing

## Soal 1
**Jelaskan keterkaitan antara SaaS, PaaS, dan IaaS dalam cloud computing**
**jawaban**
SaaS, PaaS, dan IaaS adalah tiga model layanan dalam cloud computing yang tersusun secara bertingkat:

- **IaaS (Infrastructure as a Service)**: menyiapkan pondasi Infrastruktur — VM, storage, jaringan. Pengguna mengelola OS, runtime, aplikasi.
Level paling dasar dalam cloud.
kemudian Menyediakan sumber daya infrastruktur seperti:
- Server virtual
- Storage
- Jaringan
- Sistem operasi
- Pengguna bertanggung jawab atas instalasi software, runtime, dan aplikasi.
- Contoh: AWS EC2, Google Compute Engine, Azure VM.
  
- **PaaS (Platform as a Service)**: berada di atas IaaS; menyediakan platform (runtime, database, build tools) yang memudahkan developer membangun dan menjalankan aplikasi tanpa mengelola infrastruktur. Berada di atas IaaS.
- Menyediakan platform pengembangan:
- Tools developer
- Database
- Runtime environment
- Framework aplikasi
- Developer tinggal fokus membuat aplikasi, tanpa mengelola server atau OS.
- Contoh: Google App Engine, Heroku, AWS Elastic Beanstalk.

- **SaaS (Software as a Service)**: lapisan aplikasi siap-pakai yang dijalankan di atas platform/infrastruktur tadi — pengguna akhir hanya menggunakan aplikasi melalui web/klien.
- Level paling atas
- Merupakan aplikasi jadi yang bisa langsung digunakan pengguna melalui internet.
- Contoh: Gmail, Google Drive, Microsoft 365, Zoom.
[SaaS] <-- aplikasi siap pakai
[PaaS] <-- platform & runtime
[IaaS] <-- server, storage, network


## soal 2
**Gambarkan diagram yang menunjukkan keterkaitan antara cloud native app teknologi container, PaaS, dan SaaS.**

          ┌──────────────────────────┐
          │        IaaS Layer        │
          │ (VM, Network, Storage)   │
          └─────────────┬────────────┘
                        │
                        ▼
          ┌──────────────────────────┐
          │        PaaS Layer        │
          │  - Kubernetes / Orches.  │
          │  - Container Registry    │
          │  - Managed Database      │
          └─────────────┬────────────┘
                        │
                        ▼
     ┌──────────────────────────────────────┐
     │       Cloud Native Application       │
     │  - Docker / OCI Containers           │
     │  - Microservices Architecture        │
     │  - Service Mesh / Sidecar            │
     └────────────────────┬─────────────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │         SaaS           │
             │ Aplikasi Web / Mobile │
             │   Dipakai End-User     │
             └────────────────────────┘


## soal 3
**Buat 2 workspace menggunakan uv. Workspace 1 menggunakan Python 3.14 free-threaded dan 1 lagi menggunakan Python 3.14 (GIL-enabled). buat 2 program yang akan dieksekusi di masing-masing workspace tersebut (2 program yang sama di setiap workspace). 2 program tersebut merupakan program untuk mengambil data JSON dari suatu endpoint. Program 1 menggunakan asyncio (async-http), sementara program satunya lagi menggunakan multiprocessing untuk pemrograman paralel. Bandingkan waktu yang diperlukan untuk mengakses JSON endpoint tersebut. Tulis hasil tersebut pada README.md pada setiap workspace.**








