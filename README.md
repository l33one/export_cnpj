# EXECUTANDO EM SISTEMAS LINUX E MACOS
Adicione os CNPJs no arquivo cnpj.txt e salve

Execute o script python via terminal, prompt de comando ou como preferir

    python export_cnpj.py
    
Será gerado um arquivo excel na mesma pasta com os dados dos CNPJs coletados do site Brasil APIs.


nomenclatura do arquivo: cnpj_export_yyyymmdd_hhmmss.xlsx, onde:

    yyyy: Ano com 4 digitos, ex. 2023
    mm: Mês com 2 dígitos, ex. 02
    dd: Dia com 2 dígitos, ex. 11
    hh: Hora no formato 24h, ex. 23
    mm: Minutos com 2 dígitos
    ss: Segundos com 2 dígitos
    obs. Será usado o fuso horário do computador que executar o script.

Exemplo completo: cnpj_export_20230127_175001.xlsx



# EXECUTANDO EM SISTEMAS WINDOWS

Abrir a pasta "dist"

Adicionar os CNPJs no arquivo cnpj.exe e salvar.

Executar o arquivo export_cnpj.exe

Será gerado um arquivo excel na mesma pasta com os dados dos CNPJs coletados do site Brasil APIs.

nomenclatura do arquivo: cnpj_export_yyyymmdd_hhmmss.xlsx, onde:

    yyyy: Ano com 4 digitos, ex. 2023
    mm: Mês com 2 dígitos, ex. 02
    dd: Dia com 2 dígitos, ex. 11
    hh: Hora no formato 24h, ex. 23
    mm: Minutos com 2 dígitos
    ss: Segundos com 2 dígitos
    obs. Será usado o fuso horário do computador que executar o script.

Exemplo completo: cnpj_export_20230127_175001.xlsx



## Para distribuir o arquivo para Windows basta compartilhar o arquivo "export.cnpj.rar" da pasta "dist"

