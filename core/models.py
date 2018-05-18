# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    cpf_cnpj = models.CharField(max_length=17)
    ie = models.CharField(max_length=15)
    nome = models.CharField(max_length=70)
    tipo_cliente = models.CharField(max_length=7)
    segmento = models.CharField(max_length=40)
    nome_contato = models.CharField(max_length=70)
    e_mail = models.CharField(max_length=60)
    rua = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    telefone1 = models.CharField(max_length=20, blank=True, null=True)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        db_table = 'Cliente'
        unique_together = (('ie', 'estado'), ('cpf_cnpj', 'estado'),)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=17, unique=True)
    razao_social = models.CharField(unique=True, max_length=80)
    nome_fantasia = models.CharField(max_length=50)
    ie = models.CharField(max_length=15)
    data_cadastro = models.DateField(blank=True, null=True)
    categoria = models.CharField(max_length=30)
    nome_contato = models.CharField(max_length=30)
    rua = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    numero = models.IntegerField()
    cep = models.BigIntegerField()
    complemento = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=40)
    telefone1 = models.CharField(max_length=20)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)
    e_mail = models.CharField(max_length=85, blank=True, null=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        db_table = 'Fornecedor'
        unique_together = (('ie', 'estado'),)


class Material(models.Model):
    cor = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=70)
    descricao = models.TextField(blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return self.nome


class Orcamento(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    situacao = models.CharField(max_length=30)
    detalhes = models.CharField(max_length=30)
    prazo = models.DateField()
    entrega = models.CharField(max_length=60, blank=True, null=True)
    custo_frete = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    margem = models.IntegerField(blank=True, null=True)
    valor_orçamento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_contato = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Orcamento'


class Projeto(models.Model):
    id_orcamento = models.ForeignKey(Orcamento, models.DO_NOTHING, db_column='id_orcamento')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    rastreio = models.CharField(max_length=50)
    data_entregue = models.DateField(blank=True, null=True)
    pagamento = models.CharField(max_length=85, blank=True, null=True)
    situacao = models.CharField(max_length=30, blank=True, null=True)
    data_confirmado = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Projeto'


class Servico(models.Model):
    id_projeto = models.ForeignKey(Projeto, models.DO_NOTHING, db_column='id_projeto')
    unidade = models.SmallIntegerField(blank=True, null=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Servico'

class FornecedorMaterial(models.Model):
    id_material = models.ForeignKey('Material', models.DO_NOTHING, db_column='id_material')
    id_fornecedor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='id_fornecedor')

    class Meta:
        db_table = 'FonecedorMaterial'
        unique_together = (('id_material', 'id_fornecedor'),)