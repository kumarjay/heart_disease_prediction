pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'sudo python:3'
            }}
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


