import httpx

class CoinConversorServices:
    
    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/last/'

    def converter(self, coin_origin, coin_target):
        try:
            response = httpx.get(
            url= f'{self.__base_url}/{coin_origin}-{coin_target}'
            )
            if response.status_code == 404:
                return response.json().get('message')

            response.raise_for_status()

            return response.json().get(f'{coin_origin}{coin_target}').get('bid')
        except httpx.HTTPStatusError as e:
            return f'Erro de servidor ou requisição: {e.response.status_code}'
        except httpx.HTTPError as e:
            return f'Erro de conexão: Não chegou no servidor'
        except Exception as e:
            return f'Erro: {e}'