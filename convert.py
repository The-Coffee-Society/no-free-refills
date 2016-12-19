import csv
import sqlite3


def import_data(data_path, output_path):
    with open(data_path, 'rU') as csv_file:
        project_reader = csv.reader(csv_file)
        rows = []
        header_type = []
        for i, row in enumerate(project_reader):
            rows.append(row)
            if not i:
                header_type = [None for x in row]
            else:
                for j, header_type_val in enumerate(header_type):
                    if header_type_val is None:
                        curr_cell = row[j]
                        if curr_cell != '':
                            try:
                                float(curr_cell)
                                header_type[j] = "FLOAT"
                            except ValueError:
                                header_type[j] = "TEXT"

    conn = sqlite3.connect(output_path)
    conn.text_factory = str
    c = conn.cursor()

    columns_list = []
    for j in range(len(rows[0])):
        header_name = rows[0][j]
        this_header_type = header_type[j]
        columns_list.append('{} {}'.format(header_name, this_header_type))
    the_huge_columns_string = ', '.join(columns_list)
    info_string = 'CREATE TABLE data ({})'.format(the_huge_columns_string)
    c.execute(info_string)
    insert_statement = 'INSERT INTO data VALUES ({})'.format(','.join(['?' for x in header_type]))
    c.executemany(insert_statement, rows[1:])
    conn.commit()
    return

if __name__ == '__main__':
    import os
    import_data(os.path.join('Original Downloads from Kaggle', 'Speed Dating Data.csv'),
                'dating.db')
