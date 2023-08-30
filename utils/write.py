# import modul JSON (memformat list ke JSON)
import json;

# import library Pandas sebagai pd (menulis data ke file xlsx dan csv)
import pandas as pd;

# import module os (validasi dan menulis sebuah directory)
import os; 

# declaration function write dengan parameter data, category, name
def write(data, category, name):

    # Mengubah data dari parameter menjadi format JSON
    data = json.dumps(data);

    # menentukan directory penyimpanan berdasarkan category dari parameter 
    path = f'data/{category}';

    # mengecek directory sudah ada apa belum 
    isExist = os.path.exists(path);

    # validasi jika variable isExist bernilai False, maka dibuatkan directory dari variable path
    if(not isExist): os.makedirs(path);
    
    # menulis variable data dengan format JSON ke file JSON dengan nama name + .json 
    with open(f'{path}/{name}.json', 'w') as file:
        file.write(data);
    
    # membaca variable data dengan format JSON sebagai DataFrame menggunakan Pandas
    df = pd.read_json(data);
    
    # menyimpan DataFrame ke dalam file csv dengan nama name + .csv
    df.to_csv(f'{path}/{name}.csv');

    # merename label index DataFrame menjadi no
    df.index = df.index.rename('no');

    # menambahkan 1 ke setiap index
    df.index = df.index + 1;

    # menyimpan DataFrame ke dalam file excel dengan nama name + .xlsx
    df.to_excel(f'{path}/{name}.xlsx');
    
    # log ke layar path dari result data yang telah ditulis 
    print(f'Result   : {path}\n');
