from kafka import KafkaProducer
import json
import time

# Kafka Producer 설정
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커의 주소
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 메시지를 JSON으로 직렬화
)

# 메시지 전송
def send_messages():
    for i in range(10):
        message = {'number': i}
        producer.send('boaz', value=message)  # 'boaz'라는 토픽으로 메시지 전송
        print(f"Sent: {message}")
        time.sleep(1)  # 1초마다 메시지 전송

    producer.flush()  # 모든 메시지가 전송되었는지 확인
    producer.close()

if __name__ == "__main__":
    send_messages()
