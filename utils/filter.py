from bs4 import BeautifulSoup;

def filter(html):

    soup = BeautifulSoup(html, 'html.parser');
    data = [];
    cards = soup.find_all('div', attrs={'class': 'col-xs-2-4 shopee-search-item-result__item'});

    if(not len(cards)): return False;

    for card in cards:
        
        nama = card.find('div', attrs={'class': '_1yN94N WoKSjC _2KkMCe'}).get_text();
        link = card.find('a').get('href');
        harga = card.find('div', attrs={'class': 'cbl0HO MUmBjS'}).get_text();
        img = card.find('img', attrs={'class': 'B0Ze3i wAkToc'}).get('src');
        kota = card.find('div', attrs={'class': 'mrz-bA'}).get_text();
        terjual = card.find('div', attrs={'class': 'x+3B8m wOebCz'}).get_text();

        data.append({
            'nama': nama,
            'link': f'https://shopee.co.id{link}',
            'harga': harga,
            'img': img,
            'kota': kota,
            'terjual': terjual,
        });
    
    return data;
