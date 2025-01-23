
choice env = var.environment

node(){
    parallel 
    {
    stage('Checkout'){
        sh 'git clone github@github.xom'
        }
    stage('Build'){
        sh 'maven build'

    }
    stage('Unit Tests'){
        sh 'junit filename'

    }
    stage('Push artifact'){
        sh 'jf push *.jar'
    }
    }
}
