### Access the Kafka container:

```commandline
docker exec -it kafka bash
``` 

### 1. Create a Topic:

```commandline
kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --replication-factor 1 \
  --partitions 3 \
  --topic test-topic
```

### 2. List Topics:
```commandline
kafka-topics --list \
  --bootstrap-server localhost:9092
```

### 3. Start a Producer:
```commandline
kafka-console-producer --broker-list localhost:9092 --topic test-topic
```
- Type messages and press Enter to send each message.

### 4. Start a Consumer:
```commandline
kafka-console-consumer --bootstrap-server localhost:9092 \
  --topic test-topic \
  --from-beginning
```

### 5. Check Consumer Groups:
```commandline
kafka-consumer-groups --bootstrap-server localhost:9092 --list
```


### 6. Describe specific consumer group
```commandline
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --describe \
  --group <group-name>
```


### 6. Add partitions to topic
```commandline
kafka-topics --alter \
  --bootstrap-server localhost:9092 \
  --topic test-topic \
  --partitions 6
```


### 7. Stop container 
```docker-compose down```



Command	                                Description
```kafka-topics --list```	            List all topics.

```kafka-topics --describe```	        Describe topic details (partitions, replicas).

```kafka-console-producer```	        Start a producer to send messages.

```kafka-console-consumer```	        Start a consumer to read messages.

```kafka-consumer-groups --list```	    List active consumer groups.

```kafka-consumer-groups --describe```	Show details of a consumer group.



