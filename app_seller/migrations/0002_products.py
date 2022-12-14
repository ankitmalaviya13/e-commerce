# Generated by Django 4.1 on 2022-08-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('pic', models.FileField(default='product.jpg', upload_to='products')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.user_seller')),
            ],
        ),
    ]
