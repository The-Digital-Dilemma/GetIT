from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', status=404)

def privacyPolicy(request):
    return render(request, 'privacy_policy.html')
