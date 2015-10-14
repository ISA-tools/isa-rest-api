# isa-rest-api

RESTful web service to interact with ISA API. Separating out the web service from the programmable API.

Needs to import isatools package from [isa-api project](https://github.com/ISA-tools/isa-api)

Basically to test directly, make sure you've got the right prereqs installed:

`pip install -r files/requirements.txt`

then:

`python app.py` to start flask's embedded server, and browse. 
`localhost:5000/api/spec.html` for swagger UI
`localhost:5000/api/spec.json` for swagger JSON

or load into PyCharm and play with the test_rest_api.py tests

# Usage (to complete)
## Convert ISArchive (ISA-Tab) archive to ISA-JSON
### `POST /convert/isatab-to-json`
| Consumes              | Produces           | Description    |
| --------------------- |:------------------:| -------------- |
| `application/zip`    | `application/json` |  Takes a ISArchive zip file containing ISA-Tab `.txt` files, converts and returns a single ISA-JSON. Returns 200 OK if succeeded. |

## Convert ISArchive (ISA-JSON) to Tab ISArchive (ISA-Tab) (incomplete, do not use)
### `POST /convert/json-to-isatab`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
| `multipart/form-data` | `multipart/form-data` |  Takes a ISArchive zip file containing a collection of ISA-JSON `.json` files, converts and returns a ISArchive containing ISA-Tab `.txt` files. Returns 200 OK if succeeded.|

### `POST /convert/json-to-isatab`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
| `application/json`    | `application/zip`     |  Takes ISA-JSON content, converts and returns a ISArchive containing ISA-Tab `.txt` files. Returns 200 OK if succeeded. |

## Convert ISArchive (ISA-Tab) to CEDAR JSON
### `POST /convert/isatab-to-cedar`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
| `application/zip    ` | `application/json`    |  Takes a ISArchive zip file containing a collection of ISA-Tab `.txt` files, converts and returns a single CEDAR JSON. Returns 200 OK if succeeded.|

## Create and populate and ISA object, and then get an ISA document (incomplete, do not use)
### `POST /create/`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
| `application/json`    | `application/json`    |  Takes JSON with create parameters (TBC), returns 201 OK and URI of newly created ISA object if succeeded. |

### `PUT /update/{object_id}`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
| `application/json`    | `application/json`    |  Takes JSON with update parameters (TBC), returns 201 OK and URI of updated ISA object if succeeded. |

### `GET /get/{object_id}`
| Consumes              | Produces              | Description    |
| --------------------- |:---------------------:| -------------- |
|                       | `application/json`    |  Returns 200 OK and URI of ISA-JSON representation of ISA object with object ID `{object_id}`. |

# Docker stuff

From docker-flask-example, below copied from that project's README.md, need to test our own settings.

A generic python/Flask app with a Docker file

# Getting started with Docker
1. Install DockerToolbox (https://www.docker.com/toolbox)
2. Install VirtualBox (https://www.virtualbox.org/wiki/Downloads)
3. Open the newly installed "Docker" folder (in Applications for Mac)
4. Click "Docker Quickstart Terminal"
5. Run: docker pull heddle317/docker-flask-example
6. Run: docker run -p 8080:80 -e ENVIRONMENT='production' -d --name=flask_app heddle317/docker-flask-example
7. Run: VBoxManage controlvm default natpf1 "flask_app,tcp,127.0.0.1,8080,,8080"
8. Go to localhost:8080 in your browser and you should see "Hello, world!"

# Creating your own version of this repo
1. Fork this repository.
2. Create an account at Dockerhub.com
3. Click the "Create" dropdown in the far top right corner (not the "Create Repository+" button)
4. Select "Create Automated Build"
5. Link your Github (or Bitbucket) account, select your user, select the github repo, etc.
6. Click the "Trigger a build" button, go to the "Build Details" tab and you should see a new build for your container.

# Testing your docker container when there are changes
1. Clone your new repository down to your laptop
2. Make a change to your Flask application (white space changes or comments are easy to test).
3. Push your change to github.
4. Go to your dockerhub account, click on your automated build repository, and click the build details tab.
5. Once the build is finished, go to boot2docker.
6. Run: docker pull [dockerHubUsername]/docker-flask-example (if you changed the name of the repo, reflect that here)
7. Run: docker run -p 8080:80 -e ENVIRONMENT='production' -d --name=flask_app [dockerHubUsername]/[repoName]
8. Go to localhost:8080 in your browser and you should see your application.

# Running your docker image in AWS
1. Make an AWS account (if you don't have one).
2. Create your own VPC (OPTIONAL: if you don't have one or want a new one).
3. Create a new public subnet.
4. Create an instance in your new public subnet.
5. Ssh to your new machine: ssh -i aws.pem ec2-user@[instance-public-dns]
6. Run: sudo yum update -y
7. Run: sudo yum install -y docker
8. Run: sudo service docker start
9. Run (only necessary for private docker images): sudo docker login -e '[email]' -p '[password]' -u '[dockerHubUsername]'
10. Run: sudo docker pull [dockerHubUsername]/[repoName]
11. Run: sudo docker run -p 80:80 -e ENVIRONMENT='production' -d --name=flask_app [dockerHubUsername]/[repoName]
12. Go to [instance-public-dns] to see your web app.

# Setting up your python development environment (OPTIONAL)
1. If your laptop is not setup for python, follow these instructions (http://newcoder.io/pyladiessf/)
2. Create a new virtualenv with venv or mkvirtualenv
3. Run: pip install -r ./files/requirements.txt
4. Create a keys.sh file with your sensitive information (e.g. export ENVIRONMENT='dev' and SECRET_KEY='')
5. Run: ./run.sh web.py
6. You should be able to see your application running on localhost:7010 (that port is configured in the app/config.py file)


