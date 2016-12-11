import csv
import sqlite3


def import_data(data_path, output_path):
    with open(data_path, 'rU') as csv_file:
        project_reader = csv.reader(csv_file)
        rows = []
        for row in project_reader:
            rows.append(row)

    conn = sqlite3.connect(output_path)
    c = conn.cursor()

    return

if __name__ == '__main__':
    import os
    import_data(os.path.join('Original Downloads from Kaggle', 'Speed Dating Data.csv'),
                'dating.db')
