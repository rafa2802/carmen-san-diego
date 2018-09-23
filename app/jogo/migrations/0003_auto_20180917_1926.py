# Generated by Django 2.0.7 on 2018-09-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0002_auto_20180917_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='pais_dois',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paisdois', to='jogo.Pais', verbose_name='País Dois'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais_dois_imagem',
            field=models.ImageField(blank=True, null=True, upload_to='paises/', verbose_name='Bandeira do País Dois'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais_um',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paisum', to='jogo.Pais', verbose_name='País Um'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais_um_imagem',
            field=models.ImageField(blank=True, null=True, upload_to='paises/', verbose_name='Bandeira do País Um'),
        ),
    ]