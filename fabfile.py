from fabric.api import local

def deploy():
    local('docker build -t garciadiazjaime/website-focus .')
    local('docker push garciadiazjaime/website-focus')
    local('echo "docker pull garciadiazjaime/website-focus"')
