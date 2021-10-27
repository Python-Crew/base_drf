from __future__ import absolute_import, unicode_literals
import importlib
import logging
from .banks import BaseBank
from BaseDRF.settings import BANK_CLASS


class BankFactory:
    def __init__(self):
        self._banks = BANK_CLASS

    def _import_bank(self, bank_class: str):
        bank = self._banks[bank_class]
        print(bank)
        package, attr = bank.rsplit(".", 1)
        print(package)
        print(attr)
        bank = getattr(importlib.import_module(package), bank_class)

        print(bank)
        logging.debug("Import bank class")

        return bank

    def create(self, bank_class: str) -> BaseBank:
        """Build bank class"""

        bank_klass = self._import_bank(bank_class)
        bank = bank_klass()

        logging.debug("Create bank")
        return bank
