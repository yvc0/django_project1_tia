from django.http import HttpResponse

def show_output(request):
    # Simple Python logic: add two numbers
    a = 10
    b = 5
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is {result}")
