from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200921_1456'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auctions',
            new_name='Auction',
        ),
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='last_bids',
            new_name='last_bid',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='starting_bids',
            new_name='starting_price',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='bids',
            new_name='bid',
        ),
    ]
