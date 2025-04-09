pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/Tamizh2R/DR_project.git', branch: 'main'
            }
        }

        stage('Generate Terraform Config') {
            steps {
                sh 'python3 generate_terraform.py'
            }
        }

        stage('Terraform Init') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'AWS Credentials', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }
    }
}

