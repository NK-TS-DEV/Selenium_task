from django.core.management.base import BaseCommand
from Selenium_parser_prod.services.parser import BrainSeleniumParser
from Selenium_parser_prod.models import Product

class Command(BaseCommand):
    help = 'Parse the tool from Brain.com.ua'

    def handle(self, *args, **options):
        bot = BrainSeleniumParser()
        try:
            bot.open_site()
            bot.search_product("Apple iPhone 15 128GB Black")
            bot.go_to_first_product()

            data = bot.run_parser()

            self.save_to_db(data)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Mistake: {e}"))
        finally:
            bot.close()

    def save_to_db(self, data):
        product, created = Product.objects.update_or_create(
            product_code=data.get("Code"),
            defaults={
                "title": data.get("Title"),
                "price": data.get("Price"),
                "sale_price": data.get("Sale_Price"),
                "color": data.get("Color"),
                "memory": data.get("Memory"),
                "manufacturer": data.get("Manufacturer"),
                "display_size": data.get("Display"),
                "resolution": data.get("Resolution"),
                "reviews_count": int(data.get("Reviews", 0)),
                "images": data.get("Image", []),
                "specs": data.get("Characteristics", {})
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"The product was created: {product.title}"))
        else:
            self.stdout.write(self.style.WARNING(f"The product was updated: {product.title}"))