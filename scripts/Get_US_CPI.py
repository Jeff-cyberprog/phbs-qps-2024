import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(parent_dir)

from src import utils

cpi_data = utils.fetch_us_cpi()
print(cpi_data)
last_4_quarters_inflation = utils.calculate_inflation(cpi_data)
print("the inflation of last four quarters is: ")
print(last_4_quarters_inflation)

cpi_data.to_csv(os.path.join(parent_dir, "data", "cpi_data.csv"))
last_4_quarters_inflation.to_csv(os.path.join(parent_dir, "data", "last_4_quarters_inflation.csv"))
