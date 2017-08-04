# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# APIView inherit by the view
from rest_framework.views import APIView
# import the model (table)
from .models import GenericUser
# import the serializer to convert the data into the json
from .serializer import UserListSerializler
# to respond to the user query
from rest_framework.response import Response


# create the view
class UserListView(APIView):
    # function for get method by the user to API
    def get(self, request):
        # select all from the GenericUser table
        user_list = GenericUser.objects.all()
        # call to serializer to convert the data into json form which is returned by the database
        # many = True for selecting all the data
        serialized_data =  UserListSerializler(instance=user_list, many=True).data
        # return the data to the user in json format as response
        return Response(serialized_data)

class UserCreateView(APIView):
    # function to perform the post operation throug api
    def post(self,request):
        post_data = request.data
        user_name = post_data['user_name']
        email = post_data['email']
        mobile_number = post_data['mobile_number']
        user = GenericUser(user_name = user_name, email = email, mobile_number = mobile_number)
        try:
            user.save()
        except Exception as e:
            return Response({
                'message': 'Post was not saved successfully'
            })

        return Response({
            'message': "Post Saved Successfully"
        })