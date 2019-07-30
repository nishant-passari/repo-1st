pipeline {
    agent any
        stages {
        stage('build') {
            steps {
                sh 'python3 my_script.py'
                sh 'python3 plus_pattern.py 5'
            }
        }
    }
}
