pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/username/student-app.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-app .'
            }
        }

        stage('Docker Image') {
            steps {
                sh 'docker push yourdockerhubusername/student-app'
            }
        }

    }
}