from django.conf.urls.defaults import *

urlpatterns = patterns('target.views',
    (r'^company/$','company_view_all'),
    (r'^company/new/$','company_add'),
    (r'^company/(?P<slug>[\w-]+)/$','company_view'),
    (r'^company/(?P<slug>[\w-]+)/edit/$','company_edit'),
    (r'^product/$','product_view_all'),
    (r'^product/new/$','product_add'),
    (r'^product/upc/(?P<upc>[\d-]+)/$','product_upc'),
    (r'^product/(?P<slug>[\w-]+)/$','product_view'),
    (r'^product/(?P<slug>[\w-]+)/edit/$','product_edit'),
    (r'^tag/(?P<tag>[\w-]+)/$','tag_view'),
    (r'^tag/(?P<tags_flat>[\w\-\+]+)/$','tag_multiple_view'),
    (r'^campaign/$','campaign_view_all'),
    (r'^campaign/new/$','campaign_add'),
    (r'^campaign/(?P<slug>[\w-]+)/$','campaign_view'),
    (r'^campaign/(?P<slug>[\w-]+)/edit/$','campaign_edit'),
    (r'^campaign/(?P<slug>[\w-]+)/add_product/$','campaign_add_product'),
    (r'^campaign/(?P<slug>[\w-]+)/add_company/$','campaign_add_company'),
    (r'^campaign/(?P<slug>[\w-]+)/join/$','user_join_campaign'),
    (r'^campaign/(?P<slug>[\w-]+)/leave/$','user_leave_campaign'),
    (r'^store/$','store_view_all'),
    (r'^store/all\.json$','store_all_json'),
    #(r'^store/near/(?P<zip>[\d-]+)/json$','store_near_zip_json'),
    (r'^store/new/$','store_add'),
    (r'^store/(?P<slug>[\w-]+)/$','store_view'),
    (r'^store/(?P<slug>[\w-]+)/edit$','store_edit'),
)