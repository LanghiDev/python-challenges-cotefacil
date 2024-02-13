import scrapy
import json
import argparse

class PedidoEletronicoSpider(scrapy.Spider):
    name = "pedido_eletronico"
    allowed_domains = ['pedidoeletronico.servimed.com.br', 'peapi.servimed.com.br']
    start_urls = ["https://peapi.servimed.com.br/api"]

    def __init__(self, *args, **kwargs):
        super(PedidoEletronicoSpider, self).__init__(*args, **kwargs)
        
        # Configurando o parser de argumentos
        parser = argparse.ArgumentParser()
        parser.add_argument('pharmRequestCode', help='Código do pedido servimed')

        # Obtendo os argumentos da linha de comando
        args = parser.parse_args()
        self.pharmRequestCode = args.pharmRequestCode
    
    def parse(self, response):
        self.log(f'Pedido solicitado: {self.pharmRequestCode}')
        urlApi = 'https://peapi.servimed.com.br/api/usuario/login'

        formdataDict = {
            'usuario': 'juliano@farmaprevonline.com.br',
            'senha': 'a007299A'
        }

        yield scrapy.Request(
            url=urlApi,
            method='POST',
            headers={'Content-Type': 'application/json'},
            body=json.dumps(formdataDict),
            callback=self.after_login
        )
    
    def after_login(self, response):
        if response.status == 200:
            self.log('Login realizado com sucesso!')
            
            urlMenu = 'https://peapi.servimed.com.br/api/Menu/1'

            headers = {
                ':authority': 'peapi.servimed.com.br',
                ':method': 'GET',
                ':path': '/api/Menu/1',
                ':scheme': 'https',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q=0.9',
                'Accesstoken': '8e7c74d0-ca8b-11ee-b31e-81f27c1028b2',
                'Contenttype': 'application/json',
                'Cookie': '_gid=GA1.3.1089322417.1707764890; _ga_TGSHLZ7V8G=GS1.3.1707802245.2.1.1707802288.0.0.0; _ga=GA1.3.1893471441.1707269471; _gat=1; _gat_gtag_UA_149227611_1=1; sessiontoken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4ZTdjNzRkMC1jYThiLTExZWUtYjMxZS04MWYyN2MxMDI4YjIiLCJpYXQiOjE3MDc4NDExMjMsImV4cCI6MTcwNzg4NDMyMywiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.lsUc2Qn0QphQvGueU00a20zDkvAJBCk3lXagsJCswXNYMil0XgQjr0XhSUv8f2hRd_WtUE4wYWzgDvSIv8Jbnw; accesstoken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4ZTdjNzRkMC1jYThiLTExZWUtYjMxZS04MWYyN2MxMDI4YjIiLCJpYXQiOjE3MDc4NDExMjMsImV4cCI6MTcwNzg4NDMyMywiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.lsUc2Qn0QphQvGueU00a20zDkvAJBCk3lXagsJCswXNYMil0XgQjr0XhSUv8f2hRd_WtUE4wYWzgDvSIv8Jbnw; _ga_0684EZD6WN=GS1.3.1707836776.15.1.1707841833.0.0.0',
                'Loggeduser': '22850',
                'Origin': 'https://pedidoeletronico.servimed.com.br',
                'Referer': 'https://pedidoeletronico.servimed.com.br/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            }

            yield scrapy.Request(
                url=urlMenu,
                headers=headers,
                callback=self.menu
            )
        
        else:
            self.log('Falha no login ;(')
    
    def menu(self, response):
        if response.status == 200:
            self.log('Seção de Menu.')

            urlApi = 'https://peapi.servimed.com.br/api/Pedido'

            formdataDict = {
                "dataInicio": "",
                "dataFim": "",
                "filtro": self.pharmRequestCode,
                "pagina": 1,
                "registrosPorPagina": 10,
                "codigoExterno": 518565,
                "codigoUsuario": 22850,
                "kindSeller": 0,
                "users": [
                    518565,
                    267511
                ]
            }

            headers = {
                ':authority': 'peapi.servimed.com.br',
                ':method': 'POST',
                ':path': '/api/Pedido',
                ':scheme': 'https',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q=0.9',
                'Accesstoken': '8e7c74d0-ca8b-11ee-b31e-81f27c1028b2',
                'Content-Length': '161',
                'Content-Type': 'application/json',
                'Contenttype': 'application/json',
                'Cookie': '_gid=GA1.3.1089322417.1707764890; _ga_TGSHLZ7V8G=GS1.3.1707802245.2.1.1707802288.0.0.0; _ga=GA1.3.1893471441.1707269471; _gat=1; sessiontoken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4ZTdjNzRkMC1jYThiLTExZWUtYjMxZS04MWYyN2MxMDI4YjIiLCJpYXQiOjE3MDc4NDE2OTgsImV4cCI6MTcwNzg4NDg5OCwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.QcEFGs3MIo7AXt2jRgVH-I770UYViLC73Jjot08zOMwjwy6MBlsVVqySgsFVlCju9kES44p-duKtLm9H3rrMOQ; accesstoken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4ZTdjNzRkMC1jYThiLTExZWUtYjMxZS04MWYyN2MxMDI4YjIiLCJpYXQiOjE3MDc4NDE2OTgsImV4cCI6MTcwNzg4NDg5OCwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.QcEFGs3MIo7AXt2jRgVH-I770UYViLC73Jjot08zOMwjwy6MBlsVVqySgsFVlCju9kES44p-duKtLm9H3rrMOQ; _ga_0684EZD6WN=GS1.3.1707836776.15.1.1707842415.0.0.0',
                'Loggeduser': '22850',
                'Origin': 'https://pedidoeletronico.servimed.com.br',
                'Referer': 'https://pedidoeletronico.servimed.com.br/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            }

            yield scrapy.Request(
                url=urlApi,
                method='POST',
                headers=headers,
                body=json.dumps(formdataDict),
                callback=self.pharmRequest
            )

        else:
            self.log('Sem acesso ao Menu.')

    def pharmRequest(self, response):
        if response.status == 200:
            self.log('Seção de pedidos.')
            
            urlApi = f'https://peapi.servimed.com.br/api/Pedido/ObterTodasInformacoesPedidoPendentePorId/{self.pharmRequestCode}'

            yield scrapy.Request(
                url=urlApi,
                callback=self.pharmRequestSelec
            )
        else:
            self.log('Sem acesso aos pedidos.')

    def pharmRequestSelec(self, response):
        if response.status == 200:
            self.log('Pedido encontrado!')
            
            pharmReqJson = json.loads(response.text)
            
            motivo = pharmReqJson['rejeicao'].strip()
            produtos = []

            for p in pharmReqJson['itens']:
                produtos.append({
                    'codigo_produto': p['produtoCodigoExterno'],
                    'descricao': p['produto']['descricao'].strip(),
                    'quantidade_faturada': p['quantidadeFaturada']
                })

            retornoFaturamento = {
                'motivo': motivo,
                'itens': produtos
            }

            retornoFaturamentoJson = json.dumps(retornoFaturamento)

            print(retornoFaturamentoJson)

            with open('retornoFaturamento.json', 'w') as f:
                f.write(retornoFaturamentoJson)

        else:
            raise Exception('ERRO: Pedido não encontrado...')


if __name__ == '__main__':
    # Inicializa o spider com os argumentos da linha de comando
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()

    # Executando o spider
    process.crawl(PedidoEletronicoSpider)
    process.start()
