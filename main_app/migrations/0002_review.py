# Generated by Django 4.0.1 on 2023-02-07 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('lastModified', models.DateField(auto_now=True)),
                ('review', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.record')),
            ],
        ),
    ]
