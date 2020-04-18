# Generated by Django 3.0.4 on 2020-04-18 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20200418_2157'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='approved_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Staff'),
        ),
    ]