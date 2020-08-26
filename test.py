from requests_html import HTML, HTMLSession

session = HTMLSession()
page = 'https://videoglaz.ru/ip-kamery'
resp = session.get(page)


def get_last_page(page_link):
    resp.html.render(timeout=30)
    pages = resp.html.find('.pagination-sm .page-link')
    page_index_list = []
    for page_index in pages:
        page_nom = page_index.text
        page_index_list.append(page_nom)
    if page_index_list[-2] != 'Предыдущая' and page_index_list[-2] != '1':
        last_page_index = int(page_index_list[-2]) + 1
    else:
        last_page_index = None
    return last_page_index

last_page = get_last_page(page)

if last_page != None:
    for links in range(2, last_page):
        link = f'{page}/page/{links}'
        print(link)
else:
    print('Only one page')