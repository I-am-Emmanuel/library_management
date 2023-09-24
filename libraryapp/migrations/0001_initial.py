# Generated by Django 4.2.5 on 2023-09-24 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('authors', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelfLocation', models.CharField(max_length=50)),
                ('isAvailable', models.BooleanField(default=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='physical_books', to='libraryapp.book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberId', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('borrowed_books', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='borrowers', to='libraryapp.physicalbook')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to='libraryapp.book')),
                ('members', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to='libraryapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='DigitalBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileSize', models.FloatField()),
                ('download_link', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digital_books', to='libraryapp.book')),
            ],
        ),
    ]