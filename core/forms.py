from django.forms import ModelForm
from core.models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf_cnpj", "ie", "segmento", "tipo_cliente", "nome_contato", "telefone1",
         "telefone2", "e_mail", "cep", "estado", "cidade", "rua", "numero", "bairro", "complemento"]

class OrcamentoForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["cnpj", "razao_social", "nome_fantasia", "ie", "data_cadastro", "categoria", "nome_contato", "rua", "bairro", "numero", "cep", "complemento", "cidade", "estado", "telefone1", "telefone2", "e_mail"]

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class FornecedorMaterialForm(ModelForm):
    class Meta:
        model = FornecedorMaterial
        fields = ["id_material"]