from requests_html import HTML, HTMLSession

session = HTMLSession()

def chek_for_products(page_link):           #проверка на наличие подкаталогов
    response = session.get(page_link)
    is_product_page = True
    try:
        find_products_div = response.html.find('.catalog-seo-grid', first=True).attrs['class'][0] #поиск класса контейнера с товаровами
    except AttributeError:
        is_product_page = False
        pass
    return is_product_page