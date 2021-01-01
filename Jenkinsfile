pipeline {
    agent any
    
    stages {
        stage('build') {
            docker {
                    image 'python:2-alpine' 
                }
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


