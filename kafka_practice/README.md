
## Introduction

- 해당 코드는 boaz라는 kafka topic을 생성하고 consumer, producer가 실제로 어떻게 데이터를 가져가는지 확인하기 위한 예시입니다.
- 아래 How to run을 따라서 실습을 진행해주세요.
- **실습을 진행한 이후에 더 찾아볼 법한 것들에 대해 학습해보세요.**
  - 생성한 topic 목록은 어디서 볼 수 있지?
  - consumer, producer를 동시에 여러개 동작시켜도 동일하게 동작할까?

## How to run

1. run kafka

``` bash
# check if docker daemon is running please.
docker-compose up
```

2. install dependencies

``` bash
pip install kafka-python
```

3. create topic

``` bash
python create_topic.py
```

4. run consumer

``` bash
python consumer.py 
```

5. run producer

``` bash
python producer.py 
```

## results

``` bash
# create_topic.py output
Topic 'boaz' created successfully.

# consumer.py output
python consumer.py 
Received: {'number': 0}
Received: {'number': 1}
Received: {'number': 2}
Received: {'number': 3}
Received: {'number': 4}
Received: {'number': 5}
Received: {'number': 6}
Received: {'number': 7}
Received: {'number': 8}
Received: {'number': 9}

# producer.py output
python producer.py 
Sent: {'number': 0}
Sent: {'number': 1}
Sent: {'number': 2}
Sent: {'number': 3}
Sent: {'number': 4}
Sent: {'number': 5}
Sent: {'number': 6}
Sent: {'number': 7}
Sent: {'number': 8}
Sent: {'number': 9}
```


# 사실은 너무 비싸서
aws의 SQS를 사용한다. (이건 프리티어로 사용)
* 신입 서류에서 단순히 카프카 사용했다는 것 보다는 왜 사용했는지에 대해서 적어야 할듯.