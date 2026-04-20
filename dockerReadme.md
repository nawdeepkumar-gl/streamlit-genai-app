#  Streamlit GenAI App — Docker Setup Guide

This guide provides step-by-step instructions to install Docker and run the Streamlit GenAI application using Docker.

---

#  Prerequisites

* Windows 10/11 (64-bit)
* WSL2 enabled
* Ubuntu (or any Linux distro in WSL)
* Python (optional for local testing)

---

#  Step 1: Install Docker Desktop

1. Download Docker Desktop from:
   👉 https://www.docker.com/products/docker-desktop/

2. Install and launch **Docker Desktop**

3. During installation:

   * Enable **WSL 2 integration**
   * Restart your system if prompted

---

#  Step 2: Verify Docker Installation

Open WSL terminal and run:

```bash
docker version
```

If you see **Client + Server**, Docker is working.

---

#  Step 3: Fix Permission Issue (WSL)

If you get permission errors, run:

```bash
sudo usermod -aG docker $USER
```

Then restart WSL from Windows PowerShell:

```bash
wsl --shutdown
```

Reopen WSL and verify again:

```bash
docker version
```

---

#  Step 4: Project Setup

Navigate to your project directory:

```bash
cd /mnt/d/streamlit-genai-app
```

---

#  Step 5: Create Dockerfile

Create a file named `Dockerfile` and add:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

#  Step 6: Create requirements.txt

Generate dependencies:

```bash
pip freeze > requirements.txt
```

---

#  Step 7: Build Docker Image

```bash
docker build -t streamlit-genai-app .
```

---

#  Step 8: Run the Application

```bash
docker run -p 8501:8501 streamlit-genai-app
```

---

#  Step 9: Access the App

Open your browser:

👉 http://localhost:8501

---

# ⚠️ Common Issues & Fixes

###  Docker not running

* Start **Docker Desktop**

###  Permission denied

```bash
newgrp docker
```

###  App not loading

* Check logs in terminal
* Verify `app.py` exists
* Ensure dependencies are in `requirements.txt`

---

#  Project Structure

```
streamlit-genai-app/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md
```

---

#  Future Enhancements

* Add FastAPI backend
* Integrate RAG pipeline
* Use Docker Compose (multi-container setup)
* Deploy to cloud (Azure / AWS)

---

