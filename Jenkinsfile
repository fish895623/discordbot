pipeline {
  agent { docker: "fish895623/ddocker:latest" }
  stages {
    stage('Build image') {
      steps {
        echo 'Starting to build docker image'
        script {
          def customImage = docker.build("my-image:${env.BUILD_ID}")
          customImage.push()
        }
      }
    }
  }
}
