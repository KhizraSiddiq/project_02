from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201109_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Vehicules', 'Vehicules'), ('Weapons', 'Weapons'), ('Books', 'Books'), ('Multimedia', 'Multimedia'), ('Others', 'Others')], default='', max_length=30),
        ),
    ]