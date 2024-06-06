pipeline{
    agent any

    stages{
        stage('Test'){
            steps{
                sh '''
                ls /shared_data/python_env/pytest_venv/bin/
                source /shared_data/python_env/pytest_venv/bin/activate
                pytest --version
                python3 test.py
                '''
            }
        }
    }
}