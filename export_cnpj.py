import requests
import pandas as pd
import json
from datetime import datetime
from time import sleep
from tqdm import tqdm
URL = 'https://brasilapi.com.br/api/cnpj/v1/'

print('''
Create by: Leewan Meneses

███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗     ██████╗███╗   ██╗██████╗     ██╗
██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝████╗  ██║██╔══██╗    ██║
█████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║       ██║     ██╔██╗ ██║██████╔╝    ██║
██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║       ██║     ██║╚██╗██║██╔═══╝██   ██║
███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║       ╚██████╗██║ ╚████║██║    ╚█████╔╝
╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═══╝╚═╝     ╚════╝ 
                                                                                       
                                                                                       ''')

print('Please wait while the information is updated... \n')
try:
    file_cnpj = open('cnpj.txt','r')
    list_cnpj = file_cnpj.readlines()
    file_cnpj.close()
except:
    print("Arquivo 'cnpj.txt' não localizado.")
    quit()
data_export = {}
ret = False
for i in tqdm(range(10)):
    for cnpj in list_cnpj:
        try:
            res_cnpj = requests.get(URL+str(cnpj))
            if res_cnpj.status_code == 200:
                json_cnpj = res_cnpj.text
                data_cnpj = json.loads(json_cnpj)
                new_json = {}
                for data in data_cnpj:
                    if not isinstance(data_cnpj[data], list):
                        new_json[data] = data_cnpj[data]
                data_export[cnpj] = new_json
                ret = True
            else:
                data_export[cnpj] = 'Ocorreu algum erro ao buscar o CNPJ: Codigo do Erro: ' + str(res_cnpj.status_code)
        except:
            data_export[cnpj] = 'Ocorreu algum erro ao buscar o CNPJ: Codigo do Erro: 0'
            continue
        

if ret:
    df = pd.DataFrame.from_dict(data_export, orient='index')
    now = datetime.now()
    sufix = now.strftime("%Y%m%d_%H%M%S")
    df.to_excel('cnpj_export_' + str(sufix) + '.xlsx')
