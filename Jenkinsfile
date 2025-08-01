pipeline {
    agent any // Run the pipeline on any available Jenkins agent (your VM in this case)

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Yanniky/my-devops-flask-app.git' // Replace with your repo URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the current directory
                    // Tag it with a unique build number from Jenkins
                    docker.build("my-flask-app:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    // Run a test command inside the built Docker image
                    // This is a simple test, a real app would have unit tests
                    sh 'docker run --rm my-flask-app:${BUILD_NUMBER} python -c "import flask"'
                    echo "Basic Docker image test passed!"
                    // In a real scenario, you'd run something like:
                    // sh 'docker run --rm my-flask-app:${BUILD_NUMBER} pytest' (if you had pytest tests)
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                // In this case, our "artifact" is the Docker image.
                // We'll trust Docker's local image storage for now.
                // Later, we'd push to a registry.
                echo "Docker image built and ready: my-flask-app:${env.BUILD_NUMBER}"
            }
        }
    }
}