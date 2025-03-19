from django.shortcuts import render, redirect


def add_to_file(word1:str, word2:str):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + word1 + ' ' + word2)


def read_from_file():
    file = open(
        'file.txt', 'r', encoding='utf-8'
    ).read().splitlines()
    words = []
    for line in file:
        word = line.split(' ')
        words.append(word)
    return words

def index_page(request):
    return render(request, 'home.html')

def add_word(request):
    if request.method == 'GET':
        return render(request, 'add_word.html')
    else:
        add_to_file(request.POST['word1'], request.POST['word2'])
        return redirect('add_word')
    
def words_list(request):
    words = read_from_file()
    return render(request, 'words_list.html', {'words': words})
