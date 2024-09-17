from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.decorators import login_required

@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST['content']
        Tweet.objects.create(user=request.user, content=content)
        return redirect('tweet_list')
    return render(request, 'tweets/create_tweet.html')
