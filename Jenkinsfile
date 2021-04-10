pipeline {
  agent any
  environment {
    REGIS_TOKEN = credentials('ghcr')
  }
  stages {
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