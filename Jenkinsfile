pipeline {
  agent any
  stages {
    stage('Install dependencies (Python 3.11 in Docker)') {
      agent {
        docker {
          image 'python:3.11'
          args '-u 0:0'
        }
      }
      steps {
        sh 'python -V'
        sh 'python -m venv venv'
        sh './venv/bin/pip install --upgrade pip'
        sh './venv/bin/pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
      agent {
        docker {
          image 'python:3.11'
          args '-u 0:0'
        }
      }
      steps {
        sh './venv/bin/pytest --junitxml=report.xml'
      }
      post {
        always {
          junit 'report.xml'
        }
      }
    }
  }
}
