from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('client_list/',views.Client_List, name="Clients"),
    #path of the view in the client_List
    path('clients_data/<str:cd_ID>/' , views.Clients_data, name="clients_data"),
    path('client_info/',views.Client_Info, name="client_info"),
    path('Client_Payments/',views.Client_Payments,name="Client_Payments"),
    #path of the view in clients_payment
    path('client_pay/<str:cp_id>/',views.Clients_pay, name="client_pay"),
    path('clients_docs/', views.Client_Documents, name="clients_docs"),
    path('billing/',views.Billing,name="billing"),
    path('General-notes/',views.General_Notes,name ="General-notes"),
    #add a path for create client in client_list
    path('create_client/', views.createClient, name="create_client"),
    path('update_client/<str:pku>/', views.updateClient, name="update_client"),
    path('delete_client/<str:pku>/', views.deleteClient, name="delete_client"),
    path('edit_personalinfo/<str:pku>/', views.editPersonalinfo, name="edit_personalinfo"),
    path('edit_companyinfo/<str:pku>/', views.editcompanyinfo, name="edit_companyinfo"),
    path('upload_profile_picture/', views.profilePic, name='upload_profile_picture'),
]