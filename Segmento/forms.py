from haystack.forms import SearchForm
from django.forms import ModelForm
from Segmento.models import Segmento


class SegmentoForm(ModelForm):
    class Meta:
        model = Segmento
        fields = '__all__'


#formularios de busqueda
class SegmentoSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
