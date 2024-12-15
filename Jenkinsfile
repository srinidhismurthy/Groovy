pipeline {
    agent any

    environment {
        VENV_DIR = "$HOME/Srinidhi/env" // Directory for the virtual environment
    }

    triggers {
        pollSCM('H/5 * * * *') // Poll Git repository every 5 minutes for changes
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create a Python virtual environment
                    sh 'python3 -m venv ${VENV_DIR}'
                    
                    // Install dependencies from requirements.txt
                    sh './${VENV_DIR}/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Run the Selenium test script
                    sh './${VENV_DIR}/bin/python test_google.py'
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Cleaning up: Removing virtual environment..."
                
                // Remove the virtual environment directory
                sh "rm -rf ${VENV_DIR}"
            }
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
