pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test') {
      steps {
        sh 'node --version'
        sh 'svn --version'
        sh '''docker ps
docker images'''
      }
    }

  }
}