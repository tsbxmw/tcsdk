node('stf'){
    stage('get code'){
        if (!fileExists('tcsdk')){
            sh 'git clone https://github.com/tsbxmw/tcsdk'
        }
    }
    stage('update code to new'){
        dir('tcsdk'){
            sh 'rm -rf test.py test_upload.py'
            sh 'git pull origin master'
        }
    }
    stage('build file'){
        dir('tcsdk'){
            sh 'python setup.py sdist'
            if (!fileExists('./dist')){
                sh 'exit 1'
            }
        }
    }
    stage('test'){
        dir('tcsdk'){
            sh 'cp -rf ./tests/* ./'
            sh 'python test.py'
            sh 'python test_upload.py'
        }
    }
}