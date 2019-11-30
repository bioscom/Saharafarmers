from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, \
    Country, State, LocalGovt, CropGroup, CropClass, CropSubClass, Farm, ProduceStore

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )





class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'state_name', 'capital', 'slogan')
    list_filter = ('country', 'state_name')

admin.site.register(LocalGovt)


#admin.site.register(CropGroup)
@admin.register(CropGroup)
class CropGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(CropClass)
class CropClassAdmin(admin.ModelAdmin):
    list_display = ('cropgroup', 'class_name')
    list_filter = ('cropgroup', 'class_name')

#admin.site.register(CropClass)
admin.site.register(CropSubClass)


admin.site.register(Farm)
admin.site.register(ProduceStore)