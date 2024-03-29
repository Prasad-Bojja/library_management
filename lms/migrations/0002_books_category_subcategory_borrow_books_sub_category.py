# Generated by Django 4.2.7 on 2024-01-09 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=250)),
                ('publisher', models.CharField(max_length=250)),
                ('date_published', models.DateTimeField()),
                ('status', models.CharField(choices=[(1, 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[(1, 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[(1, 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.category')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateField()),
                ('return_date', models.DateField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.books')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.students')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.subcategory'),
        ),
    ]
