pipeline {
  agent any
  stages {
    stage('Install dependencies and run tests in Python container') {
      steps {
        script {
          docker.image('python:3.11').inside('-u 0:0') {
            sh 'python -V'
            sh 'python -m venv venv'
            sh './venv/bin/pip install --upgrade pip'
            sh './venv/bin/pip install -r requirements.txt'
            sh './venv/bin/pytest --junitxml=report.xml || true'
          }
        }
      }
      post {
        always {
          junit 'report.xml'
        }
      }
    }
  }
}

