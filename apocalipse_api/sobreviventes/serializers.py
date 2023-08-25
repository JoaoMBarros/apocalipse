from rest_framework import serializers
from .models import Sobrevivente, Inventario

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = '__all__'

    def validate_sexo(self, value):
        if value not in ['M', 'F']:
            raise serializers.ValidationError("Sexo inválido")
        return value

class SobreviventeLocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ['latitude', 'longitude']
    
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'
    
    def validate_inventario_disponivel(self, value):
        if value == False:
            raise serializers.ValidationError("Inventario indisponivel")
        return value

class ItemTrocaSerializer(serializers.Serializer):
    agua = serializers.IntegerField(default=0)
    comida = serializers.IntegerField(default=0)
    medicamento = serializers.IntegerField(default=0)
    municao = serializers.IntegerField(default=0)

class TrocaSerializer(serializers.Serializer):
    sobrevivente = serializers.IntegerField()
    itens = ItemTrocaSerializer()

class InfectadoSerializer(serializers.Serializer):
    sobrevivente = serializers.IntegerField()