# Generated by Django 4.1.5 on 2023-02-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='pic',
            field=models.FileField(default='sad.jpeg', upload_to='seller_pics'),
        ),
    ]