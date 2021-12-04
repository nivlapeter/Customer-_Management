from management.models import Customer, Order, Product
from django.shortcuts import render, redirect
# creates multiple forms within one form
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# flash message that sends a one time message to the template
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()  # CreateUserForm beibg rendered to the template

    if request.method == "POST":
        # the form is rendered and the data passed in
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # gets a single form attribute
            # allows for getting the username without other form attributes
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'customer/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")  # fetches the username
        password = request.POST.get("password")  # fetches the password

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(
                request, "Check your username or password and try again")

    context = {}
    return render(request, 'customer/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()  # orders summation

    delivered = orders.filter(
        status='delivered').count()  # delivered summation
    pending = orders.filter(status='pending').count()  # pending summation

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request, 'customer/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    # Querying orders relevant to the given user
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()  # orders summation

    delivered = orders.filter(
        status='delivered').count()  # delivered summation
    pending = orders.filter(status='pending').count()  # pending summation

    context = {'orders': orders, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'customer/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        # request.FILES takes in any files that are recieved, POST data is passed in.
        form = CustomerForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():  # checks form validation
        form.save()  # saves the form

    context = {'form': form}
    return render(request, 'customer/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'customer/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    order_count = orders.count()

    context = {'customer': customer, 'orders': orders,
               'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'customer/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields={'product', 'status'}, extra=10)  # creating an instance, extra sets how many form options get displayed
    customer = Customer.objects.get(id=pk)  # customer instance
    #form = OrderForm(initial={'customer':customer})
    # queryset avoids the prefilled display in the forms,formset allows creation of multiple forms on the same page
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formset.is_Valid():
            formset.save()
            return redirect('/')  # redirects back to the home page

    context = {'formset': formset}  # Parsing to the template
    return render(request, 'customer/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirects back to the home page
    context = {'order': order}
    return render(request, 'customer/order_form', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()  # delets the order
        return redirect('/')  # redirects back to the home page

    context = {'item': order}
    return render(request, 'customer/delete.html', context)
