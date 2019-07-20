import getmac
from django.views import View
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from blog_app.models import Post, Item, Vote


# Create your views here.
def index(request):
    template = 'blog_app/index.html'
    title = 'Blog | Chocolat'
    posts = Post.objects.all().order_by("-create_date")
    paginator = Paginator(posts, 3)  # Show 3 post per page

    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    context = {
        'posts': total_article,
        'title': title
    }
    return render(request, template, context)


def single(request, post_slug):
    template = 'blog_app/single.html'
    single_post = Post.objects.get(slug=post_slug)
    item = Item.objects.filter(post_id=single_post.id).annotate(total=Count('vote')).order_by('-total')

    # dictonary for store item -> vote count
    total_vote = {}

    for i in item:
        cnt = Vote.objects.filter(post_id=single_post.id, item_id=i.id).count()
        total_vote[i.id] = cnt

    # print(total_vote)

    mac_id = getmac.get_mac_address()
    is_vote = False
    if Vote.objects.filter(post_id=single_post.id, voted_by=request.user.id) or Vote.objects.filter(post_id=single_post.id, mac_address=mac_id) :
        is_vote = True
    else:
        is_vote = False

    context = {
        'post': single_post,
        'items': item,
        'is_vote': is_vote,
        'total_vote': total_vote
    }
    return render(request, template, context)


def vote_post(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id', '')
        item_id = request.POST.get('item_id', '')

        post = Post.objects.get(id=post_id)
        item = Item.objects.get(id=item_id)
        mac_id = getmac.get_mac_address()

        if not Vote.objects.filter(post_id=post_id, voted_by=request.user.id) and not Vote.objects.filter(post_id=post_id, mac_address=mac_id):
            ob_vote = Vote(
                post_id=post.id,
                item_id=item.id,
                voted_by=request.user.id,
                mac_address=mac_id
            )
            ob_vote.save()

    return redirect('blog_app:single', post.slug)


def add_new_item(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id', '')
        item_name = request.POST.get('item_name', '')
        short_desc = request.POST.get('short_desc', '')
        mac_id = getmac.get_mac_address()

        post = Post.objects.get(id=post_id)

        ob_item = Item(
            post_id=post_id,
            item_title=item_name,
            short_desc=short_desc,
            is_approved=False,
            create_by=request.user,
            mac_address=mac_id
        )
        ob_item.save()

    return redirect('blog_app:single', post.slug)


class CreateUpdateItem(View):
    template = 'blog_app/update_item.html'
    title = 'Update Item | Chocolat'

    def get(self, request, item_id=None):
        if item_id:
            item_id = int(item_id)
            try:
                item = Item.objects.get(Q(id=item_id) & Q(create_by=request.user)& Q(is_approved=False))
            except:
                item = None
                return HttpResponse("404 Error!")

            return render(request, self.template, context={'title': self.title, 'item': item})

        else:
            return render(request, self.template, context={'title': self.title})

    def post(self, request, item_id=None):
        post_id = request.POST.get('post_id', '')
        item_title = request.POST.get('item_name', '')
        short_desc = request.POST.get('short_desc', '')
        mac_id = getmac.get_mac_address()

        if item_id:
            item_id = int(item_id)
            item = Item.objects.get(id=item_id)
            item.item_title = item_title
            item.short_desc = short_desc
            item.mac_address = mac_id

            item.save()

        return redirect('users_app:dashboard')

@login_required
def delete_item(request, item_id=None):
    item = Item.objects.get(Q(id=item_id) & Q(create_by=request.user)& Q(is_approved=False))
    item.delete()

    return redirect('users_app:dashboard')


def contact(request):
    template = 'blog_app/contact.html'
    title = 'Contact | Chocolat'
    context = {'title': title}
    return render(request, template, context)
