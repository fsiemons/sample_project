pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                git 'https://github.com/fsiemons/sample_project.git'
            }
        }
        stage('Test'){
            steps{
                sh 'python3 test.py'
            }
        }
    }
}