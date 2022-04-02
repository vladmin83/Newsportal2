from django.forms import ModelForm, BooleanField
from .models import New


# Создаём модельную форму
class NewForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = New
        fields = ['title', 'categoryType', 'newCategory', 'text', 'author', 'check_box']

