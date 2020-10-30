## Coupons App - Postgres / Python / JS (Heroku)

### Tech
1. Docker - Containers
2. Postgres - DB
3. pgAdmin - Postgres GUI
4. Python(3) Flask - Server (API and UI)
5. HTML/JS - Client UI

### Steps
#### 1. Python3
https://www.python.org/downloads/

#### 2. Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli

#### 3. Install docker
Download Docker 
- Windows: https://hub.docker.com/editions/community/docker-ce-desktop-windows
- Mac: https://hub.docker.com/editions/community/docker-ce-desktop-mac

#### 4. Start Postgres and pgAdmin(as a container) using docker-compose
`$> docker-compose up` 

This command pulls docker image and starts Postgres 12.2 and pgAdmin 4.4.18

### 5. Database

- Postgres will be running in container port 5432 and exposed at `http://localhost:5432`

  - Default DB username: `admin` , password:  `secret`

- pgAdmin will be running in container port 80 and exposed at `http://localhost:8080`

  - Default username: `admin@linuxhint.com` , password:  `secret`
  - To add 'postgres' server to pgAdmin, get postgres server host, username, password, database
    - To get host/IP address of postgres (running indocker container)
      - `$> docker ps -a` : Lists all running container
      - `$> docker inspect <CONTAINER ID>` : Container id of postgres
      - IPAddress will be in `NewtorkSettings.Networks.IPAddress`
      - Use this IPAddress as host
    - Heroku postgres details will be in Heroku Data Store settings

- PostgreSQL docs - https://www.postgresql.org/docs/12/index.html
- Example SQL is at `./sql.txt`

### 6. Start Python (Flask) Server
  Serves UI and API server

  1. Create virtualenv `$> python3 -m venv ./server/virtualenv`
  2. Activate virtualenv `$> source ./server/virtualenv/bin/activate`
  3. Install dependencies : `$> pip3 install -r ./server/requirements.txt`
  4. Start python server : `$> python3 ./server/app.py`

#### Server urls
- UI : `http://localhost:5000/`
- API : `http://localhost:5000/api/`
