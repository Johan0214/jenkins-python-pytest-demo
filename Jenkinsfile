pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
        stage('Publish Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
