# DESAFIOS COTE FÁCIL PYTHON

## Tecnologias

- Python
- Scrapy
- Selenium
- Docker

## Instruções para execução
1) É necessário ter instalado o Docker. Você pode instalar [clicando aqui](https://www.docker.com/get-started/)
2) Poderá clonar meu repositório ou fazer download.
      ```
      git clone  https://github.com/LanghiDev/python-challenges-cotefacil.git
      ```

3) Acessar o diretório onde estiver o arquivo "Dockerfile" de cada desafio (se este possuir)
4) Executar no terminal:
     ```
      docker run (imagem)
     ```

      _Obs.: O desafio 2 possui parâmetros, deixando o comando da seguinte maneira:_ 
        ```
        docker run (imagem) <num_pedido>
        ```
<br>

5) Imagens a serem aplicadas nos comandos docker:
   - Desafio 2: pedido-servimed
   - Desafio 3: (anulado)
   - Desafio 4: python-ftp-scripts
   - Desafio 5: company-tree

<Br><br>

## Observações

- Não há disponível o desafio 1.
- O processo do desafio 2 apenas passou da autenticação, mas toda sua lógica do procedimento da aquisição do número do pedido fornecido está disponível.
- O desafio 6, utilizando Selenium, só funciona com o navegador visível. Por isso, não foi implementado no Docker. Mas para executá-lo, basta ter os requisitos:

          ```
          Python 3.8+
          Google Chrome

          # Rodar no terminal, no mesmo caminho do arquivo .py:
          pip install Selenium
          pip install webdriver_manager

          python questao6.py
          ```


## Obrigado!
