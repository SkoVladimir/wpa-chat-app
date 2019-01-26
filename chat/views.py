from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    flag = 0
    all_contacts = Contact.objects.all()
    for contact in all_contacts:
        if contact.user == user:
            flag = 1
            break
    if flag == 0:
        new_contact = Contact.objects.create(user=user)
    # print(all_contacts)
    # new_contact = Contact.objects.create(user=user)
    # if new_contact not in all_contacts:
    #     new_contact.save()
    # print(all_contacts)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)
