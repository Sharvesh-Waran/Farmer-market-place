from rest_framework import serializers
#from django.contrib.auth.models import User

from items.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='name.name', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'product_name', 'price', 'quantity']

class SingleTransactionSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='name.name', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'product_name', 'price', 'quantity', 'created_by', 'created_at']
