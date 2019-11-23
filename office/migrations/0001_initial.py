# Generated by Django 2.2.7 on 2019-11-23 21:12

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('visit_addr', models.CharField(blank=True, max_length=500)),
                ('send_mail_opt', models.CharField(choices=[('0', 'not sent'), ('1', 'already sent'), ('2', 'send now!!')], default='0', max_length=15)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Host')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Visitor')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='visits',
            field=models.ManyToManyField(through='office.Visit', to='office.Visitor'),
        ),
    ]
