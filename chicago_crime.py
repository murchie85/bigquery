# Author: Adam McMurchie
# Description: This code investigates chicago crime rates by doing some basic exploration first. 
# Building on top of kaggle tutorial


from google.cloud import bigquery


# create the object
client = bigquery.Client()


# Construct pointer
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# Fetch data
dataset = client.get_dataset(dataset_ref)



# print tables
tables = list(client.list_tables(dataset))
for table in tables:
    print(table.table_id)


print('Number of tables are ' + str(len(tables)))


# Point to one table only the crime table 
table_ref = dataset_ref.table('crime')

# Fetch data 
table = client.get_table(table_ref)

# printing info
print('Number of time stamps are :' + str(str(table.schema).count('TIMESTAMP')))
print('Number of INTEGERs are :' + str(str(table.schema).count('INTEGER')))
print('Number of NULLABLEs are :' + str(str(table.schema).count('NULLABLE')))
print('')
print(table.schema)


print('preview')
print(client.list_rows(table, max_results=10).to_dataframe())


fields_for_plotting = ['latitude', 'longitude'] 