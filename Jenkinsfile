
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        DOCKER = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip install --upgrade pip'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
                bat '"%PYTHON%" -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" --version'
                bat '"%DOCKER%" build -t medibot:jenkins .'
            }
        }
    }

    post {
        success {
            echo 'MediBot Pipeline Completed Successfully!'
        }
        failure {
            echo 'MediBot Pipeline Failed. Check Console Output.'
        }
    }
}
