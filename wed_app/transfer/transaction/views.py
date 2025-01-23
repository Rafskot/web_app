from django.shortcuts import render, redirect
from .models import Chek
from .forms import ChekForm
from django.views.generic import DetailView, UpdateView, DeleteView


def tran_home(request):
    cheks = Chek.objects.order_by('-date_create')
    return render(request, 'transaction/tran_home.html', {'cheks': cheks})


class TranDetailView(DetailView):
    model = Chek
    template_name = 'transaction/detail_view.html'
    context_object_name = 'transaction'


class TranUpdateView(UpdateView):
    model = Chek
    template_name = 'transaction/create.html'

    form_class = ChekForm


class TranDeleteView(DeleteView):
    model = Chek
    success_url = '/transaction/'
    template_name = 'transaction/transaction-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ChekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверная'

    form = ChekForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'transaction/create.html', data)
