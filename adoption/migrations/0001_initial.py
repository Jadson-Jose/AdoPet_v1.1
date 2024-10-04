# Generated by Django 5.1.1 on 2024-10-03 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopter', '0001_initial'),
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(auto_now=True)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopter.adopter')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
    ]