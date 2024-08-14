from kafka.admin import KafkaAdminClient, NewTopic

# Kafka Admin Client 설정
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test_admin_client'
)

# 새로운 토픽 생성
topic_name = "boaz"
topic_list = [NewTopic(name=topic_name, num_partitions=3, replication_factor=1)]

# 토픽 생성
try:
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print(f"Topic '{topic_name}' created successfully.")
except Exception as e:
    print(f"Failed to create topic '{topic_name}': {e}")

admin_client.close()
