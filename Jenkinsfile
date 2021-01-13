pipeline {
  agent any
  stages {
    stage('t1') {
      steps {
        sh 'echo 123'
      }
    }

    stage('t2') {
      steps {
        build 't1'
      }
    }

  }
}