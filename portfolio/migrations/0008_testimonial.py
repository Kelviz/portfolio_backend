# Generated by Django 4.2.4 on 2023-08-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_year_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
                ('feedback', models.TextField(max_length=700)),
            ],
        ),
    ]
