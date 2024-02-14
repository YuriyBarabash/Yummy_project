from .models import FooterItem


def footer_items(request):
    return {'footer_items': FooterItem.objects.first()}