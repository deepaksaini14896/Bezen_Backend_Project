from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from utils import resize_photo
from rq import Queue
from redis import Redis

# Tell RQ what Redis connection to use
redis_conn = Redis()
# No args implies the default queue
q = Queue(connection=redis_conn)

# Create your views here.
class RecordAPI(ViewSet):
    # Add record
    def create(self, request):
        serializers = RecordSerializer(data=request.data)

        if serializers.is_valid():
            q.enqueue(resize_photo, request.data['image'].name)
            serializers.save()
            return Response({"Message":"Record Added"})

        return Response(serializers.errors)

    # Show all record
    def list(self, request):
    	record = Record.objects.all().order_by('-timestamp')[::-1]
    	serializers = RecordSerializer(record, context={"request":request}, many=True)

    	return Response(serializers.data)