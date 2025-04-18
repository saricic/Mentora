from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings




def mainpage(request):
    template = loader.get_template('main.html')
    print(f"User authenticated: {request.user.is_authenticated}")
    return render(request, 'main.html')
def learnPage(request):
    return render(request, 'learn.html')

@login_required
def chatButton(request):
    return render(request, 'chat.html')

def loginbutton(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pass
    return render(request, 'login.html', {'form': form})


@csrf_exempt
def gemini_proxy(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request
            body = json.loads(request.body)
            user_message = body.get('message', '')

            # Make the API request to Gemini
            api_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
            api_key = settings.GEMINI_KEY

            if not api_key:
                return JsonResponse({'error': 'API key is missing'}, status=500)

            # Correct Gemini API request format
            response = requests.post(
                f'{api_url}?key={api_key}',
                json={
                    "contents": [{
                        "parts": [{
                            "text": user_message
                        }]
                    }],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                        "topP": 0.8
                    }
                },
                headers={'Content-Type': 'application/json'}
            )

            # Debugging logs
            print("API response status:", response.status_code)
            print("API response body:", response.text)

            # Check if the API request was successful
            if response.status_code != 200:
                return JsonResponse({
                    'error': f'API request failed with status {response.status_code}',
                    'details': response.text
                }, status=500)

            # Parse the Gemini response correctly
            response_data = response.json()
            if 'candidates' in response_data and len(response_data['candidates']) > 0:
                bot_response = response_data['candidates'][0]['content']['parts'][0]['text']
                return JsonResponse({'response': bot_response})
            else:
                return JsonResponse({'error': 'No valid response from Gemini'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)