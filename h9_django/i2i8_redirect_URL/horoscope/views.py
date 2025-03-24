from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    "aries": "Сегодня вы будете полны энергии и решимости. Используйте эту силу, чтобы начать новые проекты.",
    "taurus": "Сосредоточьтесь на своих финансах. Возможно, стоит пересмотреть свои расходы и сбережения.",
    "gemini": "Общение будет ключевым сегодня. Не стесняйтесь делиться своими мыслями и идеями с окружающими.",
    "cancer": "Сегодня вам стоит уделить внимание своим близким. Проведите время с семьей или друзьями.",
    "leo": "Ваши лидерские качества будут на высоте. Используйте их, чтобы вдохновить других.",
    "virgo": "Обратите внимание на детали. Сегодня важно быть внимательным к мелочам в работе и личной жизни.",
    "libra": "Ищите гармонию в отношениях. Возможно, вам стоит поговорить с кем-то, чтобы разрешить недоразумения.",
    "scorpio": "Сегодня вы можете столкнуться с неожиданными эмоциями. Постарайтесь разобраться в своих чувствах.",
    "sagittarius": "Пришло время для приключений! Не бойтесь выйти за пределы своей зоны комфорта.",
    "capricorn": "Сосредоточьтесь на своих целях. Сегодня отличный день для планирования и работы над долгосрочными проектами.",
    "aquarius": "Ваши идеи могут быть восприняты с энтузиазмом. Делитесь своими мыслями с окружающими.",
    "pisces": "Сегодня вам стоит обратить внимание на свои интуитивные ощущения. Доверьтесь своим внутренним ощущениям.",
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
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Знак_зодиака:неизвестный = {sign_zodiac}')

