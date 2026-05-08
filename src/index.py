import json

def handler(event, context):
    print("Evento recebido do S3 com sucesso!")
    return {
        'statusCode': 200,
        'body': json.dumps('Sucesso no processamento serverless!')
    }
