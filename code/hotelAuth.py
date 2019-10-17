import json

#Format return policy that API Gateway expects
def generatePolicy(principalId, effect, resource):
  return {
    'principalId': principalId,
    'policyDocument': {
      'Version': '2012-10-17',
      'Statement': [{
        'Action': 'execute-api:Invoke',
        'Effect': effect,
        'Resource': resource
      }]
    }
  };
def customLogicFunction(token):
    #Run your custom authorization here
    #i.e. Check your DynamoDB table for token associated with user
    #Return true or false
    return

def lambda_handler(event, context):
    
    #if(customLogicFunction(event['authorizationToken']) == true)
        return generatePolicy('user', 'Allow', event['methodArn'])
    
    #else
      #return generatePolicy('user', 'Deny', event['methodArn']) n