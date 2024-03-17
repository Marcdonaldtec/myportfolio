
from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def donation_form(request):
    return render(request, 'donation/donation_form.html')

from stripe.error import CardError

def charge(request):
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Donation',
                source=token,
            )
            # Handle successful payment
            return render(request, 'donation/success.html')
        except CardError as e:
            # Display error message to the user
            error_message = str(e)
            return render(request, 'donation/error.html', {'error_message': error_message})


