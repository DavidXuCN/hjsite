from urllib.parse import urlencode
from django import template


register = template.Library()

@register.simple_tag
def get_login_qq_url():
    params = {
        'response_type': 'code',
        'client_id': '101734313',
        'redirect_uri': 'https://huijia-cn.com/user/login_by_qq',
        'state': 'hjiewz',
    }
    return 'https://graph.qq.com/oauth2.0/authorize?' + urlencode(params)
