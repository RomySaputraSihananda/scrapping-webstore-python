# import function browser, filter, write dari module utils
from utils import browser, filter, write;

# list dari category dan cat_id dari URL shopee
categorys = [
    ['Aksesoris-Fashion', '11042921'],
    ['Buku-Alat-Tulis', '11044123'],
    ['Elektronik', '11044258']
];

# validasi ketika file ini dijalankan sebagai main program
if(__name__ == '__main__'):
    
    # looping list categorys
    for category in categorys:
        
        # assignment int 0 ke variable i
        i = 0;
        
        # assignment list kosong ke variable all_data
        all_data = [];

        # destructuring list category ke variable category, cat_id
        [category, cat_id] = category;

        # looping page yang ada
        while True:

            # assignment return value dari function browser ke variable html
            html = browser(f'https://shopee.co.id/{category}-cat.{cat_id}?page={i}');

            # assignment return value dari function filter ke variable data
            data = filter(html);

            # validasi jika variable data bernilai False, maka looping berhenti
            if(not data): break;
            
            # log ke layar category dan page yang discrapping 
            print(f'Category : {category}\nPage     : {i + 1}');

            # menulis data dari variable data (setiap page)
            write(data, f'{category}/page_{i + 1}', f'page_{i + 1}');
            
            # assignment new data dan old data ke variable all_data
            all_data = all_data + data;

            # increment variable i
            i += 1;
        
        # menulis data dari variable all_data (semua page)
        write(all_data, category, 'all_page');