import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os

# Menentukan path ke chromedriver.exe yang ada di folder yang sama dengan skrip
chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

# Setup WebDriver (menggunakan Chrome di sini)
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Agar tidak menampilkan browser secara visual

# Menggunakan Service untuk memberikan path ke chromedriver.exe
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL yang ingin dikunjungi
url = 'https://www.kbcoco.com/#/pages/goods/category/category?cateList=0'
driver.get(url)

# Fungsi untuk scroll halaman agar semua kategori dimuat
def scroll_page():
    # Lakukan scroll untuk memuat seluruh konten
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Menunggu agar halaman sepenuhnya dimuat
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Fungsi untuk mengambil data kategori setelah mengklik kategori
def get_category_data():
    categories = []

    # Ambil semua elemen dengan class 'twoScroll-item'
    items = driver.find_elements(By.CLASS_NAME, "twoScroll-item")

    for item in items:
        try:
            # Ambil nama kategori
            category_name = item.find_element(By.CLASS_NAME, "using-hidden.twoScroll-item-text").text
            # Klik item kategori untuk memuat halaman kategori tersebut
            item.click()
            time.sleep(2)  # Tunggu sebentar untuk memastikan halaman kategori dimuat

            # Ambil URL produk setelah kategori diklik
            category_url = driver.current_url  # URL saat ini setelah mengklik kategori
            categories.append([category_name, category_url])

            # Kembali ke halaman utama untuk melanjutkan ke kategori berikutnya
            driver.back()
            time.sleep(2)  # Tunggu sebentar agar halaman kembali dimuat
        except Exception as e:
            print(f"Error extracting data for an item: {e}")
    
    return categories

# Melakukan scroll agar semua kategori dimuat
scroll_page()

# Ambil data kategori setelah scroll
category_data = get_category_data()

# Simpan data ke file CSV
with open('kategori.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['nama_kategori', 'url'])
    writer.writerows(category_data)

# Atau bisa menggunakan pandas untuk menyimpan dalam CSV
df = pd.DataFrame(category_data, columns=['nama_kategori', 'url'])
df.to_csv('kategori.csv', index=False, encoding='utf-8')

# Tutup browser setelah selesai
driver.quit()

print("Data telah berhasil disimpan ke dalam kategori.csv")
