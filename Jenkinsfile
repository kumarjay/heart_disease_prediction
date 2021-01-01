pipeline {
    //agent any
    agent { docker { 
        image 'python:3' 
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


