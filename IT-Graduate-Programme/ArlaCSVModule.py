import os
import csv
#import time

def process_csv_files(storage_location, delimiter):
    #Used for comparing CSV Module run time to Pandas run time
    #start_time = time.time()
    csv_files = [file for file in os.listdir(storage_location) if file.endswith('.csv')]
    
    if not csv_files:
        print("Can't find any CSV files in the specified location")
        return

    for csv_file in csv_files:
            file_path = os.path.join(storage_location, csv_file)

            with open(file_path, 'r', encoding='utf-8') as input_file:
                reader = csv.reader(input_file, delimiter=delimiter)
                header = next(reader)
                print(f"\nData types for {csv_file}:")

                for col, data_type in zip(header, zip(*reader)):
                    print(f"{col}: {set(map(type, data_type))}")

            new_file_path = os.path.join("ProcessedCSVS", f"processed_{csv_file.replace('.csv', '_output.csv')}")
            
            with open(new_file_path, 'w', newline='', encoding='utf-8') as output_file:
                writer = csv.writer(output_file, delimiter='|')
                writer.writerow(header)

                with open(file_path, 'r', encoding='utf-8') as input_file:
                    reader = csv.reader(input_file, delimiter=delimiter)
                    next(reader)
                    for row in reader:
                        writer.writerow(row)

    print(f"\nData saved to {new_file_path} with '|' as the separator.")

    #end_time = time.time()
    #elapsed_time = end_time - start_time
    #print(f"\nTotal time taken: {elapsed_time:.2f} seconds")

storage_location = input("Input path to folder containing CSV files: ")
delimiter = input("Input the delimiter type used in the CSV files: ")

process_csv_files(storage_location, delimiter)
