pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test') {
      steps {
        sh 'node --version'
        sh 'svn --version'
        sh 'hostname'
      }
    }

    stage('prod') {
      steps {
        pwd(tmp: true)
        sh 'uname -r'
        sh 'hostname'
      }
    }

  }
}