import channels
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justchat.settings")
channel_layer = channels.asgi.get_channel_layer()
