# Generated by Django 4.0.5 on 2022-06-23 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.SmallIntegerField()),
                ('description', models.CharField(max_length=100)),
                ('Categoryname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='internship.category')),
            ],
        ),
    ]
