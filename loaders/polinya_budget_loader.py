# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class PolinyaBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    def parse_item(self, filename, line):
        if line[0]=='':
            return;

        # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
        # mapping to be constant over time, we are forced to amend budget data prior to 2015.
        # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
        programme_mapping = {
            # old programme: new programme
            '1340': '1350',
            '1550': '1530',
            '1600': '1601',
            '2400': '2410',
            '3100': '3110',
            '3130': '3110',
            '3210': '3230',
            '3230': '3260',
            '3240': '3260',
            '3310': '3300',
            '3320': '3321',
            '4590': '4599',
            '9230': '9232',
            '9290': '9299',
        }

        # Some inconsistencies in 2015- also
        programme_mapping_post_2014 = {
            # old programme: new programme
            '1521': '1500',
            '1610': '1600',
            '9292': '4510',
            '9291': '4590',
            '4590': '4599'
        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            # We got 3-digit functional codes as input (mostly), so we make them all
            # into 4-digit ones by adding an extra zero, i.e. left-justify them adding a 0.
            # Note: later, in2csv started removing the leading zero, so we add it first if needed.
            fc_code = line[1].zfill(3).ljust(4, '0')

            # Institutional codes are 2-digits, we expect them to be 3-digits.
            # We add a leading zero, this will make code '0' the root, the city hall.
            ic_code = line[0].rjust(3, '0')

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)
            else:
                fc_code = programme_mapping_post_2014.get(fc_code, fc_code)

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': line[2][:-2],        # First three digits (everything but last two)
                'ic_code': ic_code,
                'item_number': line[2][-2:],    # Last two digits
                'description': line[3],
                'amount': self._parse_amount(line[7 if is_actual else 6])
            }

        else:
            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': line[0][:-2],        # First three digits (everything but last two)
                'ic_code': '000',               # All income goes to the root node
                'item_number': line[0][-2:],    # Last two digits
                'description': line[1],
                'amount': self._parse_amount(line[5 if is_actual else 4])
            }
