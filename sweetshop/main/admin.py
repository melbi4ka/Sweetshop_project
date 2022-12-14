from django.contrib import admin

from sweetshop.main.models import SubscribedUser, AdditionalLinkInformation, Subsections


@admin.register(SubscribedUser)
class SubscribedUserAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'email', 'name', )
    list_filter = ('email', )
    search_fields = ('name', )
    sortable_by = ('id', 'name', )

@admin.register(AdditionalLinkInformation)
class AdditionalLinkInformationAdmin(admin.ModelAdmin):
    fields = ['section_name', 'subsections']
    ordering = ('-id',)
    list_display = ('id', 'section_name', 'list_subsections')
    list_filter = ('section_name',)
    search_fields = ('section_name', )
    sortable_by = ('section_name', )
    list_per_page = 3

    def list_subsections(self, obj):
        return ", ".join([s.subsection_name for s in obj.subsections.all()])

@admin.register(Subsections)
class SubsectionsAdmin(admin.ModelAdmin):
    pass
