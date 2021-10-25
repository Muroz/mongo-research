# Mongo Research

The purpose of this repo is to explore and compare all of the mongo drivers available on each programming language

## Local Instance:

As part of this repo, there is a `docker-compose` file at the root to run a local mongo instance and an instance of mongo-express (which is a GUI to interact with the db instance). They are set to run on ports `27017` and `8081` respectively, but can be updated as desired.

You can run them locally with:

`docker-compose up`

And stop all processes with if run on detached mode (-d option):

`docker-compose down`
