from haystack import indexes
from Segmento.models import Segmento


class SegmentoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #model fields
    segmento = indexes.CharField(model_attr='segmento')
    activo = indexes.BooleanField(model_attr='activo')

    def get_model(self):
        return Segmento

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(activo=True)
