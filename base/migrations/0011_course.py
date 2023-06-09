# Generated by Django 4.2 on 2023-05-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_sector_image_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('document', models.FileField(blank=True, null=True, upload_to='docs')),
                ('is_popular', models.BooleanField(default=False)),
                ('sector', models.ManyToManyField(blank=True, to='base.sector')),
            ],
        ),
    ]
