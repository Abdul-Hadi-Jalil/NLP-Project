import csv
import os

def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        for line in infile:
            line = line.strip().split()  # Split line into a list of values
            writer.writerow(line)  # Write the list as a row in the CSV

def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as infile, open(txt_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)

        for line in reader:
            line = ' '.join(line)
            outfile.write(line + '\n')

def main():
    input_file = input("Enter the name of the file you want to convert (e.g., input.txt): ")
    output_file = input("Enter the name of the output file (e.g., output.csv): ")

    if input_file.endswith('.txt') and output_file.endswith('.csv'):
        try:
            if not os.path.exists(input_file):
                print(f"Error: The file '{input_file}' does not exist.")
                return

            txt_to_csv(input_file, output_file)
            print("File successfully converted to CSV.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("The given format is not supported for conversion.")

if __name__ == "__main__":
    main()
