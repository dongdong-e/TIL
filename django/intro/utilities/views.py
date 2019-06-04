from django.shortcuts import render
import requests
import json
import random

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')


def random_photo(request):
    result = requests.get('https://picsum.photos/v2/list')
    photo_dic_1 = json.loads(result.text)

    photo_dic_2 = []
    for i in range(0, len(photo_dic_1)):
        photo_dic_2.append(photo_dic_1[i]['download_url'])

    picked_photo = random.choice(photo_dic_2)

    context = {'picked_photo': picked_photo}

    return render(request, 'utilities/random_photo.html', context)