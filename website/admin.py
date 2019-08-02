from django.contrib import admin
from .models import Post,Category,Tag,IMG

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(IMG)

#修改网页title和站点header。
'''admin.site.site_title = "登录系统后台"
admin.site.site_header = "汇嘉网站管理系统"
admin.site.index_title = "站点"
'''
