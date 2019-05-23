from transliterate import translit, get_available_language_codes
from requests_html import HTML, HTMLSession
import os
import csv

#Функция обработки ссылок в категориях
def category_parse(link_formated, head, upper_dir):

    chek_for_products(link_formated)

    if product_page == True:
        response = session.get(link_formated)
        products = response.html.find('a.it.good-item-name')
        for product in products:
            product_link = product.attrs['href']
            product_link = f'https://videoglaz.ru{product_link}'
            save_product(product_link, upper_dir)
    else:
        pass

    #Сборн названий подкатегорий и ссылок на них
    response = session.get(link_formated)
    categoryes = response.html.find('table li')
    for category in categoryes:

        #Форматирую названия категорий и ссылки на них
        cat_head = category.find('a', first=True).text
        cat_link = category.find('a', first=True).attrs['href']
        cat_link_formated = f'{site_link}{cat_link}'

        list_file = f'{upper_dir}/{upper_dir}.csv'
        csv_export = open(list_file, 'a')
        csv_writer = csv.writer(csv_export)
        csv_writer.writerow([cat_head, cat_link_formated])
        csv_export.close()

        #Создаю папку для подкатегории
        rename_file(cat_head, True)
        dir_path = f'{upper_dir}/{output_name}'

        try:
            os.makedirs(dir_path)
        except FileExistsError:
            pass

        # #Создаю 
        # list_file = f'{dir_path}/{dir_name}.csv'
        # csv_export = open(list_file, 'w')
        # csv_writer = csv.writer(csv_export)
        # csv_writer.writerow(['Категория', 'Ссылка'])
        # csv_export.close()