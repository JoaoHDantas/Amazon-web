# Generated by Django 5.0.6 on 2024-05-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprar_novamente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('preco', models.CharField(max_length=20, null=True)),
                ('descricao', models.TextField(null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
