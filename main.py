from transliterate import translit, get_available_language_codes
from requests_html import HTML, HTMLSession
import os
import csv

from includes.rename import rename_file
from includes.category_parse import category_parse
from includes.prod_page_parse import save_product, products_page_parse


#Открываю html сессию с сайтом
session = HTMLSession()
site_link = 'https://videoglaz.ru'
cat_link_basecat = '/catalog.php'
formated_link = f'{site_link}{cat_link_basecat}'
response = session.get(formated_link)

#Создаю csv файл для записи категорий и ссылок на них
cat_list_file = 'cat_list.csv'
csv_export_create = open(cat_list_file, 'w')
csv_writer = csv.writer(csv_export_create)
csv_writer.writerow(['Категория', 'Ссылка'])

#Собираю названия категорий и ссылки на них
categoryes = response.html.find('.context a')

#Some shitycode
for category in categoryes:

    #Форматирую названия категорий и ссылки на них
    cat_head = category.find(first=True).text
    cat_link = category.find('a', first=True).attrs['href']
    cat_link_formated = f'{site_link}{cat_link}'

    #Записываю категории и ссылок на них в csv файл
    csv_export = open(cat_list_file, 'a')
    csv_writer.writerow([cat_head, cat_link_formated])
    csv_export.close()

    rename_file(cat_head, True)

    print(output_name)
    # try:
    #     os.makedirs(output_name)
    # except FileExistsError:
    #     pass

    # sub_list_file = f'{output_name}/{output_name}.csv'
    # csv_export = open(sub_list_file, 'w')
    # sub_csv_writer = csv.writer(csv_export)
    # sub_csv_writer.writerow(['Категория', 'Ссылка'])

    # parse_sub_category(cat_link_formated, cat_head, output_name)
print('All done!')