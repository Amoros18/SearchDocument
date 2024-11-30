from django.urls import path
from . import views

urlpatterns = [
    path("",views.listUser,name="list_user"),
    path("add",views.addUser,name="add_user"),
    path("<int:id>/",views.user, name="user"),
    path("update/<int:id>/",views.updateUser,name="update_user"),
    path("delete/<int:id>/",views.deleteUser,name="delete_user")
]