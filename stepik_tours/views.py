from django.shortcuts import render
from django.views import View

import data


class MainView(View):

    def get(self, request):
        title_list = []
        picture_list = []
        id_list = []
        for key, value in data.tours.items():
            titles_get = value.get('title')
            title_list.append(titles_get)
            pictures_get = value.get('picture')
            picture_list.append(pictures_get)
            id_list.append(key)
        titl_pic_random = {
            'tours': title_list,
            'picture': picture_list,
            'id': id_list,
            'subtitle': data.subtitle,
            'description': data.description
        }
        return render(request, 'index.html', context=titl_pic_random)
