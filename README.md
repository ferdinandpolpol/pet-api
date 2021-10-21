# pet-api

## Dev Setup
- Install docker and docker-compose
- The command below will create a django container and automatically import the data from pets.csv
`docker-compose up --build -d`

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