import json
import boto3
import datetime
timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
client = boto3.client('iot-data')


def lambda_handler(event, context):
    temp = event['multiValueQueryStringParameters']['temp'][0]
    print(event)
    roomId = 101
    response = client.publish(
        topic = 'setTemp',
        qos = 1,
        payload = json.dumps({"roomid": roomId,"timestamp": timestamp, "thermostat": temp })
    )
    return {
        "statusCode": 200,
    } 