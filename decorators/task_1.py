# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
def clear_text():
    with open("test_file/task1_data.txt", "r", encoding="utf-8") as data_file:
        data = data_file.readlines()

    with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as answer_file:
        for row in data:
            clean_row = ''.join([i for i in row if not i.isdigit()])
            answer_file.write(clean_row)


clear_text()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
