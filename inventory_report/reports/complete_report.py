from datetime import datetime
from collections import Counter


class CompleteReport:
    @classmethod
    def generate(cls, inventory: list):
        minimum_year = min([i["data_de_fabricacao"] for i in inventory])
        closest_date = min(
            [
                i["data_de_validade"] for i in inventory
                if
                i["data_de_validade"] > datetime.now().strftime("%Y-%m-%d")
            ]
        )
        company, second = Counter(
            i["nome_da_empresa"] for i in inventory
        ).most_common()[0]

        comp_item = {}
        for i in inventory:
            if i["nome_da_empresa"] in comp_item:
                comp_item[i["nome_da_empresa"]] += 1
            else:
                comp_item[i["nome_da_empresa"]] = 1

        comp_list = [f"- {key}: {value}\n" for key, value in comp_item.items()]
        return (
            f"Data de fabricação mais antiga: {minimum_year}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}\n"
            f"Produtos estocados por empresa:\n"
            f"{''.join(comp_list)}"
        )
