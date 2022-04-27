from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import authenticated_user, permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# --------------- Dashboard Functionality -------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_orders = order.count()
    delivered = order.filter(status='delivered').count()
    pending = order.filter(status='Pending').count()

    context = {'order':order , 'customer':customer, 
         'total_orders':total_orders, 'delivered':delivered  , 'pending':pending}
    return render(request, "dashboard.html", context)

# --------------- SingUp Functionality -------------------

@authenticated_user
def register(request):
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            
           
            messages.success(request, 'Account created for ' + username)
            return redirect('login')
                
    context = {'form':form}
    return render(request, "register.html", context)

# --------------- Login Functionality -------------------

@authenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, "login.html", context)

# --------------- Login Functionality -------------------

def logoutUser(request):
    logout(request)
    return redirect('login')

# --------------- User page Functionality -------------------

@login_required(login_url='login')
@permission(allowed_roles=['customer'])
def Userpage(request):
    orders = request.user.customer.order_set.all()
    
    total_orders = orders.count()
    delivered = orders.filter(status='delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'total_orders':total_orders,
    'delivered':delivered,'pending':pending}
    return render(request, "User.html", context)

# --------------- account Setting Functionality -------------------

@login_required(login_url='login')
@permission(allowed_roles=['customer'])
def account_setting(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect('User')  
    context = {'form':form}
    return render(request, "account_setting.html", context)

# --------------- Customer page Functionality -----------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    order_num = order.count()
      
    myFilter = OrderFilter(request.GET, queryset=order)

    order = myFilter.qs

    context = {'customer':customer, 'order':order, 
    'order_num':order_num, 'myFilter':myFilter}
   
    return render(request, "customer.html", context)

# --------------- Update Customer page Functionality -----------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def Update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = NewCustomer(instance=customer)
    if request.method == 'POST':
        form = NewCustomer( request.POST ,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customer/<str:pk>')

    context = {'form':form}
    return render(request, "update_customer.html", context)

# --------------- Product page Functionality -------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {'products':products})

# --------------- New Product Functionality -------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def New_product(request):
    form = NewProduct
    if request.method == 'POST':
        form = NewProduct(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products')

    context = {'form':form}
    return render(request, "New_product.html", context)

# --------------- create Order Functionality --------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order ,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'create_order.html', context)

# --------------- Update Order Functionality --------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def Update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = NewOrder(instance=order)
    if request.method == 'POST':
        form = NewOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'UpdateOrder.html', context)

# --------------- New Customer Functionality --------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def New_Customer(request):
    form = NewCustomer()
    if request.method == 'POST':
        form = NewCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'create_customer.html', context)

# --------------- delete order Functionality --------------------

@login_required(login_url='login')
@permission(allowed_roles=['admin'])
def delete_order(request , pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()   
        return redirect('/')

    context = {'item':item}
    return render(request, 'delete_order.html', context)