from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            return Inventory.open_csv(path, type)

    @classmethod
    def open_csv(cls, path, type):
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(reader))
            if type == "completo":
                return CompleteReport.generate(list(reader))
            else:
                raise ValueError("Tipo inválido")
