pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages ("unit tests") {
        steps {
            sh "python3 test_calculator.py"
        }
    }
}
