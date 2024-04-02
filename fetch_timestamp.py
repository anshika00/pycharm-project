import csv
import pandas as pd
import datetime

file_path1 = "/home/nineleaps/Downloads/20240305124003123456_Extract 2/20240305124003123456_Extract.zip/sample2.csv"
file_path2 = "/home/nineleaps/Downloads/20240305124003123456_Extract 2/20240305124003123456_Extract.zip/sample.csv"


timestamp_data = pd.read_csv(file_path2)
# print(timestamp_data)
unix_timestamp = timestamp_data.InteractionId
timestamp_datetime= unix_timestamp.apply(lambda x: datetime.datetime.utcfromtimestamp(x))
print(timestamp_datetime)

for file_path in [file_path1,file_path2]:  # Specify your CSV file paths here
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Add the new column with respective values
    df['load_timestamp'] = timestamp_datetime
    df.to_csv(file_path, index=False)
    print(f"New column added to '{file_path}'")

    # Save the updated DataFrame back to the CSV file
    # updated_file_path = file_path.replace('.csv', '_updated.csv')  # Append '_updated' to the file name
    # df.to_csv(updated_file_path, index=False)

    # print(f"New column added to '{file_path}' and saved as '{updated_file_path}'")




