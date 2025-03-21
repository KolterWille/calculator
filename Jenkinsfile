pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage ("unit tests") {
            steps {
                sh "python3 test_calculator.py"
            }
        }
    }
}