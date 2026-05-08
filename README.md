# Automa-o-de-Infraestrutura-com-AWS-Lambda-e-Amazon-S3-via
Este projeto demonstra a automação de fluxos de trabalho na nuvem utilizando AWS Lambda e Amazon S3, orquestrados pelo AWS CloudFormation.

# Projeto: Automatizando Tarefas com AWS Lambda e S3 via CloudFormation

## 🎯 Objetivo
Este laboratório tem como foco a implementação de uma arquitetura **Serverless** e orientada a eventos. O objetivo é utilizar o **AWS CloudFormation** para automatizar a criação de um bucket no **Amazon S3** que dispara uma **Lambda Function** sempre que um novo arquivo é adicionado.

---

## 🛠️ Tecnologias e Serviços Utilizados
*   **AWS CloudFormation**: Automação da infraestrutura como código (IaC).
*   **Amazon S3**: Armazenamento de objetos e origem dos eventos.
*   **AWS Lambda**: Execução de código em resposta a eventos (computação serverless).
*   **IAM (Identity and Access Management)**: Configuração de permissões e roles de execução.
*   **YAML**: Linguagem para definição do template.

---

## 📂 Estrutura do Repositório
*   `/templates/automation-stack.yaml`: Template CloudFormation com os recursos S3 e Lambda.
*   `/src/index.py`: Exemplo de código Python para a função Lambda.
*   `README.md`: Documentação com insights técnicos.

---

## 📝 Insights e Aprendizados
1.  **Gatilhos de Evento (Triggers)**: Aprendi como conectar o S3 à Lambda, permitindo que processos (como processamento de imagens ou logs) ocorram em tempo real após um upload.
2.  **Permissões de Recurso**: Entendi a importância das `LambdaPermission`, que autorizam o serviço S3 a invocar a função Lambda.
3.  **Escalabilidade Serverless**: A grande vantagem de não precisar gerenciar servidores, deixando a AWS escalar a execução conforme a demanda de arquivos no bucket.

---

## 💻 Exemplo de Template (Integração S3-Lambda)

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Automação S3 e Lambda - Projeto DIO'

Resources:
  # 1. Bucket S3
  MeuBucketAutomatizado:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'dio-lambda-s3-project-${AWS::AccountId}'

  # 2. IAM Role para a Lambda
  LambdaExecutionRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: [lambda.amazonaws.com]
            Action: ['sts:AssumeRole']
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'

  # 3. Função Lambda
  MinhaFuncaoAutomata:
    Type: 'AWS::Lambda::Function'
    Properties:
      Handler: index.handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Runtime: python3.9
      Code:
        ZipFile: |
          def handler(event, context):
              print("Evento recebido do S3 com sucesso!")
              return {"status": "sucesso"}

  # 4. Permissão para o S3 chamar a Lambda
  S3InvokeLambdaPermission:
    Type: 'AWS::Lambda::Permission'
    Properties:
      Action: 'lambda:InvokeFunction'
      FunctionName: !Ref MinhaFuncaoAutomata
      Principal: s3.amazonaws.com
      SourceArn: !GetAtt MeuBucketAutomatizado.Arn
