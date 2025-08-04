from django.contrib import admin

from apps.portfolio.models.portfolio import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "demo"]
