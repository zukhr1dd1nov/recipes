from django.forms import ModelForm
from .models import Taom
from modeltranslation.forms import TranslationModelForm

class TaomForm(ModelForm):
    class Meta:
        model = Taom
        fields = ('kategoriya','name_uz', 'name_ru', 'name_en', 'comment_text_uz','comment_text_ru','comment_text_en','portions','how_much_time' ,'text_uz','text_ru','text_en', 'photo')
