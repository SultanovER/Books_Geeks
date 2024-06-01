from django.shortcuts import render
from django.http import HttpResponse
import datetime

def about_view(request):
    if request.method == 'GET':
        return HttpResponse('Султанов А.Э., 19 лет')

def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Всего по-немножку!')

def time_view(request):
    if request.method == 'GET':
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Возвращаем текущее время в HttpResponse
        return HttpResponse(f'Текущее время: {current_time}')
