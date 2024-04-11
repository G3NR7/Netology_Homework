def read_all_files(name :str, flag :bool =False ): 
    data =[]
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            data += line.rstrip('\n').split('\n')
    if flag:
        return name, len(data), data
    else:
        return name, len(data)

def sort():
    d_list = []
    for i in range(3):
        name_in_sort, len_in_sort = read_all_files(f'{i+1}.txt')
        d_list.append({'name': name_in_sort, 'len': len_in_sort})
    d_list1 = sorted(d_list, key=lambda i: i['len'])
    return d_list1

def write_file(len_list :list):
    for i in len_list:
        a, b, c = read_all_files(i['name'], True)
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i in len_list:
            print(i['name'], end=' ')
            a, b, c = read_all_files(i['name'], True)
            f.write(f'{a}\n{b}\n')
            [f.write(f'{j}\n') for j in c]

def main():
    write_file(sort())

if __name__ == '__main__':
    main()