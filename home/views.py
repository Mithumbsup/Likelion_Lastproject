from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Order
from django.utils import timezone
from .forms import PostForm, CommentForm
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

potato_price = {'a-5' : 5000, 'a-10' : 9000, 'a-20' : 16000, 'b-5' : 4000, 'b-10' : 7500, 'b-20' : 14000, 'c-5' : 2500, 'c-10' : 4500, 'c-20' : 8000}
del_price = {'a-5' : 3000, 'a-10' : 4000, 'a-20' : 5000, 'b-5' : 3000, 'b-10' : 4000, 'b-20' : 5000, 'c-5' : 3000, 'c-10' : 4000, 'c-20' : 5000}

# Create your views here.
def home(request):
    posts = Post.objects.all
    return render(request, 'home/home.html', {'posts':posts})

@login_required
def detail (request, post_id):
    post_detail = get_object_or_404 (Post, pk = post_id)
    form = CommentForm()
    return render(request, 'home/detail.html',{'post': post_detail, 'form':form})

def mypage(request):
    post = get_object_or_404(Post)
    # categories = Category.objects.all()
    return render(request, 'home/mypage.html',{'post' : mypage})

def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id = post.pk)
    else:
        form = PostForm()
    
    return render (request, 'home/post_new.html', {'form':form})
    

def order_save(request):
    order = Order()
    # order.writer = user_name
    order.product = request.GET['product']
    order.orderer = request.GET['orderer']
    order.postcode = request.GET['postcode']
    order.address = request.GET['address']
    order.phone1 = request.GET['phone1']
    order.phone2 = request.GET['phone2']
    order.email = request.GET['email']
    order.message = request.GET['message']
    order.created_date = timezone.datetime.now()
    order.price = potato_price['order.product']
    order.delivery_price = del_price['order.product']
    order.total_price = order.price + order.delivery_price
    order.save()
    return redirect('order_detail', order_id=order.pk)

def post_order(request):
    return render(request, 'home/post_order.html',)
# def post_order(request):
#     if request.method=="POST":
#         form=PostForm(request.POST)
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.save()
#             return redirect('detail',post_id=post.pk)
#     else:
#         form=PostForm()
#     return render(request,'home/post_order.html',{'form':form})

def order_list(request, post_id):
    categories = Category.objects.all()
    user = User.objects.get(pk=post_id)
    orders = Order.objects.filter(user=user)
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {'user': user, 'orders': orders, 'categories': categories}
    return render(request, 'home/order_list.html', context)

def post_edit(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'home/post_edit.html',{'form':form})

def post_delete(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect('home')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
    return redirect('detail', post_id=post.pk)

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    return redirect('detail', post_id=post.id)

def order_save(request):
    order = Order()
    # order.writer = user_name
    order.product = request.GET['product']
    order.orderer = request.GET['orderer']
    order.postcode = request.GET['postcode']
    order.address = request.GET['address']
    order.phone1 = request.GET['phone1']
    order.phone2 = request.GET['phone2']
    order.email = request.GET['email']
    order.message = request.GET['message']
    order.created_date = timezone.datetime.now()
    order.price = potato_price['order.product']
    order.delivery_price = del_price['order.product']
    order.total_price = order.price + order.delivery_price
    order.save()
    return redirect('order_detail', order_id=order.pk)
