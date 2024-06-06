pipeline{
    agent any

    stages{
        stage('Test'){
            steps{
                sh '''
                source /shared_data/python_env/pytest_venv/bin/activate
                pytest --version
                python3 test.py
                '''
            }
        }
    }
}