def read_file(file_name):
    with open(file_name, encoding='utf-8') as file_:
        data = file_.readlines()
        rows = len(data)
        dict1[file_.name] = rows
        return dict1

dict1 = {}
read_file('1.txt')
read_file('2.txt')
read_file('3.txt')
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

with open('new.txt', 'w', encoding='utf-8') as file:
    text = ''
    for key, value in sorted_dict.items():
        text += key + '\n'
        text += str(value) + '\n'
        with open(key, encoding='utf-8') as f:
            content = f.readlines()
        text += "".join(content)
        text += '\n'
    file.write(text)

