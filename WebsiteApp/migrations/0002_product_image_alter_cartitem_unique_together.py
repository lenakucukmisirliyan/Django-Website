# Generated by Django 5.0.2 on 2024-04-11 18:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('user', 'product')},
        ),
    ]
