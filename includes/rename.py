from transliterate import translit, get_available_language_codes

#Заменяю все ненужные символы в имени файла
def rename_file(input_name, trnslt):
    global output_name

    if trnslt == True:
        name = translit(input_name, 'ru', reversed=True) #Транслитерируем
    else:
        name = input_name

    name = name.replace(' ', '_')
    name = name.replace('"', '_')
    name = name.replace('/', '_')
    name = name.replace('.', '_')
    name = name.replace(',', '_')
    name = name.replace('{', '_')
    output_name = name.replace('}', '')