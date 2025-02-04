import csv
from tinydb import TinyDB, Query

def read_csv(file_path):
    # Read and parse the CSV file
    try :
        data = []
        f = open (file_path,mode='r', encoding='utf-8',newline='')
    
        reader = csv.DictReader(f)
    
        for i in reader:
            data.append(i)
        f.close()
        return data
    except FileNotFoundError:
        raise ValueError('[|]')

def insert_into_db(data, db_path=None):
    if db_path == None or not data:
        raise ValueError("ValueError")
    
    db = TinyDB(db_path)
    for i in data:
        db.insert(i)
    return db.all()

def query_db(db_path, query_field, query_value):
    # Query the database
    pass

if __name__ == "__main__":
    # Main execution logic
    pass