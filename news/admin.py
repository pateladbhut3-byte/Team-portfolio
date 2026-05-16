from django.contrib import admin
from django.utils.html import format_html
from news.models import News
class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_des','download_pdf')

    def download_pdf(self, obj):
        if obj.form_pdf:
            return format_html(
                '<a href="{}" download target="_blank">Download FILES</a>',
                obj.form_pdf.url
            )
        return "No File"

    download_pdf.short_description = " FILES"

admin.site.register(News,NewsAdmin)
# Register your models here.
