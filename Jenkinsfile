#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 10, unit: 'MINUTES')
    }

    environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/.venv"
    }

    stages {
        stage('Install requirements') {
            steps {
                withPythonEnv('python3.9') {
                    sh """
                        echo ${SHELL}
                        sh 'python3 --version'
                        sh 'python --version'
                        [ -d .venv ] && rm -rf .venv
                        #virtualenv --python=python3 .venv
                        virtualenv .venv

                        #. .venv/bin/activate
                        export PATH=${VIRTUAL_ENV}/bin:${PATH}
                        pip install --upgrade pip
                        pip install -r requirements_dev.txt
                    """
                }
            }
        }

        stage('Check style') {
            steps {
                withPythonEnv('python3.9') {
                    sh '''
                        #. .venv/bin/activate
                        black --check .
                    '''

                    sh '''
                        isort --check --profile black .
                    '''

                    sh '''
                        ruff check .
                    '''
                }
            }
        }

        stage('Unit tests') {
            steps {
                sh """
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pytest
                """
            }
        }

        stage('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
        }
    }
}
