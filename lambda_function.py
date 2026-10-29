import json

def lambda_handler(event, context):
    print("Otrzymano zdarzenie (Event):", json.dumps(event))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Witaj! Ta wersja została wdrożona automatycznie przez CodePipeline!')
    }
