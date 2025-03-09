# Portfolio Rebalancer

This GUI application, written in Python/QT (PySide6), is designed to help rebalance the distribution of stock holdings within a portfolio.
To achieve this, a target percentage allocation for the portfolio holdings, as well as the desired total monthly savings amount, is initially defined.
Based on these values, the savings amounts for individual holdings are rounded up or down to whole numbers.

Reports generated at the end of the year capture the actual stock values and highlight deviations from the target allocation.
Additionally, they propose the monthly savings amounts per holding for the following year—without considering returns—
to restore the intended portfolio allocation over the entire savings year.

## GUI

### Convert UI to python class
Example: `pyside6-uic -g python form.ui > ui_form.py`