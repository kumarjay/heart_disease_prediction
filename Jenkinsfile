pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'python:3'
                    image "docker build -t flask-app ."
                    image "docker run -it -p 8000:8000 flask-app"
            }}
            steps {
                //sh 'python -m app.py'
                echo "Hello World"
            }
        }
    }
}


