from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201004_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Vehicules', 'Vehicules'), ('Weapons', 'Weapons'), ('Books', 'Books'), ('Multimedia', 'Multimedia')], default='', max_length=30),
        ),
    ]
