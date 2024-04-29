import requests

def validar_html(html_file):
    # URL da API de validação do W3C Markup Validation Service
    url = "https://validator.w3.org/nu/?out=json"
    
    # Cabeçalhos da solicitação HTTP
    headers = {
        "Content-Type": "text/html; charset=utf-8"
    }
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Dados da solicitação HTTP (HTML a ser validado)
    data = html
    
    # Enviar solicitação HTTP para a API de validação
    response = requests.post(url, headers=headers, data=data)
    
    # Processar a resposta JSON
    result = response.json()
    
    # Verificar se o HTML é válido
    if result["messages"]:
        print("O HTML não é válido:")
        for message in result["messages"]:
            print(f"- {message['message']}")
    else:
        print("O HTML é válido.")

# HTML a ser validado
html_file = "testeH.html"

# Chamada da função de validação
validar_html(html_file)