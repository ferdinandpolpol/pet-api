# pet-api

## Dev Setup
- Install docker and docker-compose
- The command below will create a django container and automatically import the data from pets.csv
`docker-compose up --build -d`

## Using the API
### GET
```
```

### POST
```
curl -H "Content-type: application/json" -d '{ "name": "sample", "species": "dog", "age": 123}' -X POST "http://localhost/pet/"
```