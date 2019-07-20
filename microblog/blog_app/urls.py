from django.urls import path
from blog_app.views import index, single, vote_post, add_new_item, CreateUpdateItem, delete_item, contact

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:post_slug>/', single, name='single'),
    path('vote/', vote_post, name='vote_post'),
    path('new_item/', add_new_item, name='new_item'),
    path('update_item/<int:item_id>', CreateUpdateItem.as_view(), name='update_item'),
    path('delete_item/<int:item_id>', delete_item, name='delete_item'),
    path('contact/', contact, name='contact'),
]


