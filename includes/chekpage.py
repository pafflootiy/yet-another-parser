from requests_html import HTML, HTMLSession

#проверка на наличие подкаталогов
def chek_for_products (page_link):
    response = session.get(page_link)
    global product_page
    product_page = True
    try:
        find_products_div = response.html.find('.catalog-seo-grid', first=True).attrs['class'][0] #поиск класса контейнера с товаровами
    except AttributeError:
        product_page = False
        pass