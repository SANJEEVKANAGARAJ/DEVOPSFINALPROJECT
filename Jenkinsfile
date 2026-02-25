pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "sanjeevrk4145/student-app"
        SERVER_IP = "16.171.208.10"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/SANJEEVKANAGARAJ/DEVOPSFINALPROJECT.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t sanjeevrk4145/student-app .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push sanjeevrk4145/student-app'
            }
        }

        stage('Deploy to Cloud') {
            steps {

                sh '''
                ssh ubuntu@$SERVER_IP << EOF
                docker pull sanjeevrk4145/student-app

                docker stop student-app || true
                docker rm student-app || true

                docker run -d -p 80:80 --name student-app sanjeevrk4145/student-app

                EOF
                '''
            }
        }

    }
}