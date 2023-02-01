from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = json.load(file)
            return data
