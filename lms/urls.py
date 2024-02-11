from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('student_create/',students_register,name='student_create'),
    path('student_list/',student_list,name='student_list'),
    path('student_view/<int:student_id>/',student_viwes,name='student_view'),
    path('student_update/<int:student_id>/',student_update,name='student_update'),
    path('student_delete/<int:student_id>/',student_delete,name='student_delete'),
    path('category_list/',category_list,name='category_list'),
    path('category_create/',category_create,name='category_create'),
    path('category_view/<int:c_id>/', category_view, name='category_view'),
    path('category_update/<int:c_id>/', category_update, name='category_update'),
    path('category_delete/<int:c_id>/', category_delete, name='category_delete'),
    path('subcategory_list/', sub_category_list, name='subcategory_list'),
    path('subcategory_create/', sub_category_create, name='subcategory_create'),
    path('subcategory_update/<int:sub_id>/', sub_category_update, name='subcategory_update'),
    path('subcategory_view/<int:sub_id>/', sub_category_view, name='subcategory_view'),
    path('subcategory_delete/<int:sub_id>/', sub_category_delete, name='subcategory_delete'),
    path('book_list/', book_list, name='book_list'),
    path('book_create/', book_create, name='book_create'),
    path('book_update/<int:b_id>/', book_update, name='book_update'),
    path('book_delete/<int:b_id>/', book_delete, name='book_delete'),
    path('book_view/<int:b_id>/', book_view, name='book_view'),
    path('transaction_list/',transaction_list,name='transaction_list'),
    path('transaction_create/',transaction_create,name='transaction_create'),
    path('transaction_view/<int:borrow_id>/',transaction_view,name='transaction_view'),
    path('transaction_update/<int:borrow_id>/',transaction_update,name='transaction_update'),
    path('transaction_delete/<int:borrow_id>/',transaction_delete,name='transaction_delete'),

]

