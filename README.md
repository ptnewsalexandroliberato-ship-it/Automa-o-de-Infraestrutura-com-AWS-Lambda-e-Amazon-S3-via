# Projeto: Automatizando Tarefas com AWS Lambda e S3 via CloudFormation

## 🎯 Objetivo
Este laboratório tem como foco a implementação de uma arquitetura **Serverless** e orientada a eventos. O objetivo é utilizar o **AWS CloudFormation** para automatizar a criação de um bucket no **Amazon S3** que dispara uma **Lambda Function** sempre que um novo arquivo é adicionado ao armazenamento.

---

## 🛠️ Tecnologias e Serviços Utilizados
*   **AWS CloudFormation**: Orquestração da infraestrutura como código (IaC).
*   **Amazon S3**: Armazenamento de objetos e gatilho de eventos.
*   **AWS Lambda**: Computação serverless para execução do código em resposta aos eventos.
*   **IAM (Identity and Access Management)**: Gerenciamento de permissões e roles de segurança.
*   **YAML / Python**: Linguagens utilizadas para o template e para a lógica da função.

---

## 📂 Estrutura do Repositório
*   `/templates/automation-stack.yaml`: Template CloudFormation com a stack completa.
*   `/src/index.py`: Script Python contendo a lógica da Lambda Function.
*   `README.md`: Documentação técnica e guia de aprendizado.

---

## 📝 Insights e Aprendizados
1.  **Event-Driven Architecture**: Compreensão de como desacoplar sistemas usando eventos do S3 para iniciar processos automáticos.
2.  **Segurança e IAM**: Aplicação do princípio de privilégio mínimo ao criar uma Role específica para a execução da Lambda.
3.  **Configuração de Triggers**: Aprendizado sobre a necessidade de conceder permissão explícita (`Lambda::Permission`) para que o serviço S3 possa invocar a função Lambda com sucesso.

---

## 💻 Código da Função Lambda (`src/index.py`)
Este é o código que será executado automaticamente:

```python
import json

def handler(event, context):
    print("Evento recebido do S3 com sucesso!")
    # Lógica para processar o arquivo recebido
    return {
        'statusCode': 200,
        'body': json.dumps('Sucesso no processamento serverless!')
    }
