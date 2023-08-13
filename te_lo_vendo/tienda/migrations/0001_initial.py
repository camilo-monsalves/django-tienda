# Generated by Django 4.2.4 on 2023-08-10 01:13

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField()),
                ('sku', models.IntegerField()),
                ('disponible', models.BooleanField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rut', models.CharField()),
                ('nombre', models.CharField()),
                ('apellido', models.CharField()),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('cantidad', models.IntegerField()),
                ('direccion', models.CharField()),
                ('formas_pago', models.CharField(choices=[('DEBITO', 'Debito'), ('CREDITO', 'Credito'), ('TRANSFERENCIA', 'Transferencia')], default='DEBITO')),
                ('estado_pedido', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('PREPARACION', 'Preparacion'), ('ENVIADO', 'Enviado')], default='PENDIENTE')),
                ('producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='tienda.producto')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
