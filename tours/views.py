from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

import data


class DepartureView(View):

    def get(self, request, departure):
        prices = []
        nights = []
        context = {}
        id = 0
        for key, value in data.tours.items():
            departure_of_tour = value.get('departure')
            if departure == departure_of_tour:
                id += 1
                prices.append(value['price'])
                nights.append(value['nights'])
                value['id'] = key
                context[id] = value
        price_sorted = sorted(prices)
        nights_sorted = sorted(nights)
        tour = {
            'tours': context,
            'departure': data.departures,
            'prices': price_sorted,
            'nights': nights_sorted
        }
        return render(request, 'departure.html', context=tour)


class TourView(View):

    def get(self, request, id):
        tour = data.tours.get(id)
        tour_departure = {
            'tours': tour,
            'departure': data.departures
        }
        return render(request, 'tour.html', context=tour_departure)


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 ошибка - ошибка на стороне сервера 
                                '(страница не найдена)')


def custom_handler500(request):
    return HttpResponseServerError('внутренняя ошибка сервера')
