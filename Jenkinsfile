//------------------------------------------------------------------------------
// Jenkinsfile for ActianCorp/jaspersoft-docs
//
// Builds the Zensical site (zensical.toml) and deploys it to the
// aws-docserver on every push to main. Modeled on the
// data-intelligence.docs_production_deploy Jenkins job / the
// data-platform-docs Jenkinsfile, adapted for this repo's build
// (`zensical build` + the flare2md link/list checks, no Makefile here).
//------------------------------------------------------------------------------

//----- functions, methods -----------------------------------------------------
//post notifications
def sendMessages() {
    echo "--> sendMessages()"
    script {
        if ( DEVOPS_BUILD.toBoolean() == false ) {
            emailext(
                body: '${DEFAULT_CONTENT}',
                mimeType: 'text/html',
                replyTo: '${DEFAULT_REPLYTO}',
                subject: '${DEFAULT_SUBJECT}',
                to: "${EMAIL_RECIPIENTS}",
                recipientProviders: [culprits(), requestor()]
            )
        } else {
            echo "--- DevOps build, SKIP sendMessages() ---"
        }
    }
}

pipeline {
    agent { label 'default-agent' }

    // triggers{
    //     pollSCM('H/5 * * * *')
    // }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }

    environment {
        DOCNAME="${JOB_NAME}"

        EMAIL_RECIPIENTS='jim.mccaskey@hcl-software.com, ' +
            'bipinkumar.pandey@hcl-software.com, calvin.raj@hcl-software.com, cody.kern@hcl-software.com, mike.zayour@hcl-software.com'
    }

    stages {
        stage('Cleanup Previous Build and Configure Build') {
            steps {
                sh "rm *.log 2>/dev/null || true"
                script {
                    if ( !env.BRANCH_NAME) { // non-multibranch pipeline does not provide BRANCH_NAME, need to set manually
                        env.BRANCH_NAME = scm.branches[0].name
                    }

                    if ( BRANCH_NAME =~ "feature/DEVOPS-*" || BRANCH_NAME =~ "bugfix/DEVOPS-*") {
                        env.DEVOPS_BUILD = true
                    } else {
                        env.DEVOPS_BUILD = false
                    }
                    env.REPO_COMMIT_URL_ANCHOR = "[${GIT_COMMIT[0..6]}](https://github.com/ActianCorp/jaspersoft-docs/commit/${GIT_COMMIT})"
                    currentBuild.description = "**Commit**: ${REPO_COMMIT_URL_ANCHOR}"

                    echo "JOB_BASE_NAME:             [" + JOB_BASE_NAME + "]"
                    echo "JOB_NAME:                  [" + JOB_NAME + "]"
                    echo "BUILD_NUMBER:              [" + BUILD_NUMBER + "]"
                    echo "BRANCH_NAME:              [" + BRANCH_NAME + "]"
                    echo "DEVOPS_BUILD:             [" + DEVOPS_BUILD + "]"
                    echo "GIT_COMMIT:               [" + GIT_COMMIT + "]"
                    echo "REPO_COMMIT_URL_ANCHOR:   [" + REPO_COMMIT_URL_ANCHOR + "]"
                }
                sh "set | sort > _${JOB_BASE_NAME}_init_env-${BUILD_NUMBER}.log"
            }
            post {
                always {
                    archiveArtifacts allowEmptyArchive: true, artifacts: '*.log'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Zensical site') {
            steps {
                sh 'zensical build'
            }
        }

        stage('Validate site') {
            steps {
                // Same gates as .github/workflows/deploy.yml: fail the build
                // rather than ship broken internal links or a flattened
                // nested list from the Flare-to-Markdown conversion.
                sh '''
                    python3 tools/flare2md/check_site.py
                    python3 tools/flare2md/check_lists.py
                '''
            }
        }

        stage('Package output for deploy') {
            steps {
                sh 'zip -r output.zip site'
                archiveArtifacts artifacts: 'output.zip', onlyIfSuccessful: true
                stash includes: 'output.zip', name: 'output.zip', useDefaultExcludes: false
            }
        }

        stage('Publish to aws-docserver') {
            when {
                branch "main"
            }
            agent { label 'aws-docserver' }
            // We don't need the source checked out to the web server
            options { skipDefaultCheckout true }
            steps {
                unstash 'output.zip'
                fileOperations([fileUnZipOperation(filePath: 'output.zip', targetLocation: '.')])
                bat "move D:\\Sites\\jaspersoft D:\\backups\\jaspersoft-${BUILD_NUMBER}.backup"
                bat "move ${WORKSPACE}\\site D:\\Sites\\jaspersoft"
            }
        }
    }

    post
    {
        always {
            echo '----- post/always -----'
            logParser failBuildOnError: true, parsingRulesPath: '/var/lib/jenkins/documentation_log_parsing.txt',
                projectRulePath: '/var/lib/jenkins/documentation_log_parsing.txt', useProjectRule: false
        }
        success {
            echo '----- post/success -----'
            cleanWs()
        }
        unsuccessful {
            // unstable, fail, or abort
            echo '----- post/unsuccessful -----'
            sendMessages()
        }
        fixed{
            // unstable or fail -> success
            echo '----- post/fixed -----'
            sendMessages()
        }
    }
}
