from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# git remote add origin https://github.com/MirevGen/Viceverca-root.git
# git branch -M main
# git push -u origin main


def reverse(request):
    user_text = request.GET['usertext']
    print(user_text)

    number_of_words = len(user_text.split())

    reversed_text = user_text[::-1]
    print(reversed_text)
    return render(request, 'reverse.html', {'user_text':user_text, "reversed_text":reversed_text, "number_of_words":number_of_words})