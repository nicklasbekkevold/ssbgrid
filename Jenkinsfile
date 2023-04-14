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
                withPythonEnv('python') {
                    echo ${SHELL}
                    echo python --version
                    [ -d .venv ] && rm -rf .venv
                    python -m venv .venv

                    .venv/Scripts/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
                    pip install -r requirements_dev.txt
                }
            }
        }

        stage('Check style') {
            steps {
                withPythonEnv('python') {
                    #. .venv/bin/activate
                    black --check .

                    isort --check --profile black .

                    ruff check .
                }
            }
        }

        stage('Unit tests') {
            steps {
                #. venv/bin/activate
                pytest
            }
        }

        stage('Cleanup') {
            steps {
                rm -rf venv
            }
        }
    }
}
