from django.db import models

class Produto(models.Model):
    TIPO_CHOICE = [
        ('lacto','LACTICIO'),
        ('prot','PROTEINA'),
        ('hort','HORTALICAS'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICE)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nome
        

class Servico(models.Model):
    SERVICO_CHOICE = [
        ('instal','INSTALAÇAO'),
        ('mont','MONTAGEM'),
        ('manut','MANUTENÇAO'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=SERVICO_CHOICE)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nome