from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctions_bids_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctions',
            old_name='current_price',
            new_name='last_bids',
        ),
        migrations.RenameField(
            model_name='bids',
            old_name='price',
            new_name='bids',
        ),
        migrations.AddField(
            model_name='auctions',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='auctions',
            name='starting_bids',
            field=models.FloatField(default=0),
        ),
    ]
