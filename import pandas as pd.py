import pandas as pd

url = 'view-source:https://www.floridahealth.gov/environmental-health/drinking-water/boil-water-notices/index.html'  # Replace with the actual URL
tables = pd.read_html(url)  # This will fetch all tables

# Assuming the table you need is the first one
df = tables[0]  