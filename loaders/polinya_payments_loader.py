# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
import datetime

class PolinyaPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):
        # The date is not always available
        try:
            date=datetime.datetime.strptime(line[0], "%Y-%m-%d")
        except ValueError:
            date=None

        # There are some incomplete lines. Return an empty record.
        area = line[3].strip()
        if area == '':
            return { 'amount': 0 }

        return {
            'area': area,
            'fc_code': '',
            'ec_code': line[5],
            'date': date,
            'payee': self._titlecase(line[6].strip()),
            'description': self._spanish_titlecase(line[7].strip()),
            'amount': self._read_english_number(line[1])
        }
