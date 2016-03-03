# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Polinya'

BUDGET_LOADER = 'PolinyaBudgetLoader'
PAYMENTS_LOADER = 'PolinyaPaymentsLoader'

FEATURED_PROGRAMMES = ['3340', '4910', '9120']

OVERVIEW_INCOME_NODES = [
                          {'label': 'Educació', 'nodes': '32'},
                          {'label': 'Cultura', 'nodes': '33'},
                          {'label': 'Esport', 'nodes': '34'},
                          {'label': 'Seguretat i mobilitat ciutadana', 'nodes': '13'},
                        ]
OVERVIEW_EXPENSE_NODES =  [
                            {'label': 'Deute', 'nodes': '01'},
                            {'label': 'Educació', 'nodes': '32'},
                            {'label': 'Cultura', 'nodes': '33'},
                            {'label': 'Esport', 'nodes': '34'},
                            {'label': 'Seguretat i mobilitat ciutadana', 'nodes': '13'},
                          ]

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
# OVERVIEW_RELAX_FACTOR = 0.5

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = True

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT        = False

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('ca', 'Catal&agrave;'),
  ('es', 'Castellano'),
)

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.ayto-polinya.es/presupuestos-municipales-2015'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2861'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10019&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.polinya.cat'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.polinya.cat/public/informacio-complementaria/avis-legal/'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.polinya.cat/public/informacio-complementaria/avis-legal/#galetes'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]
