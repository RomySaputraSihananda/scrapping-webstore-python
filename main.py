from utils import browser, filter, write;

categorys = [
    ['Aksesoris-Fashion', '11042921'],
    ['Buku-Alat-Tulis', '11044123'],
    ['Elektronik', '11044258']
];

if(__name__ == '__main__'):
    for category in categorys:
        i = 0;
        all_data = [];

        [category, cat_id] = category;

        while True:
            html = browser(f'https://shopee.co.id/{category}-cat.{cat_id}?page={i}');
            data = filter(html);

            if(not data): break;
            
            print(f'Category : {category}\nPage     : {i + 1}');

            write(data, f'{category}/page_{i + 1}', f'page_{i + 1}');
            
            all_data = all_data + data;
            i += 1;
        
        write(all_data, category, 'all_page');