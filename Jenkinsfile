pipeline {
    agent any
    
    stages {
        stage('build') {
            agent{
            docker {
                    image 'sudo docker build . -t abc/xyz'
            }}
            steps {
                //sh 'python --version'
                echo "Hello World"
            }
        }
    }
}


