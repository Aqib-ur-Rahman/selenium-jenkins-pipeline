pipeline {
    agent {
        docker {
            image 'python:3.11-slim'  // Use Python Docker image
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Aqib-ur-Rahman/selenium-jenkins-pipeline.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python test_selenium.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
