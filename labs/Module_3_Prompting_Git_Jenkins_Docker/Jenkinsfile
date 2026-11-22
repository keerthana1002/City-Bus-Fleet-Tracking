pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }
        stage('Run Arrival Time Estimator Prototype') {
            steps {
                sh 'python3 src/arrival_estimator.py'
                sh 'python3 src/fleet_simulator.py'
            }
        }
        stage('Run Automated Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }
    post {
        always {
            echo 'Build completed for Case 28: City Bus Fleet Tracking (600 Buses)'
        }
    }
}
