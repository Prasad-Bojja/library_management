from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .form import*
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    category_count = Category.objects.filter(status='Active').count()
    subcategory_count = Subcategory.objects.filter(status='Active').count()
    book_count = Books.objects.filter(status='Active').count()
    student_count = Students.objects.filter(status='Active').count()
    pending_count = Borrow.objects.filter(status='Pending').count()
    returned_count = Borrow.objects.filter(status='Returned').count()


    context = {
        'category': category_count,
        'subcategory': subcategory_count,
        'book': book_count,
        'student': student_count,
        'pending': pending_count,
        'returned': returned_count
    }
    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def students_register(request):

    try:
        if request.method == 'POST':
            code=request.POST.get('code')
            first_name=request.POST.get('first_name')
            middle_name=request.POST.get('middle_name')
            last_name=request.POST.get('last_name')
            gender=request.POST.get('gender')
            contact=request.POST.get('contact')
            email=request.POST.get('email')
            address=request.POST.get('address')
            department=request.POST.get('department')
            course=request.POST.get('course')
            status=request.POST.get('status')

            student= Students(
                code=code,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                gender=gender,
                contact=contact,
                email=email,
                address=address,
                department=department,
                course=course,
                status=status
            )
            student.save()
            messages.success(request,"Student Registration successfully !!!!")
            return redirect('/student_list/')
    except Exception:
        messages.success(request,'Please check your Student ID or Email or Contact Already Taken !!!!!!!!')
    return render(request, 'students_register.html')

@login_required(login_url='/login/')
def student_list(request):
    quary=Students.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(code__icontains= request.GET.get('search'))

    paginator = Paginator(quary, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request,'student_list.html',{'students':page_obj})

@login_required(login_url='/login/')
def student_viwes(request,student_id):
    quary=Students.objects.get(id=student_id)
    return render(request,'student_view.html',{'details':quary})

@login_required(login_url='/login/')
def student_update(request,student_id):
    try:
        quary=Students.objects.get(id=student_id)
        if request.method == 'POST':
            data = request.POST
            code=data.get('code')
            first_name=data.get('first_name')
            middle_name=data.get('middle_name')
            last_name=data.get('last_name')
            gender=data.get('gender')
            contact=data.get('contact')
            email=data.get('email')
            address=data.get('address')
            department=data.get('department')
            course=data.get('course')
            status=data.get('status')
            quary.code=code
            quary.first_name=first_name
            quary.middle_name=middle_name
            quary.last_name=last_name
            quary.gender=gender
            quary.contact=contact
            quary.email=email
            quary.address=address
            quary.department=department
            quary.course=course
            quary.status=status
            quary.save()
            messages.success(request,'Student information Update Successfully !!!!')
            return redirect("/student_list/")
    except Exception:
        messages.error(request,'Please check your Student ID or Email or Contact Already Taken !!!!!!!!')

    context={'student':quary}
    return render(request,'student_update.html',context)

@login_required(login_url='/login/')
def student_delete(request,student_id):
    quary=Students.objects.get(id=student_id)
    quary.delete()
    return redirect('/student_list/')

@login_required(login_url='/login/')
def category_list(request):
    quary=Category.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(name__icontains= request.GET.get('search'))
    
    paginator = Paginator(quary, 5)  # Show 5 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request,'category_list.html',{'categories':page_obj})


@login_required(login_url='/login/')
def category_create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        status=request.POST.get('status')

        category=Category(name=name,description=description,status=status)
        category.save()
        messages.success(request,"category created Successfully !!!")
        return redirect('/category_list/')
        
    return render(request,'category_create.html')


