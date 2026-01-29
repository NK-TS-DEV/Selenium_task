import csv
from Selenium_parser_prod.models import Product

def export_products_to_csv(path="brain_products.csv"):
    products = Product.objects.all()

    headers = [
        "Title", "Price", "Sale price", "Code", "Reviews",
        "Color", "Memory", "Manufacturer", "Display size",
        "Resolution", "Images", "Specs"
    ]

    with open(path, "w", newline="", encoding="utf-8-sig") as f:

        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerow(headers)

        for p in products:
            images_str = ", ".join(p.images) if isinstance(p.images, list) else str(p.images)

            if isinstance(p.specs, dict):
                chars_str = "\n".join([f"{k}: {v}" for k, v in p.specs.items()])
            else:
                chars_str = str(p.specs)

            writer.writerow([
                p.title,
                p.price,
                p.sale_price or "",
                p.product_code,
                p.reviews_count,
                p.color or "",
                p.memory or "",
                p.manufacturer or "",
                p.display_size or "",
                p.resolution or "",
                images_str,
                chars_str
            ])