FROM python:3.8

# Copie os arquivos necessários
COPY spiders/pedido_eletronico.py /app/pedido_eletronico.py
COPY entrypoint.sh /app/entrypoint.sh  
# Copie o script de inicialização

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências se estiver usando requirements.txt
COPY requirements.txt /app/requirements.txt  
# Se estiver usando um arquivo de requisitos
RUN pip install -r requirements.txt

# Certifique-se de que o script de inicialização seja executável
RUN chmod +x entrypoint.sh

# Comando de execução usando o script de inicialização
ENTRYPOINT ["./entrypoint.sh"]
