from django.db import models
from django.utils import timezone
from .models import Author,Translator
from datetime import date
# Create your models here.

class Book(models.Model):
    GENRE_CHOICES=[
        ('Mystery','Mystery'),
        ('Fiction','Fiction'),
        ('Novel','Novel'),
        ('History','History'),
        ('Poetry','Poetry'),
        ('Biography','Biography'),
        ('Romance','Romance'),
        ('philosophy','philosophy'),
        ('Narrative','Narrative'),
        ('Non-fiction','Non-fiction'),
    ]

    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=70,verbose_name="عنوان کتاب")
    author=models.ForeignKey(Author , verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,verbose_name='تعداد ')
    available = models.BooleanField(default=True,verbose_name='در دسترس')
    book_add_time=models.TimeField(default=timezone.now(),verbose_name='زمان اضافه شدن')
    book_add_date=models.DateField(default=date.today(),verbose_name='تاریخ اضافه شدن')
    edition=models.IntegerField(max_length=2,verbose_name='نوبت چاپ')
    category=models.CharField(max_length=20,choices=GENRE_CHOICES ,verbose_name='دسته بندی')
    translator=models.ForeignKey(Translator,on_delete=models.CASCADE, verbose_name='مترجم')
    publication=models.CharField(max_length=70,verbose_name='انتشارات')

    def __str__(self):
        return self.title

class Author(models.Model):
    auth_name=models.CharField(max_length=100,verbose_name='نام نویسنده')

    def __str__(self):
        return self.name
    
class Translator(models.Model):
    tr_name=models.CharField(max_length=100,verbose_name='نام مترجم')

    def __str__(self):
        return self.name

class Members(models.Model):
        member_id=models.IntegerField(primary_key=True)
        name=models.CharField(max_length=250,verbose_name='نام و نام خانوادگی عضو')
        phone=models.CharField(max_length=11,verbose_name='شماره تلفن')
        email=models.EmailField(verbose_name='ایمیل')
        national_id=models.IntegerField(verbose_name='شماره ملی')
        address=models.TextField(verbose_name='آدرس', null=True)
        join_date=models.DateField(verbose_name='تاریخ عضویت')
        expire_date=models.DateField(verbose_name='تاریخ اتمام عضویت')

        def __str__(self):
        return self.name

class ReservationStatus(models.Model):
        book_id=models.ForeignKey(Book , on_delete=models.CASCADE)
        member_id=models.ForeignKey(Members, on_delete=models.CASCADE)
        borrow_date=models.DateField(verbose_name=' تاریخ امانت کتاب' )
        return_date=models.DateField(verbose_name='تاریخ تحویل کتاب')
        def __str__(self):
            return f"{self.members} borrowed {self.book}" 