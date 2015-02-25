import csv

MY_FILE = '/home/rebeldroid12/new-coder/dataViz/data/sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""
    # Open CSV file
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field->value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

     # Close the CSV file
    opened_file.close() 


    # Close the CSV file
    return parsed_data


def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    # Let's see what the data looks like!
    print new_data

if __name__ == "__main__":
    main()
