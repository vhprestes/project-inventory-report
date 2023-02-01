from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = xmltodict.parse(file.read())['dataset']['record']
            return data
