# Generated by Django 4.2.7 on 2024-02-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0011_remove_books_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='status',
            field=models.CharField(choices=[('Returned', 'Returned'), ('Pending', 'Pending')], max_length=8),
        ),
    ]
