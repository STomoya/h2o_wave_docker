
# h2o_wave_docker

A Docker image for [H2O Wave](https://h2oai.github.io/wave/)

## Requirements

- Docker

- docker-compose

## Usage

Build image.

```console
docker-compose build
```

Start Wave Server

```console
docker-compose up -d
```

Run python code to update the page (`hello.py` for example)

- Inside container

    Step inside container

    ```console
    $ docker-compose exec app bash
    ```

    Run code

    ```console
    python hello.py
    ```

- Run

    ```console
    docker-compose run app python hello.py
    ```

## Author

[STomoya](hyyps://github.com/STomoya)
