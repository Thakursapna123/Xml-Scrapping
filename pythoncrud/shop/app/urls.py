
from django.urls import path
from app import views
urlpatterns = [
path('',views.create,name="create"),

path('delete/<int:id>',views.delete,name="delete"),
path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
path('edit_data/<int:id>',views.edit_data,name="edit_data"),
path('update_item/<int:id>',views.update_item,name="update_item")
# path('edit',views.edit,name="edit")
]