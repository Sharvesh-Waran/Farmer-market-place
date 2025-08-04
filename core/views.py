from django.shortcuts import render, redirect
#from django.contrib.auth import logout

from items.models import Product, Transaction

from .forms import SignupForm
from .models import UserProfile, Role

# Create your views here.

def isFarmer(request):
    try:
        farmer_role = Role.objects.get(name = 'Farmer')
        return UserProfile.objects.filter(user=request.user, role=farmer_role)
    except Role.DoesNotExist:
        return False
    
def isCustomer(request):
    try:
        customer_role = Role.objects.get(name = 'Customer')
        return UserProfile.objects.filter(user=request.user, role=customer_role)
    except Role.DoesNotExist:
        return False


def index(request):
    transactions = Transaction.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    products = Product.objects.all()
    return render(request, 'core/index.html', {
        'transactions': transactions,
        'products': products,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
'''
def logout_view(request):
    logout(request)

    return redirect(request, '/logout/')'''