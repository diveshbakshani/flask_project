# LendBuzz Flask App Project

## About the App

This is a Flask application that utilizes Python 3.12, Flask, pytest, Docker, docker-compose to simulate a backend system for a text analysis microservice architecture.

## How to Run

1. Clone the repository: `git clone https://github.com/diveshbakshani/flask_project.git`
2. Build and run the docker images while in base directory enter:
    docker compose build --no-cache
3. Once it's done building enter the following in terminal to run the docker images (in detached mode), or you can use docker desktop to run them from there as a group.
    docker-compose up -d
4. Once the containers start up you can access the microservices as laid out in the Assignment PDF
5. Or you can use postman to check the outputs by sending GET and POST requests to the endpoints:
    * http://localhost:8000/analyze
    * http://localhost:8000/services
    * http://localhost:8001/analyze
    * http://localhost:8002/count
    * http://localhost:8003/recognize

I used docker desktop 4.25.1 for this project as the latest version 4.26 had some issues with internal host routing.

## How to Run the Tests
1. Install pytest: `pip install pytest`
2. cd into the folder `tests`
3. Run the tests: `pytest`

## Thoughts

* The app was definitely a challenge to build and took me a lot of research and sifting through documentation and stack overflow to fix errors.
* I mainly referenced the flask documentation, pytest documentation and docker documentation to build the app. I also used stackoverflow to fix errors as they came.

## System Design and Scope of the App

- Firstly, the reason why this app was built as a microservice:
    - It was requested in the project but,
    - Microservices provide a few important advantages over monolithic app architecture: much more planned architecture making it easier to manage and fix issues in the future, faster development speed where the entire app isnt blocked until for example a PR gets resolved(code decoupling), flexibility to switch a specific component(or all) to a different language or a framework without blocking user endpoints, scalability of individual components, flexible deployment 
    - Moreover, microservices while being complex for individual components, reduce the overall complexity of big projects by breaking down the project into smaller chunks.

- I decided to dockerize the individual microservices of the project in order to simulate the usage of individual scaling of a service when required.
- For example, if we are getting a lot of users using sentiment analysis more than the other 2 users, a dockerized container hosted via Kubernets has the power to automatically scale it's resources according to demand.
- Also, dockerizing apps simply makes dependency management easier. This avoids version conflicts.

- What I have not included with the app but would design with the app:
    - For the purposes of testing the server is hosted on a local environment for hosting it in an actual environment with the ability to reverse proxy and load balance, we would use something like nginx, apache, gunicorn or uWSGI (specific to python) to deploy the server. Webservers also provide automatic request handling, authentication and other features.
    - Reverse proxying and load balancing makes sure that the python server is actually using it's resorces effectively by eliminating trivial, but massive requests such as requests to static files. This enables the app to scale horizontally while also being cost effective.
    - I decided against django for such a small application since the structuring of django would make it consume a lot of resources unncesessarily, being batteries included.
    - I also decided to use a dictionary to simulate some form of persistency of data however to achieve actual persistency a database like postgres would be used instead.

- Hence, in my opinion the strongest points of a microservice architecture are, and these are some of the problems that designing a microservice architecture system helps solve:
    - Scalability of individual components
    - Flexibility to work on different components simultaneously in a team
    - Containerizing code to eliminate or reduce complexity

