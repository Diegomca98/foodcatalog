# Generated by Django 3.1.7 on 2021-04-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20210411_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.amityinternational.com/wp-content/uploads/2019/02/product-placeholder.jpg', max_length=500),
        ),
    ]
