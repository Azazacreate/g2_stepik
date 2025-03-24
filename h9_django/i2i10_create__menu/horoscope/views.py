from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from datetime import date

zodiac_dict = {
    "aries": "aries. Сегодня вы будете полны энергии и решимости. Используйте эту силу, чтобы начать новые проекты.",
    "taurus": "taurus. Сосредоточьтесь на своих финансах. Возможно, стоит пересмотреть свои расходы и сбережения.",
    "gemini": "gemini. Общение будет ключевым сегодня. Не стесняйтесь делиться своими мыслями и идеями с окружающими.",
    "cancer": "cancer. Сегодня вам стоит уделить внимание своим близким. Проведите время с семьей или друзьями.",
    "leo": "leo. Ваши лидерские качества будут на высоте. Используйте их, чтобы вдохновить других.",
    "virgo": "virgo. Обратите внимание на детали. Сегодня важно быть внимательным к мелочам в работе и личной жизни.",
    "libra": "libra. Ищите гармонию в отношениях. Возможно, вам стоит поговорить с кем-то, чтобы разрешить недоразумения.",
    "scorpio": "scorpio. Сегодня вы можете столкнуться с неожиданными эмоциями. Постарайтесь разобраться в своих чувствах.",
    "sagittarius": "sagittarius. Пришло время для приключений! Не бойтесь выйти за пределы своей зоны комфорта.",
    "capricorn": "capricorn. Сосредоточьтесь на своих целях. Сегодня отличный день для планирования и работы над долгосрочными проектами.",
    "aquarius": "aquarius. Ваши идеи могут быть восприняты с энтузиазмом. Делитесь своими мыслями с окружающими.",
    "pisces": "pisces. Сегодня вам стоит обратить внимание на свои интуитивные ощущения. Доверьтесь своим внутренним ощущениям.",
}
zodiac_date_dict = {
    1: {'capricorn': (1, 20), 'aquarius': (21, 31)},
    2: {'aquarius': (1, 19), 'pisces': (20, 29)},
    3: {'pisces': (1, 20), 'aries': (21, 31)},
    4: {'aries': (1, 20), 'taurus': (21, 30)},
    5: {'taurus': (1, 21), 'gemini': (22, 31)},
    6: {'gemini': (1, 21), 'cancer': (22, 30)},
    7: {'cancer': (1, 22), 'leo': (23, 31)},
    8: {'leo': (1, 21), 'virgo': (22, 31)},
    9: {'virgo': (1, 22), 'libra': (23, 30)},
    10: {'libra': (1, 23), 'scorpio': (24, 31)},
    11: {'scorpio': (1, 22), 'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
}
type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

def get__sign_zodiacInt(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер:порядковый знака_зодиака => {sign_zodiac}')
    zodiac_name = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(zodiac_name, ))
    return HttpResponseRedirect(redirect_url)

def get__sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Знак_зодиака:неизвестный = {sign_zodiac}')

def index(request):
    string_1 = ''
    for sign in zodiac_dict:
        redirect_path = reverse('horoscope_name', args=[sign])
        string_1 += f'<li><a href={redirect_path}>{sign.title()}</a></li>'
    return HttpResponse(f'<ol>{string_1}</ol>')

def get__types(request):
    string_1 = ''
    for el in type_dict:
        string_1 += f'<li><a href={el}>{el}</a></li>'
    return HttpResponse(f'<ol>{string_1}</ol>')

def get__type(request, type_name):
    string_1 = ''
    for el in type_dict[type_name]:
        redirect_path = reverse('horoscope_name', args=[el])
        string_1 += f'<li><a href={redirect_path}>{el}</a></li>'
    return HttpResponse(f'<ol>{string_1}</ol>')

def find_out__zodiac(request, month: int, day: int):
    if (month in [1, 3, 7, 8, 10, 12] and day <= 31) or (month in [2] and day <= 28) or (month in [4, 5, 6, 9, 11] and day <= 30):
        for sign_1, date_1 in zodiac_date_dict[month].items():
            if date_1[0] <= day <= date_1[1]:
                redirect_path = reverse('horoscope_name', args=[sign_1])
                return HttpResponseRedirect(redirect_path)
    return HttpResponseNotFound(f'Укажите правильный месяц (от 1 до 12) и день (от 1 до 31)')
