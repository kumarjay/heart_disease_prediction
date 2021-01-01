pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'python:3'
                    //image "docker build -t flask-app ."
                    //image "sudo docker run -p 8000:8000 --name flask-app -d flask-app"
            }}
            steps {
                sh "sudo docker build -t flask-app ."
                sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app"
                //sh 'python -m app.py'
                echo "Hello World"
            }
        }
    }
}


