from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'lib/index.html'),

def book_list(request):
    books=Book.objects.all()
    return render(request,'library/list.html',{"books" : books})
    
def book_status(request,id):
    book=get_object_or_404(Book,pk=id)
    book_statuses=BookStatus.objects.filter(book_id=book)
    context={
        "book":book,
        "book_statuses":book_statuses,
    }
    return render(request,'library/book_status.html',context)
    