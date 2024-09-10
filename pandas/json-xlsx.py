import pandas as pd

json_file = 'data.json'

data_frame = pd.read_json(json_file)

excel_file = 'data.xlsx'
data_frame.to_excel(excel_file, index=False)
