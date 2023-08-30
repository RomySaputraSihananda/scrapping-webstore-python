# import module BeautifulSoup dari library bs4 (analisis dan pemrosesan HTML)
from bs4 import BeautifulSoup;

# declaration function filter dengan parameter html
def filter(html):

    # membuat object BeautifulSoup dengan argument html dari parameter dan 'html.parser' bawaan dari BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser');

    # assignment list kosong ke variable data
    data = [];

    # mencari semua elemen `<div class='col-xs-2-4 shopee-search-item-result__item'>` (card product) dan diassign ke variable cards
    cards = soup.find_all('div', attrs={'class': 'col-xs-2-4 shopee-search-item-result__item'});

    # validasi jika elemen yang ditemukan, maka function akan mereturn nilai False
    if(not len(cards)): return False;

    # looping setiap card pada variable cards
    for card in cards:

        # mencari elemen `<div class='_1yN94N WoKSjC _2KkMCe'/>` (nama product), mengambil text-nya dan diassign ke variable nama
        nama = card.find('div', attrs={'class': '_1yN94N WoKSjC _2KkMCe'}).get_text();

        # mencari elemen `<a/>` (link product), mengambil href-nya dan diassign ke variable link
        link = card.find('a').get('href');

        # mencari elemen `<div class='cbl0HO MUmBjS'/>` (harga product), mengambil text-nya dan diassign ke variable harga
        harga = card.find('div', attrs={'class': 'cbl0HO MUmBjS'}).get_text();

        # mencari elemen `<img class='B0Ze3i wAkToc'/>` (image product), mengambil src-nya dan diassign ke variable img
        img = card.find('img', attrs={'class': 'B0Ze3i wAkToc'}).get('src');

        # mencari elemen `<div class='mrz-bA'>` (kota product), mengambil text-nya dan diassign ke variable kota
        kota = card.find('div', attrs={'class': 'mrz-bA'}).get_text();

        # mencari elemen `<div class='x+3B8m wOebCz'>` (product terjual), mengambil text-nya dan diassign ke variable terjual
        terjual = card.find('div', attrs={'class': 'x+3B8m wOebCz'}).get_text();

        # menambah dictionary ke variable data
        data.append({

            # membuat key nama dengan value variable nama
            'nama': nama,

            # membuat key link dengan value https://shopee.co.id + variable link
            'link': f'https://shopee.co.id{link}',

            # membuat key harga dengan value variable harga
            'harga': harga,

            # membuat key img dengan value variable img
            'img': img,

            # membuat key kota dengan value variable kota
            'kota': kota,

            # membuat key terjual dengan value variable terjual
            'terjual': terjual,
        });
    
    # mereturn data (berisi kumpulan data semua card)
    return data;
