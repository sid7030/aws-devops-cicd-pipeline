pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running application tests...'
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t devops-flask-app:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                echo 'Logging in to Docker Hub...'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                }
            }
        }

        stage('Push Docker Image') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    bat 'docker tag devops-flask-app:latest %DOCKER_USERNAME%/devops-flask-app:latest'

                    bat 'docker push %DOCKER_USERNAME%/devops-flask-app:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage completed.'
            }
        }
    }

    post {
        success {
            echo '========================================='
            echo 'CI/CD PIPELINE SUCCESSFUL'
            echo '========================================='
        }

        failure {
            echo '========================================='
            echo 'CI/CD PIPELINE FAILED'
            echo '========================================='
        }
    }
}