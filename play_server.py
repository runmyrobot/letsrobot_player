
import subprocess

from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
    print('connected')

def on_disconnect():
    print('disconnected')

def on_reconnect():
    print('reconnected')

    
def on_chat_message(*args):

    try:
        fullMessage = args[0]['message']
    except:
        print "chat message is in valid"
        return

    try:
        fullMessage.decode('utf-8')
        print "message string is UTF-8"
    except UnicodeError:
        print "message string is not UTF-8"
        return

    if len(fullMessage.split("] ")) > 1:
    
        rawMessage = fullMessage.split("] ")[1]
        
        message = rawMessage
        
        splitMessage = rawMessage.split(" ")
        if len(splitMessage) == 2:
            if splitMessage[0] == "!play":
                print "!play"
                message = splitMessage[1]
                print "message:", message

        # allow this temporarily
        #if len(splitMessage) == 1:
        #    message = splitMessage[0]

        if len(splitMessage) != 2:
            return

        if message[0:11] == "youtube.com" or message[0:14] == "www.youtube.com" or message[0:23] == "https://www.youtube.com" or message[0:16] == "https://youtu.be":
                url = message
                print "url", url
                subprocess.call(["Taskkill", "/IM", "firefox.exe", "/F"])
                subprocess.Popen(["C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", url])
            
        print 'received chat', fullMessage


socketIO = SocketIO('https://runmyrobot.com', 8000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('chat_message_with_name', on_chat_message)
#socketIO.emit('aaa')
#socketIO.emit('aaa')
socketIO.wait(seconds=1)

# Stop listening
#socketIO.off('play_youtube')
socketIO.emit('aaa')
socketIO.wait(seconds=1)

# Listen only once
#socketIO.once('play_youtube', on_play_youtube)
socketIO.emit('aaa')  # Activate play_youtube
socketIO.emit('aaa')  # Ignore
socketIO.wait(seconds=1)





socketIO.wait()




