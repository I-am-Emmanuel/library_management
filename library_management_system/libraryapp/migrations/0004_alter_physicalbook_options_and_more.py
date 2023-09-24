# Generated by Django 4.2.5 on 2023-09-24 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_alter_member_borrowed_books'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='physicalbook',
            options={'ordering': ['shelfLocation']},
        ),
        migrations.AlterField(
            model_name='member',
            name='borrowed_books',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowers', to='libraryapp.physicalbook'),
        ),
    ]