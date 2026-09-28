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

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t devops-flask-app:latest .'
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

                    bat 'echo %DOCKER_PASSWORD% | "C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" login -u %DOCKER_USERNAME% --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" tag devops-flask-app:latest siddharthpingle7030/devops-flask-app:latest'

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" push siddharthpingle7030/devops-flask-app:latest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker container...'

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" stop devops-flask-app || exit 0'

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm devops-flask-app || exit 0'

                bat '"C:\\Users\\acer\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d -p 5000:5000 --name devops-flask-app devops-flask-app:latest'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}