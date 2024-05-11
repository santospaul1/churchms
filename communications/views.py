# In communication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from .forms import MessageForm

#@login_required
def conversation_list(request):
    conversations = request.user.conversations.all()
    return render(request, 'communication/conversation_list.html', {'conversations': conversations})

#@login_required
def conversation_detail(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    messages = conversation.messages.all()
    return render(request, 'communication/conversation_detail.html', {'conversation': conversation, 'messages': messages})

#@login_required
def send_message(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.conversation = conversation
            message.save()
            return redirect('conversation_detail', conversation_id=conversation_id)
    else:
        form = MessageForm()
    return render(request, 'communication/send_message.html', {'form': form})
