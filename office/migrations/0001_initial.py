# Generated by Django 2.2.7 on 2019-11-20 17:23

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('h_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('v_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('vh_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField(auto_now=True)),
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