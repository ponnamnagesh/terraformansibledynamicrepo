pipeline {
    agent any
    
    stages {
        //stage ('s3 - create bucket') {
          //  steps {
               // sh ('ansible-playbook s3-bucket.yml')
             //}
       //}
        stage('Checkout') {
            steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/QA']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ponnamnagesh/terraformansibledynamicrepo.git']]])            
              //git([url: 'git@github.com:ponnamnagesh/TerraformJenkinsS3Ansible.git', branch: 'main', credentialsId: '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'])

          }
        }    
        stage ("Terraform Init") {
            steps {
                //sh ('cd terraform-aws-ansible-engine/')
                //sh ('sudo terraform init') 
                sh ('terraform version && terraform init -input=false')
            }
        }
        stage ("Terraform Plan") {
            steps {
                //sh ('cd terraform-aws-ansible-engine/')
                sh ('sudo terraform plan') 
            }
        }
        stage ("Terraform Validate") {
            steps {
                //sh ('cd terraform-aws-ansible-engine/')
                sh ('sudo terraform validate -json') 
            }
        }
        stage ("Terraform Action") {
            steps {
                //sh ('cd terraform-aws-ansible-engine/')
                echo "Terraform action is --> ${action}"
                sh ('sudo terraform ${action} --auto-approve') 
           }
        }
    }
        }
    
