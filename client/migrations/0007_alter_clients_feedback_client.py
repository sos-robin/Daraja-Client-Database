# Generated by Django 4.1.5 on 2023-04-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_clients_feedback_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients_feedback',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='client.client'),
        ),
    ]
