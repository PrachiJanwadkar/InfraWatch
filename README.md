# 🚀 InfraWatch

A real-time system monitoring dashboard built using **Flask**, **psutil**, and **Docker**.

## ✨ Features

- 📊 Live CPU Monitoring
- 💾 Memory Monitoring
- 💽 Disk Monitoring
- 🌐 Network Statistics
- 🖥️ System Information
- 🔥 Top CPU Processes
- ⚡ REST API for Live Updates
- 🐳 Dockerized Deployment

---

## 🛠️ Tech Stack

- Python
- Flask
- psutil
- HTML
- CSS
- JavaScript
- Docker
- Git
- GitHub

---

## 📷 Screenshots

### Running on Windows

![Windows Dashboard](assets/dashboard-windows.png)

### Running inside Docker

![Docker Dashboard](assets/dashboard-docker.png)

---

## 📂 Project Structure

```text
InfraWatch/
├── app.py
├── system_monitor.py
├── Dockerfile
├── requirements.txt
├── README.md
├── assets/
├── static/
└── templates/
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🐳 Run with Docker

```bash
docker build -t infrawatch .
docker run -p 5000:5000 infrawatch
```

Open:

```
http://localhost:5000
```

---

## 📌 Future Improvements

- Historical graphs
- Email alerts
- Authentication
- Multi-host monitoring

---

## 👩‍💻 Author

**Prachi Janwadkar**