from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from items.models import Transaction

@login_required
def index(request):
    transactions = Transaction.objects.filter(Q(created_by = request.user) | Q(sold_to = request.user))

    return render(request, "dashboard/index.html", {
        'transactions': transactions,
    })
