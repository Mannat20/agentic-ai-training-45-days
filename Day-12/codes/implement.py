from user import user
from fileHelper import fileHelper 
from dbHelper import DBHelper
def main():
    user1=user()
    user1.input_details()
    user1.show()

    csv_data=user1.to_csv()
    dict_data=user1.to_dictionary()

    print(csv_data)
    print(dict_data)
    # filehelper1=fileHelper()
    # filehelper1.write_in_file(csv_data)
    # filehelper1.close_file()


    dbhelper=DBHelper()
    dbhelper.select_collection()
    dbhelper.save_document(dict_data)
if __name__ == '__main__':
    main()