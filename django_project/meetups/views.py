from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
        })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
                })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
            })
    
def confirm_registration(request): 
    return render(request, 'meetups/registration-success.html')






def func1(request):
    if request.method == 'GET': # GET é o método padrão do request
        registration_form = RegistrationForm()
        return render(request, 'app1/pag3.html', {
            'form': registration_form
            })
    else: # Ou seja, caso se vá para essa view com método POST
        linha156 = Tabela2.objects.get(slug=156)
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            form = registration_form.save() # Cria instância do BD e passa info para form
            linha156.campo4.add(form) # Adiciona form na linha156, campo4 da instância
            return redirect('nome-página-confirmação-form')
        




def func1(request):
    linha1 = Tabela2.objects.get(slug=1)
    registration_form = RegistrationForm(request.POST)  # Certifique-se de passar os dados do formulário
    if registration_form.is_valid():
        form = registration_form.save(commit=False)  # Não salve no banco de dados ainda
        nome = form.nome  # Supondo que 'nome' é o nome do campo no formulário para o nome
        email = form.email  # Supondo que 'email' é o nome do campo no formulário para o email
        form.save()  # Agora salve o formulário para gerar uma instância no banco de dados
        linha1.campo4 = nome
        linha1.campo5 = email
        linha1.save()  # Salve a linha1 com os campos atualizados
