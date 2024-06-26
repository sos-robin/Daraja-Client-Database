# Generated by Django 4.1.5 on 2023-04-03 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_rename_image_client_company_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.TextField(blank=True, max_length=200, null=True)),
                ('feedback', models.TextField(blank=True, max_length=200, null=True)),
                ('preference', models.TextField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='client.client')),
            ],
        ),
    ]
