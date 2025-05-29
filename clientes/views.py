from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from .models import Cliente

# Aqui vai toda a nossa lógica

# Função da quebra de maldição
# O request é uma solicitação de uma página(Template)
# O httpresponse responde a solicitação/requisição (Request)
def saudacao(request):
    return HttpResponse ("<h1>Olá mundo!</h1>")

#Desafio: Criar uma função chamada home() que exiba uma menaem dizendo 'AREA DO CLIENTE'

# Importante que todo html esteja dentro da pasta templates(deve ser no plural por padrão do Django. é a sintaxe dele. Ela não vem criada, temos que criar essa pasta)
def home(request):
    return render(request, 'clientes.html') 

#Essas funções são VBF ^^^^^

#Utilizando classe na view
"""  class Home(View):
        def get(self,request):
            return render(request, 'clientes.html') """
        
# Classe da página principal
class Home(ListView):
    def get(self,request):
        return render(request, 'clientes/home_cliente.html')

class Clientes_list(ListView):
    # a ferramenta listview permite (model, template_name)

    #conecta ao modelo de banco de dados
    model = Cliente # retorna uma lista chamada cliente_list
    #conecta no modelo de banco de dados
    template_name = 'clientes/list_cliente.html'
   
"""  def get(self, request):
        return render(request, 'clientes/clientes_list.html') """