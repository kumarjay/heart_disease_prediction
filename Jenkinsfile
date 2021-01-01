pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    sudo image 'python:3.5.1' 
            }}
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