@login_required(login_url='/login/')
def category_update(request, c_id):
    quary = get_object_or_404(Category, id=c_id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        status = data.get('status')
        quary.name = name
        quary.description = description
        quary.status = status
        quary.save()
        messages.success(request, 'Category Updated Successfully !!!!')
        return redirect('/category_list/')
    context = {'category': quary}
    return render(request, 'category_update.html', context)


@login_required(login_url='/login/')
def category_delete(request, c_id):
    quary = get_object_or_404(Category, id=c_id)
    quary.delete()
    return redirect('/category_list/')


@login_required(login_url='/login/')
def category_view(request,c_id):
    quary = get_object_or_404(Category, id=c_id)
    return render(request, 'category_view.html', {'category':quary})


@login_required(login_url='/login/')
def sub_category_create(request):
    categories=Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category')
        name= request.POST.get('name')
        description = request.POST.get('description')
        status=request.POST.get('status')

        if not category_id:
            messages.error(request,'Category name required !!!')
            return redirect('/subcategory_create/')
        
        category= Category.objects.get(pk=category_id)

        subcategory = Subcategory(
            category=category,
            name=name,
            description=description,
            status=status
        )
        subcategory.save()
        messages.success(request,'Subcategory created Successfully !!!!!')
        return redirect('/subcategory_list/')

    return render(request,'sub_category_create.html',{'categories':categories})


@login_required(login_url='/login/')
def sub_category_update(request, sub_id):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(id=sub_id)

    if request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        # Validate input (you may add more validation as needed)
        if not category_id or not name:
            messages.error(request, 'Category and Name are required')
            return redirect('sub_category_update', sub_id=sub_id)

        # Get the category instance
        category = Category.objects.get(pk=category_id)

        # Update Subcategory instance
        subcategory.category = category
        subcategory.name = name
        subcategory.description = description
        subcategory.status = status
        subcategory.save()

        messages.success(request, 'Subcategory updated successfully')
        return redirect('subcategory_list')  # Replace 'sub_category_list' with the actual URL name

    context = {'subcategory': subcategory, 'categories': categories}
    return render(request, 'sub_category_update.html', context)



@login_required(login_url='/login/')
def sub_category_list(request):
    quary=Subcategory.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(name__icontains= request.GET.get('search'))
    
    paginator = Paginator(quary, 5)  # Show 5 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context={'subcategories': page_obj}
    return render(request,'sub_category_list.html',context)


@login_required(login_url='/login/')
def sub_category_view(request,sub_id):
    quary=Subcategory.objects.get(id=sub_id)
    return render(request,'sub_category_view.html',{'subcategory':quary})

@login_required(login_url='/login/')
def sub_category_delete(request,sub_id):
    quary=Subcategory.objects.get(id=sub_id)
    quary.delete()
    return redirect('/subcategory_list/')

@login_required(login_url='/login/')
def book_create(request):
    
    subcategories=Subcategory.objects.all()
    
    if request.method == 'POST':
        try:  
            subcategory_id=request.POST.get('sub_category')
            book_id=request.POST.get('book_id')
            title=request.POST.get('title')
            description=request.POST.get('description')
            author=request.POST.get('author')
            publisher=request.POST.get('publisher')
            date_published=request.POST.get('date_published')
            status=request.POST.get('status')
            
            if not subcategory_id:
                messages.error(request,'Subcategory must required !!!!!')
                return redirect('/book_list/') 
            sub_category=Subcategory.objects.get(pk=subcategory_id)
            book=Books(
                sub_category=sub_category,
                book_id=book_id,
                title=title,
                description=description,
                author=author,
                publisher=publisher,
                date_published=date_published,
                status=status
            )
            book.save()
            messages.success(request,'Book Created Successfully !!!!')
            return redirect('/book_list/')
        except Exception:
            messages.error(request,'this Book id already taken !!!!!!!!!')
    
    return render(request,'book_create.html',{'subcategories':subcategories})

@login_required(login_url='/login/')
def book_update(request, b_id):
    subcategories = Subcategory.objects.all()
    book = get_object_or_404(Books, id=b_id)

    if request.method == 'POST':
        subcategory_id = request.POST.get('sub_category')
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        date_published_str = request.POST.get('date_published')
        status = request.POST.get('status')

        if not subcategory_id:
            messages.error(request, 'Subcategory is required!')
        else:
            try:
                subcategory = Subcategory.objects.get(pk=subcategory_id)
                
                # Parse the date string into a datetime object
                date_published = datetime.strptime(date_published_str, '%Y-%m-%dT%H:%M')

                book.sub_category = subcategory
                book.book_id = book_id
                book.title = title
                book.description = description
                book.author = author
                book.publisher = publisher
                book.date_published = date_published
                book.status = status
                book.save()

                messages.success(request, 'Book updated successfully!')
                return redirect('book_list')  
            except Exception as e:
                messages.error(request, 'book id already taken !!!!!!')

    context = {'book': book, 'subcategories': subcategories}
    return render(request, 'book_update.html', context)


@login_required(login_url='/login/')
def book_list(request):
    quary=Books.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(title__icontains= request.GET.get('search'))
    paginator = Paginator(quary, 5)  # Show 5 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context={'books': page_obj}
    return render(request,'book_list.html',context)

@login_required(login_url='/login/')
def book_delete(request,b_id):
    quary=Books.objects.get(id=b_id)
    quary.delete()
    return redirect('/book_list/')

@login_required(login_url='/login/')
def book_view(request,b_id):
    quary=Books.objects.get(id=b_id)
    return render(request,'book_view.html',{'book':quary})

@login_required(login_url='/login/')
def transaction_list(request):
    quary=Borrow.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(book__icontains= request.GET.get('search'))
    paginator = Paginator(quary, 5)  # Show 5 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context={'borrows': page_obj}
    return render(request,'transaction_list.html',context)


@login_required(login_url='/login/')
def transaction_create(request):
    students = Students.objects.all()
    books = Books.objects.all()

    if request.method == 'POST':
        try:
            book_id = request.POST.get('book')
            student_id = request.POST.get('student')
            borrowing_date = request.POST.get('borrowing_date')
            return_date = request.POST.get('return_date')
            status = request.POST.get('status')

            if not (book_id and student_id):
                raise ValueError('Both Book and Student fields are required for creating a transaction!')

            student = Students.objects.get(pk=student_id)
            book = Books.objects.get(pk=book_id)

            Borrow.objects.create(
                student=student,
                book=book,
                borrowing_date=borrowing_date,
                return_date=return_date,
                status=status
            )
            messages.success(request, 'Book borrowing transaction created successfully!')
            return redirect('/transaction_create/')  
        except (Students.DoesNotExist, Books.DoesNotExist) as e:
            messages.error(request, 'Student or book does not exist. Please select valid options.')

    context = {'students': students, 'books': books}
    return render(request, 'transaction_create.html', context)


@login_required(login_url='/login/')
def transaction_view(request,borrow_id):
    quary=Borrow.objects.get(id=borrow_id)
    book=Books.objects.all()
    student=Students.objects.all()
    context={'borrow':quary,'books':book,'students':student}
    return render(request,'transaction_view.html',context)


@login_required(login_url='/login/')
def transaction_update(request,borrow_id):
    quary=Borrow.objects.get(id=borrow_id)
    students = Students.objects.all()
    books = Books.objects.all()
    
    if request.method == 'POST':
        try:
            book_id = request.POST.get('book')
            student_id = request.POST.get('student')
            borrowing_date = request.POST.get('borrowing_date')
            return_date = request.POST.get('return_date')
            status = request.POST.get('status')

            if not (book_id and student_id):
                raise ValueError('Both Book and Student fields are required for updating a transaction!')

            student = Students.objects.get(pk=student_id)
            book = Books.objects.get(pk=book_id)

            quary.student=student
            quary.book=book
            quary.borrowing_date=borrowing_date
            quary.return_date=return_date
            quary.status=status
            quary.save()
            messages.success(request, 'Book borrowing transaction Updated successfully!')
            return redirect('/transaction_list/')  
        except (Students.DoesNotExist, Books.DoesNotExist) as e:
            messages.error(request, 'Student or book does not exist. Please select valid options.')

    context = {'borrow':quary,'students': students, 'books': books}
    return render(request, 'transaction_update.html', context)


@login_required(login_url='/login/')
def transaction_delete(request,borrow_id):
    quary=Borrow.objects.get(id=borrow_id)
    quary.delete()
    return redirect('/transaction_list/')

