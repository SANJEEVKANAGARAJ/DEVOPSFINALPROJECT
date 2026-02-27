# DevOps Pipeline Explorer

An interactive static website that documents our CI/CD pipeline journey — built, containerized, and deployed using the very pipeline it describes.

## Project Overview

This project is our DevOps Final Assignment for PSG College of Technology. We created a beautiful static website that explains the DevOps process itself including pipeline stages, Docker containerization, Git workflows, and cloud deployment. The website is automatically built and deployed using the exact CI/CD pipeline it documents.

## System Architecture

The core architecture follows a modern CI/CD flow:
1. Source Code: Managed in GitHub
2. Continuous Integration: Jenkins Server automates the workflow
3. Container Registry: Docker Hub stores the application images
4. Deployment: AWS EC2 instance pulls and runs the containers

## Team Members and Roles

### Sanjeev K
Role: Jenkins & CI Orchestration
- Jenkins pipeline creation and configuration
- Jenkinsfile stage management
- Continuous Integration triggers from GitHub
- Build and test stage implementation

### Ratnesh
Role: AWS Cloud & Deployment
- AWS EC2 cloud instance setup and configuration
- SSH-based deployment automation
- Container runtime management (Docker)
- System architecture documentation and design

### Pranav
Role: Docker & Containerization
- Dockerfile creation and optimization
- Docker image build and push processes
- Container vs Virtual Machine technical analysis
- Tools and technologies documentation

### Gokul Krishna
Role: CI/CD Automation & Documentation
- CI/CD automation logic and explanation
- User stories definition and validation
- Team profiles and project documentation
- Frontend animations and visual enhancements

## Project Components

### Frontend Dashboard
A modern, responsive dashboard built with HTML and CSS that serves as the central hub for the documentation.

### Pipeline Details
A dedicated section and page explaining the Jenkins CI/CD stages:
- Clone Stage: Pulling code from GitHub
- Build Stage: Verifying application integrity
- Docker Stage: Packaging into images
- Deploy Stage: Running on AWS Cloud

### Tools and Technologies
Comprehensive documentation of the tech stack:
- GitHub: Version Control
- Jenkins: Automation Server
- Docker: Containerization
- Docker Hub: Image Registry
- AWS EC2: Cloud Infrastructure
- Nginx: High-performance Web Server

## How to Run Locally

You can run this application instantly on any machine with Docker installed:

docker run -d -p 80:80 sanjeevrk4145/student-app

Once running, access the dashboard at http://localhost

## Git Workflow Guidelines

We maintain high code quality through a structured Git process:
- Feature Branching: Every new task is developed in a separate branch
- Pull Requests: Mandatory peer review for all changes
- Automated CI: Every merge triggers a full Jenkins pipeline run
- Direct Pushes: Prohibited on the main branch to ensure stability
