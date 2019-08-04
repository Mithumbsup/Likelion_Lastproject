from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Order
from django.utils import timezone
from .forms import PostForm, CommentForm
from .forms import OrderForm

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home/home.html', {'posts':posts})

def mypage(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    # categories = Category.objects.all()
    return render(request, 'home/mypage.html',{'post' : mypage})

def post_order(request,post_id):
    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(pk=post_id)
    user = request.user
    categories = Category.objects.all()
    initial = {'name': product.name, 'amount': product.price, 'quantity': quantity}
    # cart = Cart.objects.filter(user=user)
    if request.method == 'POST':
            form = OrderForm(request.POST, initial=initial)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = user
                order.quantity = quantity
                order.products = product
                order.save()
                return redirect('home/order_list.html', user.pk)

            else:
                form = OrderForm(initial=initial)

            return render(request, 'home/post_order.html', {
                'form': form,
                'quantity': quantity,
                'user': user,
                'product': product,
                'categories': categories,
            })
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