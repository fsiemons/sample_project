pipeline{
    agent any

    stages{
        stage('Test'){
            steps{
                sh '''
                . /shared_data/python_env/pytest_env/bin/activate
                pytest --version
                python3 test.py
                '''
            }
        }
    }
}