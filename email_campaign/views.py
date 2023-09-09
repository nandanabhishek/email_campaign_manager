import datetime
from django.shortcuts import render, redirect

# Create your views here. 
from .models import Subscriber, Campaign

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        subscriber = Subscriber(email=email, first_name=first_name)
        subscriber.save()
        return redirect('subscriber_list')  # Redirect to subscriber list view
    return render(request, 'add_subscriber.html')

def add_campaign(request):
    if request.method == 'POST':
        # Handle campaign creation here
        # Ensure proper validation and saving of Campaign objects
        pass
    return render(request, 'add_campaign.html')

def subscriber_list(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'subscriber_list.html', {'subscribers': subscribers})

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
send_daily_campaign_parallel()

