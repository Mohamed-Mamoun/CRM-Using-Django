from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.home, name="home"),
    path('customer/<str:pk>/' , views.customer, name="customer"),
    path('Update_customer/<str:pk>/' , views.Update_customer, name="UpdateCustomer"),
    path('product/' , views.products, name="products"),
    path('new_product/' , views.New_product, name="NewProduct"),
    path('register/' , views.register, name="register"),
    path('login/' , views.loginPage, name="login"),
    path('logout/' , views.logoutUser, name="logout"),
    path('User/' , views.Userpage, name="User"),
    path('setting/' , views.account_setting, name="accountSetting"),
    path('create_order/<str:pk>' , views.create_order, name="New_order"),
    path('create_customer/' , views.New_Customer, name="New_customer"),
    path('delete_order/<str:pk>' , views.delete_order, name="delete_order"),
    path('Update_order/<str:pk>' , views.Update_order, name="Update_order"),
    
    # --------- auth Views  -------
    path('Password_reset/' , auth_views.PasswordResetView.as_view(template_name='Password_reset.html'), name="Passord_reset"),
    path('Passord_reset_done/' , auth_views.PasswordResetDoneView.as_view(template_name='Password_reset_sent.html'), name="Password_reset_done"),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name="Password_reset_confirm"),
    path('Password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="Password_reset_complete")

]