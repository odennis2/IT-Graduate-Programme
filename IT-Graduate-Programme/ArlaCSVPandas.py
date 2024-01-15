import os
import pandas as pd
#import time

def process_csv_files(storage_location, delimiter):
    # Used for comparing Pandas run time to CSV Module run time
    #start_time = time.time()
    csv_files = [file for file in os.listdir(storage_location) if file.endswith('.csv')]

    if not csv_files:
        print("Can't find any CSV files in the specified location")
        return

    for csv_file in csv_files:
        file_path = os.path.join(storage_location, csv_file)
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"\nDataFrame for {csv_file}:")
        print(df.dtypes)

        new_file_path = os.path.join("ProcessedCSVS", f"processed_{csv_file.replace('.csv', '_output.csv')}")
        df.to_csv(new_file_path, sep='|', index=False)
        print(f"\nDataFrame saved to {new_file_path} with '|' as the separator.")
        
    #end_time = time.time()
    #elapsed_time = end_time - start_time
    #print(f"\nTotal time taken: {elapsed_time:.2f} seconds")

storage_location = input("Input path to folder containing CSV files: ")
delimiter = input("Input the delimiter type used in the CSV files: ")

process_csv_files(storage_location, delimiter)
