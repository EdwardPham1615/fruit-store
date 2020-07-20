########################## INSTALLATION ##########################
#Create network for Docker
docker network create dev
#Run MongoDB with Docker
docker run -it -d --name mongodb --hostname mongodb --network dev -p 27017:27017 \
        -e MONGO_INITDB_ROOT_USERNAME=mongo -e MONGO_INITDB_ROOT_PASSWORD=123456789 mongo:latest
#Setup MongoDB
Create "FruitOrder" database
Create "OrderCollection" collection
#Build Docker image for fruit store
cd fruit-store
docker build -t fruit-store .
#Run fruit-store with Docker
docker run -d --name fruit-store --hostname fruit-store --network dev -p 5000:5000 fruit-store

########################## DEMO ##########################
You can simply use Postman or using curl command below
#order API
curl -X POST -H "Content-Type: application/json" -d '{"date": 1, "fruit":{"melon": 2, "grape": 10}}' http://127.0.0.1:5000/order
#report API
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/report?from=1&to=4
