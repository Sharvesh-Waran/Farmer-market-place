from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from items.models import Transaction

@login_required
def index(request):
    transactions = Transaction.objects.filter(created_by = request.user)

    return render(request, "dashboard/index.html", {
        'transactions': transactions,
    })
