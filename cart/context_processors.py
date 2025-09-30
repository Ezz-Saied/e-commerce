from .models import CartItem

def cart(request):
    if request.user.is_authenticated:
        return {
            "cart_total_items": CartItem.objects.get_total_items(request.user),
            "cart_grand_total": CartItem.objects.grand_total(request.user),
        }
    return {
        "cart_total_items": 0,
        "cart_grand_total": 0,
    }
