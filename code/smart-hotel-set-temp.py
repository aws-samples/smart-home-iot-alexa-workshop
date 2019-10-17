import json
import boto3
import datetime
timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
client = boto3.client('iot-data')


def lambda_handler(event, context):
    roomId = event['multiValueQueryStringParameters']['room'][0]
    # TODO implement
    temp = 72
    response = client.publish(
        topic = 'resetRoom',
        qos = 1,
        payload = json.dumps({"roomid": roomId, "timestamp": timestamp, "shades": "up", "theater": "stopped", "thermostat": temp})
    )
    return {
        "statusCode": 200,
    }