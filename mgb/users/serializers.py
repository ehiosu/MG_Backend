from rest_framework import serializers
from    .models  import  Inventory,Character,Item
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'character', 'items']

class CharacterSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'level', 'inventory']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'character', 'items']

class autoInventorySerializer(serializers.ModelSerializer):
    class   Meta:
        model=Inventory
        fields=['id','items']
        depth=1

class CharacterSerializer(serializers.ModelSerializer):
    inventory = autoInventorySerializer(read_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'level', 'inventory']

    def create(self, validated_data):
        inventory_data = {}
        character = Character.objects.create(**validated_data)
        inventory = Inventory.objects.create(character=character, **inventory_data)
        return character
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']