from selenium import webdriver;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.chrome.options import Options;
from time import sleep;

def browser(url):
    service = Service(executable_path='browser/chromedriver');
    options = Options();
    options.add_argument('--headless');
    browser = webdriver.Chrome(service=service, options=options);

    browser.get(url);
    browser.execute_script("document.body.style.zoom='10%'");

    sleep(15);

    html = browser.page_source;

    return html;
