from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "1",
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    assert ("1" in product.__repr__()) is True
    assert ("Nicotine Polacrilex" in product.__repr__()) is True
    assert ("Target Corporation" in product.__repr__()) is True
    assert ("2021-02-18" in product.__repr__()) is True
    assert ("2023-09-17" in product.__repr__()) is True
    assert ("instrucao 1" in product.__repr__()) is True
