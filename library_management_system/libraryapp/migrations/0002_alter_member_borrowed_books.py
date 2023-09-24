# Generated by Django 4.2.5 on 2023-09-24 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='borrowed_books',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowers', to='libraryapp.physicalbook'),
        ),
    ]
