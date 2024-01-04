# Creating a Real-Time Bike-info Data Pipeline with Kafka, Apache Spark, Elasticsearch and Kibana

In this project,  we utilize Kafka for real-time collection of bicycle station data, analyze it with Spark, and store it in Elasticsearch. Kibana creates a visual dashboard with a map showing the stations and their availabilities. Finally, the data is retained in a Hadoop DataLake named Hive for further analysis, providing an integrated solution for real-time management of bicycle stations


## Pipeline
Our project pipeline is as follows:

![image](https://github.com/chaimazaghouani/Bike_Project/assets/110690177/bd211db7-eb24-465c-8b54-7bb0c6e1f31d) 


## Prerequisites
The following software should be installed on your machine in order to reproduice our work:

- Spark (spark-3.2.4-bin-hadoop3.X)
- Kafka (kafka_0-10_2.12)
- ElasticSearch (elasticsearch-8.8.2)
- Kibana (kibana-8.8.2)
- hive_2.12:3.2.4
## Steps
###### Get Bike API:
We started by collecting in real-time Bike informations ("properties": {
            "numbers": { "type": "integer" },
            "contract_name": { "type": "text" },
            "banking": { "type": "text" },
            "bike_stands": { "type": "integer" },
            "available_bike_stands": { "type": "integer" },
            "available_bikes": { "type": "integer" },
            "address": { "type": "text" },
            "status": { "type": "text" },
            "position": {
                "type": "geo_point"
            },
            "last_update": { "type": "text" }
            }) and then we sent them to Kafka for analytics.

###### Kafka Real-Time Producer:
The data is ingested from the biket streaming data API and sent to a kafka topic. You need to run Kafka Server with Zookeeper and create a dedicated topic for data transport.
###### PySpark Streaming:
 In Spark Streaming, Kafka consumer is created that periodically collect data in real time from the kafka topic and send them into an Elasticsearch index.
###### Index  to Elasticsearch:
You need to enable and start Elasticsearch and run it to store the flight-info and their realtime information for further visualization purpose. You can navigate to http://localhost:9200 to check if it's up and running.
###### Kibana for visualization
Kibana is a visualization tool that can explore the data stored in elasticsearch. In our project, instead of directly output the result, we used this visualization tool to visualize the streaming data in a real-time manner.You can navigate to http://localhost:5601 to check if it's up and running.
###### hive for storage
Hive Implementation for Historical API Data Storage: Managing and Storing Historical Data from APIs.
## How to run
1. Start Elasticsearch

`sudo systemctl start elasticsearch ` & `sudo systemctl enable elasticsearch `

2. Start Kibana

`sudo systemctl start kibana ` & `sudo systemctl enable kibana  `

3. Start Zookeeper server by moving into the bin folder of Zookeeper installed directory by using:

`./bin/zookeeper-server-start.sh ./config/zookeeper.properties`

4. Start Kafka server by moving into the bin folder of Kafka installed directory by using:

`./bin/kafka-server-start.sh ./config/server.properties`

5. Run Kafka producer:

`python3 ./kafka_producer.py`

6. Run PySpark consumer with spark-submit:

`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,,org.elasticsearch:elasticsearch-spark-30_2.12:7.14.2 /home/dell/Bike_Project/pyspark_consumer.py`(one for elasticsearch et one for hive)

## How to launch kibana dashboard

- Open http://localhost:5601/ in your browser.
- Go to Management>Kibana>Saved Objects
- Import Real-Time-Bike_Project-Project-Dashbord.ndjson
- Open dashboard

## How to launch hive table
-Open hadoop : start-dfs.sh
-Open hive : hive metastore service 
-Open http://localhost:50070/ in your browser.
  



## Final result
-Kibana:

![image](https://github.com/chaimazaghouani/Bike_Project/assets/110690177/67620a23-223b-4946-b1ed-a25b70ae9565)

-Hive:

![image](https://github.com/chaimazaghouani/Bike_Project/assets/110690177/5ea92c61-150b-4a9e-9ac0-e0456da25d66) 


## Contribution

Chaima Zaghouani

Yomna Hajji


























