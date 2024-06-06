pipeline{
    agent any

    stages{
        stage('Test'){
            steps{
                sh '''
                . /shared_data/python_env/pytest_venv/bin/activate
                pytest test.py --junitxml=test-reports/app_test.xml
                '''
            }
        }
    }
    post{
        always{
            junit 'test-reports/app_test.xml'
        }
    }
}
