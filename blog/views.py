import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from .models import Blog, Category
from read_statistics.utils import read_statistics_once_read
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
# from django.urls import reverse
from blog.models import Blog
# from comment.models import Comment
# from comment.forms import CommentForm
# from user.forms import LoginForm


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)   
    blogs = Blog.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def blog_home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 3600)
    
    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_days'] = hot_blogs_for_7_days
    return render(request, 'blog_home.html', context)

def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER) # 进行分页
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >=2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >=2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('publish_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(publish_time__year=blog_date.year,
                        publish_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    # 获取博客分类的对应博客数量    
    '''categorys = Category.objects.all()
    category_list = []
    for category in categorys:
        category.blog_count = Blog.objects.filter(category=category).count()
        category_list.append(category)'''

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['categorys'] = Category.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_dict
    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render(request, 'blog_list.html', context)

def blog_category(request, blog_category_pk):
    category = get_object_or_404(Category, pk=blog_category_pk)
    blogs_all_list = Blog.objects.filter(category=category)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['category'] = category
    return render(request, 'blog_category.html', context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(publish_time__year=year, publish_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s/%s' % (year, month)
    return render(request, 'blogs_with_date.html', context)

def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)
    # blog_content_type = ContentType.objects.get_for_model(blog)
    # comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk, parent=None)

    blogs_all_list = Blog.objects.all()

    context = {}
    context = get_blog_list_common_data(request, blogs_all_list)
    context['previous_blog'] = Blog.objects.filter(publish_time__gt=blog.publish_time).last()
    context['next_blog'] = Blog.objects.filter(publish_time__lt=blog.publish_time).first()
    context['blog'] = blog
    # context['login_form'] = LoginForm()
    # context['comments'] = comments.order_by('-comment_time')
    # context['comment_form'] = CommentForm(initial={'content_type': blog_content_type.model, 'object_id': blog_pk, 'reply_comment_id': 0})
    response = render(request, 'blog_detail.html', context) # 响应
    response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response