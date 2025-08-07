from django.shortcuts import render

from items.models import Transaction
from items.forms import NewTransactionForm
from core.views import isFarmer, isCustomer

from .serializers import TransactionSerializer, SingleTransactionSerializer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from datetime import datetime

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
            data = {'data' : serializer.data,
                    'message': 'Successfully created new item'}
            return Response(data)
        return Response('Please enter the correct details', status = 400)
    else:
        return Response("Only farmers can create new request", status = 400)

@api_view(('PUT',))
@renderer_classes([JSONRenderer])
def buyItem(request, pk):
    if isCustomer(request):
        transaction = Transaction.objects.get(pk=pk)
        if transaction.is_sold != True:
            transaction.is_sold = True
            transaction.sold_at = datetime.now()
            transaction.sold_to = request.user
            transaction.save()

            serializer = SingleTransactionSerializer(transaction)
            data = {'data' : serializer.data,
                    'message' : 'Successfully bought item'}
            return Response(data)
        return Response('Item already sold', status = 400)
    else:
        return Response("Only customers can buy requests", status = 400)



def browse_transactions(request):
    return render(request, 'api/browse.html')

def render_detail(request, pk):
    return render(request, 'api/detail.html')
