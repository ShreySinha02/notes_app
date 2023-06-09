from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import noteSerilizer
from .models import Note
@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view()
def getNotes(request):
    data=Note.objects.all()
    serializer=noteSerilizer(data,many=True)
    return Response(serializer.data)
@api_view()
def getNote(request,pk):
    data=Note.objects.get(id=pk)
    serializer=noteSerilizer(data)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = noteSerilizer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = noteSerilizer(note, many=False)
    return Response(serializer.data)