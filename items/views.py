from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

from datetime import datetime

from .models import Transaction, Product
from .forms import NewTransactionForm

from core.views import isFarmer, isCustomer

# Create your views here.
@login_required
def items(request):
    query = request.GET.get('query', '')
    transactions = Transaction.objects.filter(is_sold=False)
    product = Product.objects.filter(name__icontains=query)
    if query:
        transactions =  transactions.filter(name = product)

    return render(request, 'item/browse.html', {
        'transactions': transactions,
        'query': query,
    })


@login_required
def browse(request):
    query = request.GET.get('query', '')
    transactions = Transaction.objects.filter(is_sold=False)
    if query:
        transactions =  transactions.filter(name__name__icontains=query)

    return render(request, 'item/browse.html', {
        'transactions': transactions,
        'query': query,
    })

@login_required
def detail(request, pk):

    if request.method != 'POST':

        transaction = get_object_or_404(Transaction, pk=pk)
        related_transactions = Transaction.objects.filter(name=transaction.name, is_sold=False).exclude(pk=pk)[0:3]
        customer_request = isCustomer(request)

        return render(request, 'item/detail.html', {
            'transaction': transaction,
            'related_transactions': related_transactions,
            'isCustomer': customer_request
        })
    
    else:

        if isCustomer(request):

            transaction = Transaction.objects.get(pk=pk)
            if transaction.is_sold != True:
                transaction.is_sold = True
                transaction.sold_at = datetime.now()
                transaction.sold_to = request.user
                transaction.save()
                return redirect('dashboard:index')
            
            return HttpResponse("Error. Item has already been sold")
        
        return HttpResponse("Only Customer can buy the product.")



@login_required
def new(request):

    if isFarmer(request):

        if request.method == 'POST':

            form = NewTransactionForm(request.POST)

            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.created_by = request.user
                transaction.save()

                return redirect('items:detail', pk=transaction.id)
        else:
            form = NewTransactionForm()
        
        return render(request, 'item/form.html', {
            'form':form,
            'title': 'New item'
        })
    
    return HttpResponse("Only Farmers can create a new request.")
            
        
            


    
