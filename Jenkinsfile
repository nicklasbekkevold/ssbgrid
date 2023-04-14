#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
 pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/.venv"
    }

    stages {

        /*
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        */

        stage ('Install requirements') {
            steps {
                sh """
                    echo ${SHELL}
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

        stage ('Check style') {
            steps {
                sh """
                    #. .venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    black --check .
                """
                sh """
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    isort --check --profile black .
                """
                sh """
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    ruff check .
                """
            }
        }

        stage ('Unit tests') {
            steps {
                sh """
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pytest
                """
            }
        }

        stage ('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
        }
    }
}
