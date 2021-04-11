pipeline {
  agent any
  environment {
    REGIS_TOKEN = credentials('ghcrio')
  }
  stages {
    stage('Build image') {
      steps {
        echo 'Starting to build docker image'
        script {
          Docker_Image = docker.build("ghcr.io/fish895623/my-image:${env.BUILD_ID}")
        }
      }
    }
    stage('Deploy Image') {
      steps {
        echo 'abcd'
        script {
          docker.withRegistry('https://ghcr.io/', REGIS_TOKEN) {
            Docker_Image.push('latest')
          }
        }
      }
    }
  }
}
