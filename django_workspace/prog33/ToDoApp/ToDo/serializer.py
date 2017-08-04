from rest_framework import serializers
# import the model
from .models import Todo

# create the serializer
# it will convert the data returned by the database into the json format
class TodoListSerializler(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # for exculding the field in format
        # exclude = ('created_on', )
        # for all the fields in the data
        fields = '__all__'
