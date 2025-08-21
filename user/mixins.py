from django.contrib.auth.mixins import UserPassesTestMixin

class IsStockAdminMixin(UserPassesTestMixin):
    """
    Autorise uniquement les users avec le flag is_stock_admin.
    """
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and getattr(user, 'is_stock_admin', False)

    def handle_no_permission(self):
        from django.contrib import messages
        messages.error(self.request, "Vous n'avez pas les permissions pour cette action.")
        from django.shortcuts import redirect
        return redirect('home')
