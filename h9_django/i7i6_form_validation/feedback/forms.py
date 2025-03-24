from django import forms
from .models import Feedback

# class Form_feedback(forms.Form):
#     name = forms.CharField(label='Имя', max_length=50)
#     surname = forms.CharField(max_length=50)
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))
#     rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)

class Form_feedback(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'feedback', 'rating']
        fields = '__all__'
        # additionally
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг (от 1 до 5)',
        }
        error_messages = {
            "name": {  # сообщения при ошибочном вводе имени
                "max_length": "За что тебя так наказали? А по короче можно?",
                "min_length": "У тебя китайское имя? Может полное напишешь?",
                "required": "У тебя имя есть?",
            },
            "surname": {  # сообщения при ошибочном вводе фамилии
                "max_length": "Это от какого поколения столько набралось? Давай только последнее.",
                "min_length": "Ты инициалы ввёл? Можешь полностью написать?",
                "required": "Совсем фамилии нет?",
            },
            "feedback": {  # сообщения при незаполненном поле
                "required": "Ну хоть что-то напиши.",
            },
            "rating": {  # сообщения при ошибочном вводе рейтинга
                "max_value": "Ну ты заценил. Это по двенадцати бальной шкале? У нас пяти бальная.",
                "min_value": "Всё так плохо? Будь снисходительней.",
                "required": "Без оценки дальше не идём.",
            },
        }