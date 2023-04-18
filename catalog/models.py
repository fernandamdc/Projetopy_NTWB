from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Auxiliar(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class EnviarProjeto(models.Model):
    area = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=250)
    autores = models.ManyToManyField(Autor)
    dataEnvio = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return self.titulo


class Avaliador(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Premio(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, )
    cronograma = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor)

    def __str__(self):
        return self.nome


class ProjetoAvaliado(models.Model):
    projeto = models.OneToOneField(EnviarProjeto, on_delete=models.CASCADE)
    avaliador = models.ManyToManyField(Avaliador)
    nota = models.DecimalField(max_digits=2, decimal_places=False)

    def __str__(self):
        return self.projeto.titulo

