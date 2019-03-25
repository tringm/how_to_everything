## Docker instruction

- Template Docker file
  ```
  FROM ubuntu:18.10
  ENV LC_ALL C.UTF-8
  ENV LANG C.UTF-8
  LABEL maintainer="Tri Nguyen <tri.nguyen@helsinki.fi>"

  RUN apt update
  RUN apt install -y python3
  RUN apt install -y python3-pip
  RUN pip3 install pipenv
  RUN useradd --create-home appname

  WORKDIR /home/appname/
  COPY Pipfile* ./
  RUN find . -type f -print0 | xargs -0 chmod 644

  USER appname
  RUN LC_ALL=C.UTF-8 LANG=C.UTF-8 pipenv install

  USER root
  COPY app.py ./
  RUN chmod 644 app.py

  USER appname
  CMD ["pipenv", "run", "waitress-serve", "--listen", "*:8000", "--call", "app:create_app"]
  ```

- Create Docker Image with repo name and  tag:
  ```
  docker build --tag=reponame .
  ```

  or

  ```
  docker build --tag=reponame:v0.0.1 .
  ```

  for the exact tag instead of latest

- Passing environment variables
  - Pass the environment variables from the host to the containers
    ```
    docker run -e var_name (...)
    ```
  - Use env_files
    ```
    docker run --env-file=env_file_name app
    ```
- List docker image
  ```
  docker image ls
  ```

- Remove docker Image
  ```
  docker image rm <image_id>
  ```
