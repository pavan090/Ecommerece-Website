# Generated by Django 4.2.2 on 2023-06-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]
