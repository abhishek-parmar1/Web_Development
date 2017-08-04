# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# APIView inherit by the view
from rest_framework.views import APIView
# import the model (table)
from .models import Todo
# import the serializer to convert the data into the json
from .serializer import TodoListSerializler
# to respond to the user query
from rest_framework.response import Response

# Create your views here.
class TodoListView(APIView):

    # function for get method by the user to API
    def get(self, request):
        # select all from the GenericUser table
        todo_list = Todo.objects.all()
        # call to serializer to convert the data into json form which is returned by the database
        # many = True for selecting all the data
        serialized_data =  TodoListSerializler(instance=todo_list, many=True).data
        # return the data to the user in json format as response
        return Response(serialized_data)

class TodoCreateView(APIView):
    # function to create a view for post call on api
    def post(self,request):
        todo_data = request.data
        title = todo_data['title']
        description = todo_data['description']
        todo = Todo(title = title, description = description)
        try:
            todo.save()
        except Exception as e:
            return Response({
                'message': 'Post was not saved successfully'
            })

        return Response({
            'message': "Post Saved Successfully"
        })