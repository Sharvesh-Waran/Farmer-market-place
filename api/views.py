from django.shortcuts import render

from items.models import Transaction
from items.forms import NewTransactionForm
from core.views import isFarmer

from .serializers import TransactionSerializer, SingleTransactionSerializer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Create your views here.

@api_view(('GET',))
@renderer_classes([JSONRenderer])
def getAllItems(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    data = {'data' : serializer.data}
    return Response(data)

@api_view(('GET',))
@renderer_classes([JSONRenderer])
def getItem(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    serializer = SingleTransactionSerializer(transaction)
    data = {'data' : serializer.data}
    return Response(data)

@api_view(('POST',))
@renderer_classes([JSONRenderer])
def newItem(request):
    if isFarmer(request):
        form = NewTransactionForm()
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.created_by = request.user
            transaction.save()

            serializer = SingleTransactionSerializer(transaction)
            data = {'data' : serializer.data}
            return Response(data)
        return Response(serializer.errors)
    else:
        return Response("Only farmers can create new request")


def browse_transactions(request):
    return render(request, 'api/browse.html')

def render_detail(request, pk):
    return render(request, 'api/detail.html')
