# goit-pyweb-hw-08 (NoSQL)

## Section 1

Firstly, I created a MongoDB Cluster and installed MongoDB Compass for control. Afterwards, I made a model with a database connection. Continuing the process, I wrote the script to upload "JSON" files to the database. Lastly,  I wrote two scripts to search in the database: "search_scripts.py" and "seacrh_scripts_2.py"(with Redis caching"). I had to install Redis and Redis-LRU for the second script for caching information.

## Section 2

I created a docker-compose for "Section 2" to connect to RabbitMQ. As in the previous section, I also made a model and connected it with the MongoDB database. As required, I created two files: "consumer.py" and "producer.py". To make Python codes work with RabbitMQ, I had to install a RabbitMQ client library for Python called "pika"  and packet  "faker" to generate fake data. 

Additional task: created "consumer_sms.py" and "producer_sms.py" files to run both sms and emails. The "producer.py" also was updated to run two functions.