from rest_framework import serializers
from    .models  import  Inventory,Character,Item,Weapon,ItemWeapon
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'character', 'items']

class CharacterSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'level', 'inventory']
class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemWeapon
        fields = ['damage_type', 'strength', 'intelligence', 'dexterity', 'item']

    def create(self, validated_data):
        item_data = validated_data.pop('item')
        item = Item.objects.create(**item_data)
        weapon = ItemWeapon.objects.create(item=item, **validated_data)
        return weapon
    
class ItemSerializer(serializers.ModelSerializer):
    weapon = WeaponSerializer(read_only=True,source='itemweapon')
    class Meta:
        model = Item
        fields = ['id', 'name','weapon']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, 'weapon'):
            representation['weapon'] = WeaponSerializer(instance.weapon).data
        return representation

    
class InventorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Inventory
        fields = ['id', 'character', 'items']

class autoInventorySerializer(serializers.ModelSerializer):
    class   Meta:
        model=Inventory
        fields=['id','items']
        depth=1

class CharacterSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'level', 'inventory']

    def create(self, validated_data):
        inventory_data = {}
        character = Character.objects.create(**validated_data)
        inventory = Inventory.objects.create(character=character, **inventory_data)
        return character
    


class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemWeapon
        fields = ['damage_type', 'strength', 'intelligence', 'dexterity', 'item']

    def create(self, validated_data):
        item_data = validated_data.pop('item')
        item = Item.objects.create(**item_data)
        weapon = ItemWeapon.objects.create(item=item, **validated_data)
        return weapon