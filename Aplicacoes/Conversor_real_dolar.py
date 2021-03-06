import requests # primeiro, é necessario importar a biblioteca request

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

print(req.status_code)

# '200' -  a resposta dever ser '200' para confirmar que o acesso a url foi bem sucedido

dados = req.json() # para coletar os dados da pagina

print(dados)
'''
O resultado será:
{'result': 'success', 'provider': 'https://www.exchangerate-api.com', 'documentation': 'https://www.exchangerate-api.com/docs/free',
'WARNING_NEW_ENDPOINT': 'Swap *api.exchangerate-api.com* with *open.er-api.com* for better servers!', 
'terms_of_use': 'https://www.exchangerate-api.com/terms', 'time_last_update_unix': 1626393751, 'time_last_update_utc': 'Fri, 16 Jul 2021 00:02:31 +0000',
'time_next_update_unix': 1626481261, 'time_next_update_utc': 'Sat, 17 Jul 2021 00:21:01 +0000', 'time_eol_unix': 0, 'base_code': 'USD', 
'rates': {'USD': 1, 'AED': 3.67, 'AFN': 80.17, 'ALL': 103.69, 'AMD': 495.52, 'ANG': 1.79, 'AOA': 647.8, 'ARS': 96.22, 'AUD': 1.34, 'AWG': 1.79,
'AZN': 1.7, 'BAM': 1.65, 'BBD': 2, 'BDT': 84.79, 'BGN': 1.65, 'BHD': 0.376, 'BIF': 1970.82, 'BMD': 1, 'BND': 1.35, 'BOB': 6.89, 'BRL': 5.08,
'BSD': 1, 'BTN': 74.54, 'BWP': 11.03, 'BYN': 2.55, 'BZD': 2, 'CAD': 1.25, 'CDF': 1978.53, 'CHF': 0.917, 'CLP': 746.8, 'CNY': 6.46, 'COP': 3792.21,
'CRC': 619.34, 'CUC': 1, 'CUP': 25.75, 'CVE': 93.11, 'CZK': 21.68, 'DJF': 177.72, 'DKK': 6.3, 'DOP': 56.92, 'DZD': 134.6, 'EGP': 15.68, 'ERN': 15,
'ETB': 43.84, 'EUR': 0.845, 'FJD': 2.07, 'FKP': 0.722, 'FOK': 6.3, 'GBP': 0.722, 'GEL': 3.13, 'GGP': 0.722, 'GHS': 5.93, 'GIP': 0.722, 'GMD': 51.8,
'GNF': 9773.06, 'GTQ': 7.73, 'GYD': 208.38, 'HKD': 7.77, 'HNL': 23.91, 'HRK': 6.36, 'HTG': 93.61, 'HUF': 304.56, 'IDR': 14556.02, 'ILS': 3.28,
'IMP': 0.722, 'INR': 74.54, 'IQD': 1453.15, 'IRR': 41844.52, 'ISK': 123.54, 'JMD': 153.73, 'JOD': 0.709, 'JPY': 109.93, 'KES': 108.14, 
'KGS': 84.38, 'KHR': 4054.24, 'KID': 1.34, 'KMF': 415.44, 'KRW': 1143.75, 'KWD': 0.3, 'KYD': 0.833, 'KZT': 426.31, 'LAK': 9481.3, 'LBP': 1507.5,
'LKR': 198.9, 'LRD': 171.76, 'LSL': 14.56, 'LYD': 4.49, 'MAD': 8.95, 'MDL': 18.02, 'MGA': 3874.34, 'MKD': 52.1, 'MMK': 1645.75, 'MNT': 2838.26, 
'MOP': 8, 'MRU': 35.99, 'MUR': 42.94, 'MVR': 15.41, 'MWK': 807.55, 'MXN': 19.94, 'MYR': 4.2, 'MZN': 63.73, 'NAD': 14.56, 'NGN': 424.48, 'NIO': 35.18,
'NOK': 8.79, 'NPR': 119.27, 'NZD': 1.43, 'OMR': 0.384, 'PAB': 1, 'PEN': 3.96, 'PGK': 3.52, 'PHP': 50.24, 'PKR': 159.23, 'PLN': 3.88, 'PYG': 6820.45,
'QAR': 3.64, 'RON': 4.17, 'RSD': 99.43, 'RUB': 74.14, 'RWF': 1004.74, 'SAR': 3.75, 'SBD': 7.9, 'SCR': 14.51, 'SDG': 440.9, 'SEK': 8.66, 'SGD': 1.35,
'SHP': 0.722, 'SLL': 10210.27, 'SOS': 576.25, 'SRD': 21.13, 'SSP': 177.51, 'STN': 20.69, 'SYP': 1457.21, 'SZL': 14.56, 'THB': 32.7, 'TJS': 11.33,
'TMT': 3.49, 'TND': 2.78, 'TOP': 2.24, 'TRY': 8.57, 'TTD': 6.78, 'TVD': 1.34, 'TWD': 27.96, 'TZS': 2314.46, 'UAH': 27.3, 'UGX': 3542.23, 'UYU': 43.85,
'UZS': 10717.45, 'VES': 3401263.72, 'VND': 22977.87, 'VUV': 110.25, 'WST': 2.55, 'XAF': 553.92,
'XCD': 2.7, 'XDR': 0.702, 'XOF': 553.92, 'XPF': 100.77, 'YER': 250.92, 'ZAR': 14.56, 'ZMW': 22.63}}
'''
# São valores de diversas moedas em comparação com o dolar

valor_reais = float(input('informe o valor em R$ a ser convertido\n'))
cotacao = dados ['rates']['BRL'] # dentro de rates vou coletar o valor de BRL
print(f'O dolar está custando R${cotacao} \nEntão, R${valor_reais} em dolares valem US${(valor_reais/cotacao):2f}')
'''
informe o valor em R$ a ser convertido
10
O dolar está custando R$5.08 
Então, R$10.0 em dolares valem US$1.968504
'''
