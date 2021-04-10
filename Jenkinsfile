pipeline {
  agent any
  stages {
    stage('Set Variables') {
      steps {
        script {
          withCredentials([string(credentialsId: 'ghcr', variable: 'REGIS_TOKEN')])
        }
    stage('Build image') {
      steps {
        echo 'Starting to build docker image'
        script {
          docker.withRegistry('ghcr.io', '$REGIS_TOKEN') {
            def customImage = docker.build("ghcr.io/fish895623/my-image:${env.BUILD_ID}")
            customImage.push()
          }
        }
      }
    }
  }
}
