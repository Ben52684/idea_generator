
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Chat, HackathonIdea
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from .serializers import HackathonIdeaSerializer

import os
import re


openai_api_key = settings.OPENAI_API_KEY
client = OpenAI(api_key=openai_api_key)


def index(request):
    return render(request, 'index.html')


def parse_hackathon_ideas(response):
    ideas = []
    # Regular expression to 
    regex = r"\d+\.\s*Name:\s*(.*?)\s*Short Description:\s*(.*?)\s*Suggested build approach:\s*(.*?)(?=\d+\.\s*|$)"
    
    # Find all matches using the regular expression
    matches = re.findall(regex, response, re.DOTALL)
    
    for match in matches:
        name, description, build_approach = match
        ideas.append({
            'name': name.strip(),
            'description': description.strip(),
            'build_approach': build_approach.strip(),
        })
    
    return ideas

def save_hackathon_ideas(response):
    parsed_ideas = parse_hackathon_ideas(response)
    
    for idea in parsed_ideas:
        # Create a new HackathonIdea instance and save it to the database
        hackathon_idea = HackathonIdea(
            name=idea['name'],
            description=idea['description'],
            build_approach=idea['build_approach']
        )
        hackathon_idea.save()  # Save to the database
        print(f"Saved: {hackathon_idea.name}")

@api_view(['POST'])
def chat_response(request):
    """
    API endpoint to handle chat messages and return responses.
    """
    print(f"Received request data: {request.data}")  # Log the incoming data

    try:
        message = request.data.get('message', '')  # Get the message from the request body
        if not message:
            return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

        # OpenAI API call
        completion = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistant that generates hackathon project ideas, ask the user to describe any details about the hackathon [theme, technologies, participant skill levels, etc]. Once they have answered all questions, respond first with a title >Hackathon Ideas< and then followed by providing three hackathon options which each include a Name, a Short Description and a suggested build approach."},
                {"role": "user", "content": message},
            ]
        )

        # print(f"OpenAI response: {completion}")

        answer = completion.choices[0].message.content

        print(f'{answer}')

        # Check if the response contains '>Hackathon Ideas<' before parsing and saving
        if "Hackathon Ideas" in answer:
           save_hackathon_ideas(answer)
        # Save the chat message and response to the database
        new_chat = Chat(message=message, response=answer)
        new_chat.save()

        return Response({'response': answer}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class HackathonIdeaList(APIView):
    def get(self, request):
        # Fetch all hackathon ideas from the database
        ideas = HackathonIdea.objects.all()  # This will query all the HackathonIdea objects in the database
        
        # Serialize the ideas
        serializer = HackathonIdeaSerializer(ideas, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)