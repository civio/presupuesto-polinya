import six

if six.PY2:
    from polinya_budget_loader import PolinyaBudgetLoader
    from polinya_payments_loader import PolinyaPaymentsLoader
else:
    from .polinya_budget_loader import PolinyaBudgetLoader
    from .polinya_payments_loader import PolinyaPaymentsLoader
