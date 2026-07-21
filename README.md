# InfraWatch

A real-time system monitoring dashboard built using Flask, psutil, and Docker.

## Overview

InfraWatch is a lightweight web application that monitors system resources in real time. It displays CPU, memory, disk, network, and system information through a clean web dashboard while exposing the data through a REST API.

## Features

- Real-time CPU monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network statistics
- System information
- Top CPU-consuming processes
- REST API for live system metrics
- Dockerized deployment

## Tech Stack

- Python
- Flask
- psutil
- HTML
- CSS
- JavaScript
- Docker
- Git
- GitHub

## Screenshots

### Running on Windows

![Windows Dashboard](assets/dashboard-windows.png)

### Running inside Docker

![Docker Dashboard](assets/dashboard-docker.png)

## Project Structure

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

## Getting Started

### Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```
http://127.0.0.1:5000
```

### Run with Docker

Build the Docker image:

```bash
docker build -t infrawatch .
```

Run the container:

```bash
docker run -p 5000:5000 infrawatch
```

Open:

```
http://localhost:5000
```

## Future Improvements

- Historical performance graphs
- Email alert notifications
- User authentication
- Multi-host monitoring
- Export system metrics

## Author

**Prachi Janwadkar**
