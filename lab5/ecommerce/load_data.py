"""
Sample data loader for lab5.
Run: py manage.py shell < load_data.py
Creates 5 categories and 11 products using downloaded images.
"""
from store.models import Category, Product

categories_data = [
    ('Electronics', 'electronics', 'Gadgets and devices', 'photos/categories/electronics.jpg'),
    ('Fashion', 'fashion', 'Clothing and style', 'photos/categories/fashion.jpg'),
    ('Shoes', 'shoes', 'Sneakers and footwear', 'photos/categories/shoes.jpg'),
    ('Accessories', 'accessories', 'Watches and extras', 'photos/categories/accessories.jpg'),
    ('Sport', 'sport', 'Sports equipment', 'photos/categories/sport.jpg'),
]

categories = {}
for name, slug, desc, img in categories_data:
    cat, created = Category.objects.get_or_create(
        slug=slug,
        defaults={
            'category_name': name,
            'description': desc,
            'cat_image': img,
        },
    )
    if not created:
        cat.category_name = name
        cat.description = desc
        cat.cat_image = img
        cat.save()
    categories[slug] = cat
    print(('Created' if created else 'Updated') + ' category: ' + name)

products_data = [
    ('Classic Watch', 'classic-watch', 'Elegant classic wrist watch', 120, 'photos/products/watch.jpg', 15, 'accessories'),
    ('Headphones Pro', 'headphones-pro', 'Over-ear headphones with deep bass', 89, 'photos/products/headphones.jpg', 20, 'electronics'),
    ('Nike Red Runner', 'nike-red-runner', 'Red Nike running shoes', 150, 'photos/products/nike-red.jpg', 10, 'shoes'),
    ('Smart Watch X', 'smart-watch-x', 'Smartwatch with fitness tracking', 199, 'photos/products/smartwatch.jpg', 12, 'electronics'),
    ('White Sneakers', 'white-sneakers', 'Minimal white sneakers', 95, 'photos/products/white-shoe.jpg', 18, 'shoes'),
    ('DSLR Camera', 'dslr-camera', 'Professional DSLR camera', 650, 'photos/products/camera.jpg', 5, 'electronics'),
    ('Polarized Sunglasses', 'polarized-sunglasses', 'UV protection sunglasses', 45, 'photos/products/sunglasses.jpg', 30, 'accessories'),
    ('Street Sneaker', 'street-sneaker', 'Comfortable street sneaker', 110, 'photos/products/sneaker.jpg', 14, 'shoes'),
    ('Studio Headphones', 'studio-headphones', 'White studio headphones', 130, 'photos/products/headphones-white.jpg', 8, 'electronics'),
    ('Travel Backpack', 'travel-backpack', 'Durable travel backpack', 75, 'photos/products/backpack.jpg', 22, 'sport'),
    ('Cotton T-Shirt', 'cotton-tshirt', 'Soft cotton t-shirt', 25, 'photos/products/tshirt.jpg', 40, 'fashion'),
]

for name, slug, desc, price, img, stock, cat_slug in products_data:
    prod, created = Product.objects.get_or_create(
        slug=slug,
        defaults={
            'product_name': name,
            'description': desc,
            'price': price,
            'images': img,
            'stock': stock,
            'is_available': True,
            'category': categories[cat_slug],
        },
    )
    if not created:
        prod.product_name = name
        prod.description = desc
        prod.price = price
        prod.images = img
        prod.stock = stock
        prod.category = categories[cat_slug]
        prod.save()
    print(('Created' if created else 'Updated') + ' product: ' + name)

print('')
print('Done! Categories: ' + str(Category.objects.count()) + ', Products: ' + str(Product.objects.count()))
