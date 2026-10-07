from .models import Category


def menu_links(request):
    """
    Return all categories as a dictionary so every template can use it.
    Key name: links
    """
    links = Category.objects.all()
    return dict(links=links)
