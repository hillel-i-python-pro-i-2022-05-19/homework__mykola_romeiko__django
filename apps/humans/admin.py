from django.contrib import admin

from .models import Human, Color, SuperHuman

admin.site.register(Human)


# admin.site.register(Color)
# admin.site.register(SuperHuman)

class SuperHumanAdminInline(admin.TabularInline):
    model = SuperHuman


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    inlines = (
        SuperHumanAdminInline,
    )


@admin.register(SuperHuman)
class SuperHumanAdmin(admin.ModelAdmin):
    ...
