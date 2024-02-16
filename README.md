### Aplicação backend

Essa aplicação é uma API que possui 3 rotas:

1. ***/health***: Essa rota retorna um JSON e status HTTP 200. Exemplo:
```sh
$ curl -XGET http://localhost:5000/health
{"status":"ok"}
```
2. ***/consulta_cep***: Essa rota retorna informações a respeito de um determinado CEP como nome do logradouro, cidade e estado. Exemplo:
```sh
$ curl -XGET http://localhost:5000/consulta_cep?cep=05763340
{
    "bairro": "Jardim Piracuama",
    "cep": "05763-340",
    "complemento": "",
    "ddd": "11",
    "gia": "1004",
    "ibge": "3550308",
    "localidade": "S\u00e3o Paulo",
    "logradouro": "Rua Eug\u00eanio Pradez",
    "siafi": "7107",
    "uf": "SP"
}
```
3. ***cotacao***: Esse rota retorna dados sobre a cotação de uma determinada moeda em relação a outra. Exemplo:
```sh
$ curl -XGET http://localhost:5000/cotacao?moeda1=USD&moeda2=BRL
{
    "USDBRL": {
        "ask": "4.9675",
        "bid": "4.9665",
        "code": "USD",
        "codein": "BRL",
        "create_date": "2024-02-16 18:30:03",
        "high": "4.9892",
        "low": "4.9598",
        "name": "D\u00f3lar Americano/Real Brasileiro",
        "pctChange": "-0.12",
        "timestamp": "1708119003",
        "varBid": "-0.0062"
    }
}
```
