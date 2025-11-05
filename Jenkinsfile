pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }
        stage('Run tests with coverage') {
            steps {
                sh 'pytest --junitxml=report.xml --cov=src --cov-report=html --cov-report=term || true'
            }
        }
        stage('Publish Report') {
            steps {
                junit 'report.xml'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
}
