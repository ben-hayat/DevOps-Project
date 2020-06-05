pipeline {
   agent any
   stages {
      stage('Checkout') {
         steps {
		 // should i cd to specific directory ?
            bat 'git clone https://github.com/ben-hayat/DevOps-Project.git'
         }
      }
      stage ('Build') {
         steps {
            bat 'docker build . -t flask_p'
         }
      }
      stage('Run') {
         steps {
            bat 'docker-compose up -d'
         }
      }
      stage('Test') {
         steps {
            bat 'python tests\\ete.py'
         }
      }
	  stage('Finalize') {
         steps {
            bat 'docker-compose dowb move'
         }
      }
   }
}