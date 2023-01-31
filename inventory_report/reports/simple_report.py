from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, inventory: list):
        minimum_year = min([i["data_de_fabricacao"] for i in inventory])
        closest_date = min(
            [i["data_de_validade"]
                for i in inventory
                if i["data_de_validade"]
                > datetime.now().strftime("%Y-%m-%d")]
        )
        company, second = Counter(
            i["nome_da_empresa"]
            for i in inventory
        ).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {minimum_year}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )

# most common = lista de tuplas
# lembrando: tupla = (nome_da_empresa, quantidade)
# company, z = Counter(...).most_common()[0] está desempacotando
# a primeira tupla da lista e colocando em company.
#  o segundo fica armazenado em z
# POR ISSO NÃO RODOU SEM O SEGUNDO ELEMENTO DA TUPLA
