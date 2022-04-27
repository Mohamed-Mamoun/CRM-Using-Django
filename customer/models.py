from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# ----------------------Customers Model--------------------------

class Customer(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)

    img = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

# ----------------------Tags Model--------------------------

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# ----------------------Products Model--------------------------

class Product(models.Model):
    CATEGORY = (('indoor','Indoor'), ('out door', 'out door'))

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

# -----------------------Orders Model--------------------------

class Order(models.Model):
    STATUS  = (('Pending','Pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'))
    customer = models.ForeignKey(Customer , null=True, on_delete=SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=SET_NULL)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


