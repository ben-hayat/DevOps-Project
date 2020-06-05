pipeline {
   agent any
   stages {
      stage('Checkout') {
         steps {
			//bat 'echo skip clone until sucess'
            bat 'git clone https://github.com/ben-hayat/DevOps-Project.git DevOps'
         }
      }
      stage ('Build') {
         steps {
            bat 'docker build DevOps// -t flask_p'
         }
      }
      stage('Run') {
         steps {
            dir ('DevOps') {
                bat 'dir'
                bat 'docker-compose up -d'
            }
         }
      }
      stage('Test') {
         steps {
             dir ('DevOps\\tests') {
                 bat 'dir'
                 bat 'python e2e.py'
             }
         }
      }
	  stage('Finalize') {
         steps {
			dir ('DevOps') {
				bat 'docker-compose down'
			}
         }
      }
   }
   post {
       always {
		   dir ('DevOps') {
				bat 'docker-compose down'
				}
		   //bat 'echo skip delete until sucess'
           bat 'rmdir /s /q DevOps'
       }
   }
}