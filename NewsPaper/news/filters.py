from django_filters import FilterSet
from .models import New

class NewFilter(FilterSet):
    class Meta:
        model = New
        fields = {
            'title': ['icontains'],
            'author': ['gt'],
            'newCategory': ['gt'],
            'dateCreation': ['lte'],
        }



