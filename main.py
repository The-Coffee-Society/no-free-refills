import convert as data_loader
import os


path_to_sqlite_data = 'dating.db'


def main():
    if not os.path.exists(path_to_sqlite_data):
        print('You don\'t have a database yet!')
        csv_location = os.path.join('Original Downloads from Kaggle', 'Speed Dating Data.csv')
        data_loader.import_data(csv_location, path_to_sqlite_data)



if __name__ == '__main__':
    main()
