from requests_html import HTML, HTMLSession
import csv

session = HTMLSession()
site_link = 'https://videoglaz.ru'

#Сохранение товара
def save_product(page_link, dir_name):
    response = session.get(page_link)

    product_name = response.html.find('h1', first=True).text    #Первый h1 тэг это имя товара
    product_price = response.html.find('.price-table > tbody > tr > td', first=True).text   #Розничная цена товара
    product_fotos = response.html.find('.fancybox') #Ищу все фотки товара
    product_descr = response.html.find('.content ul', first=True).text  #Технические характеристики товара
    product_descr_formated = product_descr.replace('\n', '<br />')  #Меняю перенос строк на переноса строк

    foto_list = []

    for product_foto in product_fotos:
        foto_link = product_foto.attrs['href']
        formated_foto_link = f'{site_link}{foto_link}'
        foto_list.append(formated_foto_link)

    output_name = rename_file(product_name, False)

    csv_file_name = output_name
    product_description_csv = f'{dir_name}/{csv_file_name}.csv'
    csv_export = open(product_description_csv, 'w')
    csv_writer = csv.writer(csv_export)
    csv_writer.writerow(['Наименование', 'Цена', 'Описание', 'фото-1', 'фото-2', 'фото-3', 'фото-4'])

    #Если у товара 4 фото, то записываю их, если одно, то одно, если ни одного, то не пишу ссылки на фото
    try:
        csv_writer.writerow([product_name, product_price, product_descr_formated, foto_list[0], foto_list[1], foto_list[2], foto_list[3]])
    except IndexError:
        try:
            csv_writer.writerow([product_name, product_price, product_descr_formated, foto_list[0]])
        except IndexError:
            csv_writer.writerow([product_name, product_price, product_descr_formated])
            pass
        pass
    csv_export.close()


def products_page_parse():
    products = response.html.find('a.it.good-item-name')

    for product in products:
        product_link = product.attrs['href']
        product_link = f'{site_link}{product_link}'
        save_product(product_link)