pip install kafka-python


docker run -d --name zookeeper -p 2181:2181 \
  --env ZOOKEEPER_CLIENT_PORT=2181 \
  confluentinc/cp-zookeeper:latest


docker run -d --name kafka -p 9092:9092 \
  --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  --env KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  --env KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
  --link zookeeper \
  confluentinc/cp-kafka:latest



