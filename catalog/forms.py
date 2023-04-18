from django import forms
from .models import Autor, Avaliador, EnviarProjeto, Premio, Auxiliar, ProjetoAvaliado


# creating a form
class AutorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Autor

        # specify fields to be used
        fields = "__all__"


class AvaliadorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Avaliador

        # specify fields to be used
        fields = "__all__"


class EnviarProjetoForm(forms.ModelForm):
    autores = forms.ModelChoiceField(queryset=Autor.objects.all(),
                                     to_field_name='nome',
                                     empty_label='Selecione o autor')

    # create meta class
    class Meta:
        # specify model to be used
        model = EnviarProjeto

        # specify fields to be used
        fields = ('area', 'titulo','resumo','autores')


class PremioForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Premio

        # specify fields to be used
        fields = "__all__"


class AuxiliarForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Auxiliar

        # specify fields to be used
        fields = "__all__"


class NovaNota(forms.ModelForm):
    class Meta:
        model = ProjetoAvaliado
        fields = ['nota']