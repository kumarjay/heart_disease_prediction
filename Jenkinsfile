pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            sudo docker {
                    image 'python:3.5.1' 
            }}
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


