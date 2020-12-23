from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Author, Book

class AuthorSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
	    model = Author
	    fields = '__all__'

class BookSerializers(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner,username')

	class Meta:
	    model = Book
	    fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
	book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

	class Meta:
		model = User
		fields = ['id','username','author','book']