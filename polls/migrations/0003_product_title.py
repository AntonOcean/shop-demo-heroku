# Generated by Django 4.1.3 on 2022-12-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_product_shop_delete_choice_delete_question_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(default="my product", max_length=200),
            preserve_default=False,
        ),
    ]
