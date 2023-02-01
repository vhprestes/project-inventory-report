from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            return Inventory.open_csv(path, type)
        if "json" in path:
            return Inventory.open_json(path, type)
        if "xml" in path:
            return Inventory.open_xml(path, type)

    @classmethod
    def open_csv(cls, path, type):
        with open(path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(data))
            if type == "completo":
                return CompleteReport.generate(list(data))
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_json(cls, path, type):
        with open(path) as file:
            data = json.load(file)
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_xml(cls, path, type):
        with open(path) as file:
            data = xmltodict.parse(file.read())['dataset']['record']
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)
            else:
                raise ValueError("Tipo inválido")
