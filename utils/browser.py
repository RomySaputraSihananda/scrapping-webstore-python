# import module webdriver dari library selenium (mengendalikan browser)
from selenium import webdriver;

# import module Service dari library selenium (mengelola browser)
from selenium.webdriver.chrome.service import Service;

# import module Options dari library selenium (configure opsi browser)
from selenium.webdriver.chrome.options import Options;

# import fungsi sleep dari module time
from time import sleep;

# declaration function browser dengan parameter url
def browser(url):

    # membuat object service dari module Service dengan argument path dari path cromedriver
    service = Service(executable_path='browser/chromedriver');

    # membuat object options dari module Option 
    options = Options();

    # menambahkan opsi '--headless' (tanpa menampilkan GUI dari browser) ke objek options
    options.add_argument('--headless');

    # membuat objek browser dengan argument service dan option yang sudah diconfig
    browser = webdriver.Chrome(service=service, options=options);

    # membuka browser dan mengakses url dari parameter
    browser.get(url);

    # melakukan eksekusi JavaScript code untuk mengatur zoom page browser menjadi 10%
    browser.execute_script("document.body.style.zoom='10%'");

    # memberi jeda 15 detik Ini agar web page selesai diload 
    sleep(15);

    # mengambil source code dari web dan diassignt
    html = browser.page_source;

    # menutup browser
    browser.close();

    # mereturn variable html yang berisi source code web
    return html;
