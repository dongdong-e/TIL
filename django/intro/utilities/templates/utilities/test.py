import requests
import json

result = requests.get('https://picsum.photos/v2/list')
photo_dic_1 = json.loads(result.text)

photo_dic_2 = []
for i in range(0, len(photo_dic_1)):
    photo_dic_2.append(photo_dic_1[i]['download_url'])


# photo_urls = []
# for i in photo_dic:
#     photo_urls.append(photo_dic['download_url'])
#
# print(photo_urls)
#
# picked_photo = random.choice(photo_urls)
#
# context = {'picked_photo': picked_photo}
#
# return render(request, 'utilities/random_photo.html', context)