pipeline {
  agent any
  environment {
    REGIS_TOKEN = credentials('ghcrio')
    imagename = 'ghcr.io/fish895623/my-image'
    registryCredential = 'ghcrio'
    Docker_Image = ''
  }
  stages {
    stage('Build image') {
      steps {
        echo 'Starting to build docker image'
        script {
          Docker_Image = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps {
        echo 'abcd'
        script {
          docker.withRegistry('https://ghcr.io/', registryCredential) {
            Docker_Image.push("$BUILD_NUMBER")
            Docker_Image.push('latest')
          }
        }
      }
    }
  }
}
