# 🚀 DevOps Pipeline Explorer

> **An interactive static website that documents our CI/CD pipeline journey — ironically built, containerized, and deployed using the very pipeline it describes.**

![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-Pipeline-D24939?logo=jenkins&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Alpine-009639?logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=githubactions&logoColor=white)

---

## 📖 About

This project is our **DevOps Final Assignment** for PSG College of Technology. Instead of building a traditional app, we built a beautiful static website that explains **the DevOps process itself** — pipeline stages, Docker containerization, Git workflows, and cloud deployment.

**The irony?** This website is built, packaged, and deployed using the exact CI/CD pipeline it describes. 😏

---

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   GitHub     │────▶│   Jenkins   │────▶│  Docker Hub  │────▶│   AWS EC2   │
│  (Source)    │     │  (CI/CD)    │     │  (Registry)  │     │  (Deploy)   │
└─────────────┘     └─────────────┘     └──────────────┘     └─────────────┘
```

---

## 🐳 Quick Start with Docker

Pull and run the app with a single command:

```bash
docker pull sanjeevrk4145/student-app:latest
docker run -d -p 80:80 sanjeevrk4145/student-app
```

Then open **http://localhost** in your browser.

---

## 📂 Project Structure

```
DEVOPSFINALPROJECT/
├── frontend/
│   └── index.html          # Static website (single page)
├── .github/
│   └── workflows/
│       └── pipeline.yml    # GitHub Actions CI/CD workflow
├── Dockerfile              # Container build instructions
├── Jenkinsfile             # Jenkins pipeline definition (4 stages)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## ⚙️ CI/CD Pipeline Stages

Our pipeline runs automatically on every push to `main`:

| Stage | Description |
|-------|-------------|
| **1. Clone** | Jenkins clones the latest code from GitHub |
| **2. Build** | Docker builds the image using our Dockerfile |
| **3. Push** | Image is pushed to Docker Hub public registry |
| **4. Deploy** | SSH into EC2, pull image, and run the container |

---

## 🔄 Git Workflow

We follow a **branch-based workflow** with mandatory pull requests:

1. Create a **feature branch** from `main`
2. Make changes and **commit** with meaningful messages
3. Open a **Pull Request** for code review
4. After approval, **merge** to `main`
5. Pipeline **auto-triggers** on merge → builds → deploys

> ⚠️ Direct pushes to `main` are not allowed. All code promotion happens through PRs.

---

## 📋 User Stories

| # | User Story | Status |
|---|-----------|--------|
| 1 | As a visitor, I want to see an overview of the DevOps pipeline | ✅ Done |
| 2 | As a visitor, I want to understand each CI/CD stage | ✅ Done |
| 3 | As a visitor, I want to see the tools and technologies used | ✅ Done |
| 4 | As a visitor, I want to view the actual Dockerfile | ✅ Done |
| 5 | As a visitor, I want to understand the Git workflow | ✅ Done |
| 6 | As a visitor, I want to see the assignment checklist | ✅ Done |
| 7 | As a visitor, I want to know the team members and their roles | ✅ Done |
| 8 | As a visitor, I want to copy the docker run command easily | ✅ Done |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **HTML/CSS/JS** | Static website |
| **Nginx (Alpine)** | Lightweight web server |
| **Docker** | Containerization |
| **Jenkins** | CI/CD pipeline |
| **GitHub Actions** | Alternative CI/CD |
| **Docker Hub** | Container registry |
| **AWS EC2** | Cloud deployment |

---

## 👥 Team

| Member | Role | Responsibilities |
|--------|------|-----------------|
| **Sanjeev K** | DevOps & Infrastructure | EC2 setup, Jenkins, Jenkinsfile, Docker Hub, SSH deploy |
| **Sratn** | Application & CI/CD | Website development, Dockerfile, GitHub Actions, docs |
| **Team Member 3** | QA & Documentation | User stories, testing, PR reviews, documentation |

---

## 📄 License

This project is created for educational purposes as part of the DevOps course at PSG College of Technology.
