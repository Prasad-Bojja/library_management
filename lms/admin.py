from django.contrib import admin
from .models import*

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','description','status','date_created']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['category','name','description','status','date_created']

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display=['sub_category','book_id','title','description','author','publisher','date_published','status','date_created']

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['code','first_name','middle_name','last_name','gender','contact','email','address','department','course','status','date_created']

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['student','book','borrowing_date','return_date','status','date_created']
