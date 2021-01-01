pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'python:3'
            }}
            steps {
                sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


