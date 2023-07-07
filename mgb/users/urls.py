from django.urls import path
from .views import (
    LoginView,
    CharacterListView,
    CharacterDetailView,
    CreateCharacterView,
    CreateAccountView,
    DeleteCharacterView,
    CreateItemView,
    AddItemToInventoryView,
    CreateWeaponAPIView
   
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('characters/<int:character_id>/', CharacterDetailView.as_view(), name='character_detail'),
    path('create-character/', CreateCharacterView.as_view(), name='create_character'),
    path('create-account/', CreateAccountView.as_view(), name='create_account'),
    path('characters/<int:character_id>/delete/', DeleteCharacterView.as_view(), name='delete_character'),
    path('items/', CreateItemView.as_view(), name='create_item'),
    path('characters/<int:character_id>/inventory/<int:item_id>/add/', AddItemToInventoryView.as_view(), name='add_item_to_inventory'),
     path('weapons/create/', CreateWeaponAPIView.as_view(), name='create_weapon'),

]