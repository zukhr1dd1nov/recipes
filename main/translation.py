from modeltranslation.translator import TranslationOptions,register
from .models import Taom , Kategoriya

@register(Taom)
class TaomTranslationOptions(TranslationOptions):
    fields = ('name', 'text','comment_text')
@register(Kategoriya)
class KategoriyaTranslationOptions(TranslationOptions):
    fields = ('name',)