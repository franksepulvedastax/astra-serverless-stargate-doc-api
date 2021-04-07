# astra-serverless-stargate-doc-api

Astra (Serverless) and Stargate demo. using Document API

DataStax Astra is a cloud-native Cassandra-as-a-Service Built on Apache Cassandra designed to simplify cloud-native application development.

Stargate is an open source data gateway that sits between your app and your databases. Stargate brings together an API platform and data request coordination code into one OSS project.

The goal of this demo is to show how to write code to create a schemaless JSON document store in Astra, via Stargate’s Document API.

In this demo. we will:
#1 create an Astra serverless database,
#2 briefly show the Cassandra Query Language (CQL) console,
#3 briefly show how to collect database metadata (e.g., ID, region, etc.), 
#4 populate Python script with database metadata,
#5 use Python script, only using a http libray and a JSON parser (i.e., no Cassandra drivers), to load JSON data (i.e., documents) into our database, 
#6 review JSON datasets,
#7 use Swagger to visually render documentation for Stargate's Document API, and
#8 use Postman, a collaboration platform for API development, to query data. 
