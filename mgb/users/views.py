from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Character, Item
from .serializers import CharacterSerializer,ItemSerializer,WeaponSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try :
            user=User.objects.get(username=username)
        except:
            raise  AuthenticationFailed('user does not  exist')
        if user and not user.check_password(password):
                raise  AuthenticationFailed('invalid password')
        user=authenticate(username=username,password=password)
        if  user    is  not None:
            
            refresh =   RefreshToken.for_user(user)
            access=str(refresh.access_token)
           
            return  Response({'data':{'refresh':str(refresh),'access':access}},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class CharacterListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        characters = Character.objects.filter(player=request.user)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

class CharacterDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, character_id):
        character = Character.objects.filter(id=character_id, player=request.user).first()
        if character is not None:
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        else:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

class CreateCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(player=request.user)
            return Response({'message': 'Character created successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ItemListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)

class CreateAccountView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Missing username or password'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)
    
class DeleteCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, character_id):
        character = Character.objects.filter(id=character_id, player=request.user).first()
        if character is not None:
            character.delete()
            return Response({'message': 'Character deleted successfully'})
        else:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)
        

class CreateItemView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AddItemToInventoryView(APIView):
    def post(self, request, character_id, item_id):
        character = Character.objects.filter(id=character_id, player=request.user).first()
        item = Item.objects.filter(id=item_id).first()

        if not character:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        inventory = character.inventory

        if item in inventory.items.all():
            return Response({'error': 'Item already in inventory'}, status=status.HTTP_400_BAD_REQUEST)

        inventory.items.add(item)
        return Response({'message': 'Item added to inventory'})
    

class CreateWeaponAPIView(APIView):
    def post(self, request):
        serializer = WeaponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)