pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sanjeevrk4145/student-app"
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop student-app || true
                docker rm student-app || true
                docker run -d -p 80:80 --name student-app $DOCKER_IMAGE
                '''
            }
        }

    }
}