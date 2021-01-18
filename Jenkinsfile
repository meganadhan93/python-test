pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
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
