from django.shortcuts import render
import stripe
import uuid

stripe.api_key = "sk_test_your_secret_key"


def home(request):
    return render(request, "home.html")


def pay(request):

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        amount = request.POST["amount"]

        order_id = str(uuid.uuid4())

        message = f"""
        IPL Ticket Booking

        Name : {name}

        Email : {email}

        Amount : ₹{amount}

        Order ID : {order_id}

        Redirect to Paytm Sandbox
        """

        return render(request, "result.html", {"message": message})

    return render(request, "pay.html")


def payment_callback(request):

    status = request.POST.get("STATUS")

    if status == "TXN_SUCCESS":

        message = "Payment Successful"

    else:

        message = "Payment Failed"

    return render(request, "result.html", {"message": message})


def food(request):

    if request.method == "POST":

        dish = request.POST["dish"]

        price = request.POST["price"]

        message = f"Stripe Payment Successful\n\nDish : {dish}\nPrice : ₹{price}"

        return render(request, "result.html", {"message": message})

    return render(request, "food.html")


def paypal(request):

    if request.method == "POST":

        name = request.POST["name"]

        amount = request.POST["amount"]

        message = f"PayPal Sandbox Payment Successful\n\n{name}\n₹{amount}"

        return render(request, "result.html", {"message": message})

    return render(request, "paypal.html")