# Digit AI App

A lightweight AI-powered web application built using **Flask** and **TensorFlow** that predicts handwritten digits or alphanumeric characters from uploaded `.png` images.

Containerized with **Docker**  
Scalable with **Kubernetes**

---

## Features

- Upload `.png` images via a simple web interface  
- Predict digits or characters using a trained TensorFlow model  
- Containerized for consistent and isolated environments  
- Ready for scalable deployment using Kubernetes

---

## Local Testing (Without Docker)

To run the app locally:

```bash
git clone https://github.com/yourusername/digit-ai-app.git
cd digit-ai-app
pip install -r requirements.txt
python app.py


## Docker Setup

Follow these steps to containerize and run the application using Docker:

### Step 1: Build the Docker Image

Run this command in the project root (where the `Dockerfile` is located):

```bash
docker build -t digit-ai-app .


