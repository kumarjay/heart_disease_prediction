pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'python:3'
            }}
            steps {
                sh 'python -m app.py'
                echo "Hello World"
            }
        }
    }
}


