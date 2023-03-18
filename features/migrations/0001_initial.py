# Generated by Django 4.1.4 on 2023-03-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='images')),
                ('about', models.TextField()),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('resume', models.FileField(upload_to='resume')),
                ('facebook_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('github_link', models.URLField()),
            ],
            options={
                'verbose_name_plural': '01. Personal Data',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': '07. Contact',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('institution_name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '03. Education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '02. Experience',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_link', models.URLField()),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': '05. Projects',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '04. Skills',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('testimonial', models.TextField()),
            ],
            options={
                'verbose_name_plural': '06. Testimonials',
            },
        ),
    ]