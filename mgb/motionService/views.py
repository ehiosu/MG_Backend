from django.shortcuts import render
import  os
import  socketio
# Create your views here.

basedir=os.path.dirname(os.path.realpath(__file__))
sio=socketio.Server(async_mode='eventlet')
