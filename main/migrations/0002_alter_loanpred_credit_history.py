# Generated by Django 4.1 on 2023-05-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanpred',
            name='credit_history',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], max_length=4, verbose_name='Credit Histroy'),
        ),
    ]