import pandas as pd

# global variables 
CSV_FILE_ADDRESS = 'sample-data.csv'
FEATHER_FILE_ADDRESS = 'sample-data.feather'

# read CSV file and store it in a PANDAS's dataframe
dataframe = pd.read_csv(CSV_FILE_ADDRESS)

# save the PANDAS's dataframe into a FEATHER file
dataframe.to_feather(FEATHER_FILE_ADDRESS)


print('done')


# to read a FEATHER file, do:
# import feather
# dd=feather.read_dataframe(FEATHER_FILE_ADDRESS)