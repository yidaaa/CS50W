# Generated by Django 3.1 on 2020-09-15 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auctions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('category', models.CharField(choices=[('clothes', 'Clothes'), ('shoes', 'Shoes'), ('electronics', 'Electronics'), ('food', 'Food'), ('displays', 'Displays'), ('sports', 'Sports'), ('health', 'Health'), ('furniture', 'Furniture'), ('miscellaneous', 'Miscellaneous')], default='None', max_length=40)),
                ('image_url', models.URLField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bidders', models.ManyToManyField(blank=True, related_name='users_bidding', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watching', models.ManyToManyField(blank=True, related_name='users_watching', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]