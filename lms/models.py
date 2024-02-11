from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=8,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    date_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=8,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    date_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    sub_category = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    book_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    date_published= models.DateTimeField()
    status = models.CharField(max_length=8,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(f"{self.book_id}-{self.title}")


class Students(models.Model):
    code=models.CharField(max_length=250,unique=True)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250,blank=True,null=True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20,choices=(('Male','Male'),('Female','Female')),default='Male')
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    department=models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    status = models.CharField(max_length=8,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    date_created = models.DateTimeField(auto_now =True)

    def __str__(self):
        return str(f"{self.code}-{self.first_name}")

class Borrow(models.Model):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    borrowing_date=models.DateField()
    return_date=models.DateField()
    status = models.CharField(max_length=8,choices=(('Returned','Returned'),('Pending','Pending')))
    date_created = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.student.code
    
