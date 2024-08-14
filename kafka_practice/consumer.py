from kafka import KafkaConsumer
import json

# Kafka Consumer 설정
consumer = KafkaConsumer(
    'boaz',  # 구독할 토픽
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커의 주소
    auto_offset_reset='earliest',  # 처음부터 메시지를 읽기
    enable_auto_commit=True,  # 자동으로 오프셋 커밋
    group_id='my-group',  # Consumer 그룹 ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # 메시지를 JSON으로 역직렬화
)

# 메시지 수신
def consume_messages():
    for message in consumer:
        print(f"Received: {message.value}")

if __name__ == "__main__":
    consume_messages()
