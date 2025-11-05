pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u 0:0'
    }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'python -m venv venv'
        sh './venv/bin/pip install --upgrade pip'
        sh './venv/bin/pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
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

