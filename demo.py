from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import json
#from os import open

class Comment:
    def __init__(self, email, content, created=None):
        self.email1 = email
        self.content = content
        self.created = created or datetime.now()
        self.authors = None

comment = Comment(email='a@b.pl', content='foo bar')

Comment(email='aaa', content='kdalkdjaslkd')

class CommentSerializer(serializers.Serializer):
    email1 = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()



class TestSerializer(serializers.Serializer):
    title = serializers.CharField(source='volumeInfo.title')
    authors = serializers.ListField(source='volumeInfo.authors')
    published_date = serializers.DateField(source='volumeInfo.publishedDate', required=False)
    categories = serializers.ListField(source='volumeInfo.categories', required=False)
    thumbnail = serializers.CharField(source='volumeInfo.imageLinks.thumbnail', required=False)
    

serializer = CommentSerializer(comment)

print(serializer.data)

print(comment)

json_out = JSONRenderer().render(serializer.data)
print(json_out)
#print(comment.email)

with open('test_input.json', 'r') as file:
    json_file_content = json.load(file)

type(json_file_content)

book_list = json_file_content['items']

serialized_json = TestSerializer(book_list, many=True)

print(serialized_json.data)

json_output = JSONRenderer().render(serialized_json.data)
print(json_output)