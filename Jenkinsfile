pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage ("unit tests") {
            steps {
                sh "python test_calculator.py"
            }
        }
    }
}