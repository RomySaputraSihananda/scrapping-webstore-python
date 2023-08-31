[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# scrapping-webstore-python

Project ini adalah tugas dari program magang di **PT. INDONESIA INDIKATOR**. Tujuan proyek ini adalah untuk mengembangkan sebuah sistem yang dapat melakukan web scraping pada sebuah webstore tertentu. Web scraping adalah teknik untuk mengumpulkan informasi dari halaman web secara otomatis.

## Features

- Pemilihan teknologi atau library yang sesuai untuk web scraping.
- Penentuan struktur data yang akan disimpan.
- Pengembangan script untuk mengambil data dari halaman web.
- Pengolahan dan penyimpanan data yang diambil.
- Dokumentasi yang jelas mengenai cara menjalankan proyek dan menjelaskan kode.

## Structure

```
📦scrapping-webstore-python
 ┣ 📂browser
 ┃ ┗ 📀chromedriver
 ┣ 📂utils
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜browser.py
 ┃ ┣ 📜filter.py
 ┃ ┗ 📜write.py
 ┗  📜main.py
```

## Tech

This application is built using a number of open source projects to function properly:

- [Python](https://www.python.org/) - bahasa pemrograman yang digunakan
- [Chromedriver](https://chromedriver.chromium.org/downloads/) - komponen yang digunakan bersama dengan Selenium untuk mengotomatisasi pengujian atau web scraping di browser Chrome
- [Selenium](https://www.selenium.dev/) - framework yang digunakan untuk otomatisasi web page
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/) - library yang digunakan untuk mengekstrak informasi dari kode HTML dan XML
- [Pandas](https://pandas.pydata.org/) - library yang digunakan untuk manipulasi dan analisis data

## Requirement

- [Python](https://www.python.org/) v3.10+
- [Chromedriver](https://chromedriver.chromium.org/downloads/) (version according to the chrome used)

## Installation

This project requires [Python](https://www.python.org/) v3.10+ to run

Install all the dependencies needed in this project

```sh
pip install -r requirements.txt
```

Then run the project

```sh
python main.py
```

## License

MIT

## Credit

> Romy Saputra Sihananda
