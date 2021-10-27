import importlib
from .banks import BaseBank
from BaseDRF.settings import BANK_CLASS


class BankFactory:
    def __init__(self):
        self._banks = BANK_CLASS

    def _import_bank(self, bank_class: str):
        bank = self._banks[bank_class]
        package, attr = bank.rsplit(".", 1)
        bank = getattr(importlib.import_module(package), bank_class)
        return bank

    def create(self, bank_class: str) -> BaseBank:
        bank_klass = self._import_bank(bank_class)
        bank = bank_klass()
        return bank
