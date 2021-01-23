# Generated by Django 3.1.5 on 2021-01-11 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('ine_code', models.IntegerField()),
                ('dc_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('ine_code', models.IntegerField()),
                ('iso_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IdentifierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('ine_code', models.IntegerField()),
            ],
            options={
                'verbose_name': 'identifier type',
                'verbose_name_plural': 'identifier types',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('ine_code', models.IntegerField()),
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'provinces',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RoadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('ine_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'road type',
                'verbose_name_plural': 'road types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_foreign_address', models.BooleanField(default=False, verbose_name='is foreign address')),
                ('road_name', models.TextField(verbose_name='road name')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='number')),
                ('character', models.CharField(blank=True, max_length=5, verbose_name='character')),
                ('floor', models.CharField(blank=True, max_length=10, verbose_name='floor')),
                ('door', models.CharField(blank=True, max_length=10, verbose_name='door')),
                ('stair', models.CharField(blank=True, max_length=10, verbose_name='stair')),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='postal code')),
                ('landline_phone', models.CharField(max_length=30, verbose_name='landline phone')),
                ('mobile_phone', models.CharField(max_length=30, verbose_name='mobile phone')),
                ('email', models.CharField(blank=True, max_length=200, verbose_name='email')),
                ('email_doble_factor', models.CharField(blank=True, max_length=200, null=True, verbose_name='email doble factor')),
                ('region', models.CharField(blank=True, max_length=200, null=True, verbose_name='region')),
                ('town', models.CharField(blank=True, max_length=200, null=True, verbose_name='town')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.country')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.province')),
                ('road_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.roadtype')),
            ],
            options={
                'verbose_name': 'contact data',
                'verbose_name_plural': 'contact data',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.province', verbose_name='province'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=25, verbose_name='identifier')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
                ('surname1', models.CharField(blank=True, max_length=200, verbose_name='first surname')),
                ('surname2', models.CharField(blank=True, max_length=200, verbose_name='second surname')),
                ('gender', models.CharField(blank=True, max_length=200, verbose_name='gender')),
                ('birth_date', models.CharField(blank=True, max_length=200, verbose_name='birth date')),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=30, null=True, unique=True, verbose_name='username')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('create_in', models.DateTimeField(auto_now_add=True, null=True, verbose_name='discharge date')),
                ('contact_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.contactdata')),
                ('ident_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.identifiertype')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'unique_together': {('identifier',)},
            },
        ),
    ]
