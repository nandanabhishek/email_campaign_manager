import datetime
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here. 
from .models import Subscriber, Campaign

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html', {'campaigns': campaigns})

def subscriber_list(request):
    subscribers = Subscriber.objects.filter(is_subscribed=True)
    return render(request, 'subscriber_list.html', {'subscribers': subscribers})

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        subscriber = Subscriber(email=email, first_name=first_name)
        subscriber.save()
        return redirect('subscriber_list')  # Redirect to subscriber list view
    return render(request, 'add_subscriber.html')

def unsubscribe(request, subscriber_id):
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    subscriber.is_subscribed = False
    subscriber.save()
    return redirect('subscriber_list')  # Redirect to the subscriber list view or another appropriate URL

def add_campaign(request):
    if request.method == 'POST':
        # Handle campaign creation here
        subject = request.POST.get('subject')
        preview_text = request.POST.get('preview_text')
        article_url = request.POST.get('article_url')
        html_content = request.POST.get('html_content')
        plain_text_content = request.POST.get('plain_text_content')
        published_date = request.POST.get('published_date')  # You may need to parse this date

        # Create and save the Campaign object
        campaign = Campaign(
            subject=subject,
            preview_text=preview_text,
            article_url=article_url,
            html_content=html_content,
            plain_text_content=plain_text_content,
            published_date=published_date,
        )
        campaign.save()

        # Redirect to a success page or wherever needed
        return redirect('campaign_list')  # Redirect to the campaign list view
        
    return render(request, 'add_campaign.html')

import concurrent.futures
from django.core.mail import send_mail
from .models import Campaign, Subscriber

def send_daily_campaign_parallel():
    campaigns = Campaign.objects.filter(published_date__date=datetime.date.today())

    def send_campaign(campaign):
        subject = campaign.subject
        message = campaign.plain_text_content
        from_email = 'imabhisheknandan00@gmail.com'
        recipient_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)

        send_mail(subject, message, from_email, recipient_list, html_message=campaign.html_content)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(send_campaign, campaigns)

# to test the working of send_daily_campaign_parallel()
# send_daily_campaign_parallel()

