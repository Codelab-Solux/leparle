# Generated by Django 4.1.7 on 2023-04-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_category_image_alter_service_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcategories'),
        ),
    ]