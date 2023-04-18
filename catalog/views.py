from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.db.models import F
from django.views.generic.edit import FormMixin
from .models import Autor, Avaliador, EnviarProjeto, Premio, Auxiliar,ProjetoAvaliado
from .forms import AutorForm, AvaliadorForm, EnviarProjetoForm, PremioForm, AuxiliarForm, NovaNota


def index(request):
    return render(request, "index.html")


def list_autor_view(request):

    autor = Autor.objects.all()
    context = {}
    context["object_list"] = autor

    # add the dictionary during initialization
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "autores/list_autores.html", context)


def novo_autor_view(request):
    if request.method =='POST':
        form = AutorForm(request.POST)

        if form.is_valid():

            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form = AutorForm

    return render(request, "autores/novo_autor.html", {'form':form})


# update view for details
def editar_autor_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Autor, id=id)

    # pass the object as instance in form
    form = AutorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "autores/editar_autor.html", context)


# delete view for details
def delete_autor_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    autor=Autor.objects.get(id=id)

    autor.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/")

def novo_auxiliar_view(request):
    if request.method=='POST':
        form = AuxiliarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form = AuxiliarForm

    return render(request, "auxiliar/novo_auxiliar.html", {'form':form})

def list_auxiliar_view(request):

    auxiliar = Auxiliar.objects.all()
    context = {}
    context["object_list"] = auxiliar

    # add the dictionary during initialization
    form = AuxiliarForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "auxiliar/list_auxiliar.html", context)

def editar_auxiliar_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Auxiliar, id=id)

    # pass the object as instance in form
    form = AuxiliarForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "auxiliar/editar_auxiliar.html", context)

def delete_auxiliar_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    auxiliar=Auxiliar.objects.get(id=id)

    auxiliar.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/")

def novo_avaliador_view(request):
    if request.method=='POST':
        form = AvaliadorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form = AutorForm

    return render(request, "avaliadores/novo_avaliador.html", {'form':form})


def listar_avaliador_view(request):
    avaliador = Avaliador.objects.all()
    context = {}
    context["object_list"] = avaliador

    # add the dictionary during initialization
    form = AvaliadorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "avaliadores/list_avaliadores.html", context)

def editar_avaliador_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Avaliador, id=id)

    # pass the object as instance in form
    form = AvaliadorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "avaliadores/editar_avaliadores.html", context)

def delete_avaliador_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    avaliador = Avaliador.objects.get(id=id)

    avaliador.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/")


def novo_projeto_view(request):
    if request.method == 'POST':
        form = EnviarProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            nome_autor = request.POST.getlist('autores')
            autores = Autor.objects.filter(nome=nome_autor)
            projeto.save()
            projeto.autores.set(autores)
            return redirect("/catalog/projeto")
    else:
        form = EnviarProjetoForm()

    return render(request, "projeto/novo_projeto.html", {'form':form})


class ProjetoListView(ListView):
    model = EnviarProjeto
    context_object_name = 'projetos'
    template_name = 'projeto/list_projeto.html'
    ordering = ['-dataEnvio']

    def get_queryset(self):
        queryset = EnviarProjeto.objects.all()

        order_by = self.request.GET.get('order_by')

        if order_by == 'nota_asc':
            queryset = queryset.annotate(nota=F('projetoavaliado__nota')).order_by('nota')
        elif order_by == 'nota_desc':
            queryset = queryset.annotate(nota=F('projetoavaliado__nota')).order_by('-nota')

        return queryset



def editar_projeto_view(request, id):

    context = {}

    obj = get_object_or_404(EnviarProjeto, id=id)

    # pass the object as instance in form
    form = EnviarProjetoForm(request.POST or None, instance=obj)
    autor = Autor.objects.filter(nome='').first()

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.instance.autor = autor
        form.save()
        return HttpResponseRedirect("/catalog/projeto")

    # add form dictionary to context
    context["form"] = form

    return render(request, "projeto/editar_projeto.html", context)

def delete_projeto_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    projeto = EnviarProjeto.objects.get(id=id)

    projeto.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/catalog/projeto")


class DetalheProjeto(FormMixin, DetailView):
    model = EnviarProjeto
    template_name = 'projeto/detalhes_projeto.html'
    context_object_name = 'projeto'
    form_class = NovaNota

    def get_success_url(self):
        return reverse_lazy('detalhes_projeto', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projeto = self.get_object()
        projeto_avaliado = projeto.projetoavaliado if hasattr(projeto, 'projetoavaliado') else None
        context['form'] = self.get_form()
        context['tem_nota'] = projeto_avaliado is not None
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        projeto = get_object_or_404(EnviarProjeto, pk=self.kwargs['pk'])
        if form.is_valid():
            nota = form.save(commit=False)
            nota.projeto = projeto
            nota.save()
            nota.avaliador.set([request.user.id])
            return redirect('detalhe_projeto', pk=projeto.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form, projeto=projeto))



def projetos_nao_avaliados(request):
    # Obtém todos os projetos enviados
    projetos_enviados = EnviarProjeto.objects.all()

    # Obtém os projetos que não foram avaliados
    projetos_nao_avaliados = []
    for projeto in projetos_enviados:
        if not ProjetoAvaliado.objects.filter(projeto=projeto).exists():
            projetos_nao_avaliados.append(projeto)

    context = {'projetos_nao_avaliados': projetos_nao_avaliados}
    return render(request, 'projeto/projetos_nao_avaliados.html', context)


def inserir_premio_view(request):

    form = PremioForm()
    if request.method == 'POST':
        form = PremioForm(request.POST)
        if form.is_valid():
            premio = form.save(commit=False)
            premio.save()
            premio.autor.set(form.cleaned_data['autor'])
            return redirect("/catalog/premio")
    elif request.method == 'GET':
        form = PremioForm()

    return render(request, 'premio/novo_premio.html', {'form': form})


def listar_premio_view(request):
    return render(request, "premio/list_premio.html", {'premios': Premio.objects.all()})



def editar_premio_view(request, id):
    # dictionary for initial data with
    # field names as keys

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Premio, id=id)

    # pass the object as instance in form
    form = PremioForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "premio/editar_premio.html", context)


def delete_premio_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    premio = Premio.objects.get(id=id)

    premio.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/")

