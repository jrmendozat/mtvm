from django.forms import ModelForm
from Articulo.models import Articulo_Clase, \
Articulo_Subclase, Categoria_Articulo, Subcategoria_articulo, \
Articulo, Tipo_Costo, Articulo_Costo, Unidad, Articulo_Unidad, \
Articulo_Precio

# crear form
class ArticuloClaseForm(ModelForm):
    class Meta:
        model = Articulo_Clase
        fields = '__all__'

class ArticuloSubclaseForm(ModelForm):
    class Meta:
        model = Articulo_Subclase
        fields = '__all__'

class CategoriaArticuloForm(ModelForm):
    class Meta:
        model = Categoria_Articulo
        fields = '__all__'

class SubcategoriaArticuloForm(ModelForm):
    class Meta:
        model = Subcategoria_articulo
        fields = '__all__'

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class TipoCostoForm(ModelForm):
    class Meta:
        model = Tipo_Costo
        fields = '__all__'

class ArticuloCostoForm(ModelForm):
    class Meta:
        model = Articulo_Costo
        fields = '__all__'

class UnidadForm(ModelForm):
    class Meta:
        model = Unidad
        fields = '__all__'

class ArticuloUnidadForm(ModelForm):
    class Meta:
        model = Articulo_Unidad
        fields = '__all__'

class ArticuloPrecioForm(ModelForm):
    class Meta:
        model = Articulo_Precio
        fields = '__all__'

class ArticulopruebaForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['articulo']
