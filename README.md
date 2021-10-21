# pet-api

## Dev Setup
- Your machine might need to install docker and docker-compose
- https://docs.docker.com/get-docker/
- https://docs.docker.com/compose/install/
- The command below will create a django container and automatically import the data from pets.csv
- `docker-compose up --build -d`
- The api should be now up and running and visiting `http://localhost` should show a page with `Welcome to Pet-API`

- To stop the running cointainer
`docker-compose stop`


## Using the API with cUrl
### GET
```
curl "http://localhost/pet/"

# You can also filter by passing the parameters species, name, age
curl "http://localhost/pet/?species=dog" 
```

### POST
```
curl -H "Content-type: application/json" -d '{ "name": "sample", "species": "dog", "age": 123}' -X POST "http://localhost/pet/"
```