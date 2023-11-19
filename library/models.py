from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from datetime import date
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
    description=models.TextField(max_length=250,verbose_name='توضیحات',null=True)
    author=models.CharField(max_length=200 , verbose_name=("نویسنده"))
    quantity=models.IntegerField(default=1,verbose_name='تعداد',null=True)
    available = models.BooleanField(default=True,verbose_name='در دسترس')
    book_add_date=models.DateTimeField(default=timezone.now,verbose_name='زمان اضافه شدن')
    edition=models.IntegerField(verbose_name='نوبت چاپ')
    category=models.CharField(max_length=20,choices=GENRE_CHOICES,verbose_name='دسته بندی')
    translator=models.CharField(max_length=200, verbose_name='مترجم')
    publication=models.CharField(max_length=70,verbose_name='انتشارات')
    slug=models.SlugField(max_length=250,verbose_name='اسلاگ',null=True)
    class Meta :
        ordering = ['-book_add_date']
        indexes = [
            models.Index(fields = ['-book_add_date'])
        ]
        verbose_name="کتاب"
        verbose_name_plural="کتاب ها"

    def __str__(self):
        return self.title


class Members(models.Model):
        member_id=models.IntegerField(primary_key=True)
        full_name=models.CharField(max_length=250,verbose_name='نام و نام خانوادگی عضو')
        phone=models.CharField(max_length=11,verbose_name='شماره تلفن')
        email=models.EmailField(verbose_name='ایمیل')
        national_id=models.IntegerField(verbose_name='شماره ملی')
        address=models.TextField(verbose_name='آدرس', null=True)
        join_date=models.DateField(verbose_name='تاریخ عضویت')
        expire_date=models.DateField(verbose_name='تاریخ اتمام عضویت')

        def __str__(self):
            return self.name

class BookStatus(models.Model):
        book_id=models.ForeignKey(Book , on_delete=models.CASCADE)
        member_id=models.ForeignKey(Members, on_delete=models.CASCADE)
        borrow_date=models.DateField(verbose_name='تاریخ امانت کتاب' )
        return_date=models.DateField(verbose_name='تاریخ تحویل کتاب')
        def __str__(self):
            return f"{self.members} borrowed {self.book}" 