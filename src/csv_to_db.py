import csv
from tinydb import TinyDB, Query
import argparse

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
        raise ValueError(".'.")
    
    db = TinyDB(db_path)
    for i in data:
        db.insert(i)
    return db.all()
    


def query_db(db_path, query_field=None, query_value=None):
    db = TinyDB(db_path)
    query = Query()
    
    if query_field and query_value:
        if query_field == 'id':
            result = db.search(query.id == query_value)
        elif query_field == 'first_name':
            result = db.search(query.first_name == query_value)
        elif query_field == 'last_name':
            result = db.search(query.last_name == query_value)
        elif query_field == 'email':
            result = db.search(query.email == query_value)
        elif query_field == 'gender':
            result = db.search(query.gender == query_value)
        elif query_field == 'job':
            result = db.search(query.job == query_value)
        else:
            result = []
    else:
        result = db.all()
    
    return result


def main(csv_file, db_path):
    """
    csv_file va db_path parametrlarini qabul qiladi va CSV fayldagi ma'lumotlarni TinyDB bazasiga yuklaydi.
    
    Ushbu funksiya buyruq satri argumentlaridan foydalanmaydi,
    shuning uchun test muhitida yoki boshqa kontekstda to'g'ridan-to'g'ri parametrlar orqali chaqirilishi mumkin.
    """
    data = read_csv(csv_file)
    if len(data) < 2:
        print("CSV faylida test talabiga binoan kamida 2 ta yozuv bo'lishi kerak!")
        return
    insert_into_db(data, db_path)
    print(f"Ma'lumotlar {db_path} bazasiga muvaffaqiyatli yuklandi.")

def main():
    parser = argparse.ArgumentParser(description="Convert CSV data into a TinyDB database.")
    parser.add_argument('csv_file',help='csv file')
    parser.add_argument('--db',help='json(Tinydb)')

    args = parser.parse_args()

    try:
        data = read_csv(args.csv_file)
        insert_into_db(data, args.db)
    except Exception :
        print("Error")

if __name__ == "__main__":
    main()
