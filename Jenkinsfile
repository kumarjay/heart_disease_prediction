pipeline {
    //agent any
    agent { docker { 
        sudo chmod 666 /var/run/docker.sock
        image 'python:3.5.1' 
    } }
    stages {
        stage('build') {
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


