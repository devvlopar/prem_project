# Generated by Django 4.1.5 on 2023-02-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=100)),
                ('price', models.FloatField(default=10.0)),
                ('product_stock', models.IntegerField(default=0)),
                ('pic', models.FileField(default='sad.jpeg', upload_to='product_pics')),
            ],
        ),
    ]