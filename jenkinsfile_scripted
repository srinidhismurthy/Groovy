node {
    def venvDir = "env" // Directory for the virtual environment

    // Trigger the build on changes pushed to the repository
    properties([
        pipelineTriggers([pollSCM('H/5 * * * *')]) // Poll every 5 minutes
    ])

    try {
        stage('Checkout Code') {
            echo 'Checking out code from repository...'
            checkout scm
        }

        stage('Setup Python Environment') {
            echo 'Setting up Python virtual environment...'
            sh "python3 -m venv ${venvDir}"
            sh "./${venvDir}/bin/pip install -r requirements.txt"
        }

        stage('Run Selenium Tests') {
            echo 'Running Selenium tests...'
            sh "./${venvDir}/bin/python test_google_search.py"
        }
    } catch (Exception e) {
        echo "Pipeline failed: ${e.message}"
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        stage('Cleanup') {
            echo 'Cleaning up virtual environment...'
            sh "rm -rf ${venvDir}"
        }
    }
}
