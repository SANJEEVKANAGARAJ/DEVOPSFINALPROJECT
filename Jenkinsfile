pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "sanjeevrk4145/student-app"
        SERVER_IP = "16.171.208.10"
    }

    stages {

        stage('Clone') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/SANJEEVKANAGARAJ/DEVOPSFINALPROJECT.git'
                )
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy to Cloud') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@$SERVER_IP << EOF

                docker pull $DOCKER_IMAGE

                docker stop student-app || true
                docker rm student-app || true

                docker run -d -p 80:80 --name student-app $DOCKER_IMAGE

                EOF
                '''
            }
        }

    }
}