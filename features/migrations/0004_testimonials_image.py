# Generated by Django 4.1.4 on 2023-03-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_education_order_experience_order_project_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(blank=True, upload_to='testimonial_images'),
        ),
    ]