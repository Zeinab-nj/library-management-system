# Generated by Django 4.2.5 on 2023-11-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_book_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=250, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(verbose_name='نوبت چاپ'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1, null=True, verbose_name='تعداد'),
        ),
    ]
