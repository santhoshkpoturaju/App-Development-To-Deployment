# App-Development-To-Deployment

![Project Overview](./tutorial/overivew.png)

---

## Overview

This project demonstrates the complete workflow of developing, testing, containerizing, and deploying a sample application using modern DevOps tools and practices. It is designed to help you get hands-on experience with application development, containerization, CI/CD automation, and Kubernetes deployment.

### Project Goals

- **Develop** a sample application and understand the basics of app development.
- **Test** the application locally using Docker or Podman containers.
- **Automate** image building and pushing to a registry using GitHub Actions.
- **Deploy** the containerized application to Kubernetes using ArgoCD.

---

## 1. Lab Setup Using This Repo

### Clone the Repository

```bash
git clone https://github.com/<your-username>/App-Development-To-Deployment.git
cd App-Development-To-Deployment
```

### Prerequisites

- Python 3
- pip
- Podman

### Configure Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

---

## 2. Django Project Setup

Install Django:

```bash
pip install django
```

Start a new Django project:

```bash
django-admin startproject sampleapp .
```

Create a new Django app:

```bash
python3 manage.py startapp helloworldsite
```

Run the development server:

```bash
python3 manage.py runserver
```

Access the app at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 3. Containerize with Podman

Build the container image:

```bash
podman build -t sampleapp .
```

Run the container:

```bash
podman run -d -p 8000:8000 sampleapp
```

Access the app in your browser:  
[http://localhost:8000/](http://localhost:8000/)

---

## 4. CI/CD and Deployment

- Use **GitHub Actions** to automate building and pushing the container image.
- Deploy the application to **Kubernetes** using **ArgoCD** for continuous delivery.

Refer to the repository documentation and workflow files for more details on