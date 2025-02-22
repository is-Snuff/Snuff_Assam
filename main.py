import os
import requests
import base64
import marshal
import random
import zlib
import telebot
import py_compile
from telebot import *
from telebot import util
from telebot import types

B = '\033[2;36m'
sa = '7062693066:AAGeDn0laYAqNrdkVsdB5Z0X-i_k1TVG1p4'
bot = telebot.TeleBot(sa)
#-----------------------[protcol]----------------------#
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'module','exec'))
#cpython = lambda in_ : marshal.simple.cptencode(in_)[hahah.not work]
#-----------------------[START]----------------------#
@bot.message_handler(commands=['start'])
def START(message):            
    s1 = types.InlineKeyboardButton(text="marshal ", callback_data='marshal')
    s2 = types.InlineKeyboardButton(text="base64 ", callback_data='base64')
    s3 = types.InlineKeyboardButton(text="lambda ", callback_data='lambda')
    s4 = types.InlineKeyboardButton(text="zlib ", callback_data='zlib2')
    s5 = types.InlineKeyboardButton(text="marshal_zlib", callback_data='marshal_zlib')    
    s6 = types.InlineKeyboardButton(text="zlib_base16", callback_data='zlib_base16')
    s7 = types.InlineKeyboardButton(text="zlib_base32", callback_data='base32_zlib')
    s8  = types.InlineKeyboardButton(text="marshall_zlib_base16", callback_data='marshall_zlib_base16')
    s9 = types.InlineKeyboardButton(text="marshall_zlib_base64", callback_data='marshall_zlib_base64')    
    pro = types.InlineKeyboardButton(text="The Programmer ", url=f"https://t.me/xYourKing")     
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(s1, s2, s3, s4,s5,s6,s7,s8,s9,pro)
    bot.send_message(message.chat.id, text=f"Choose An Option", parse_mode="markdown", reply_markup=Keyy)
#-----------------------[encode]----------------------#    
@bot.callback_query_handler(func=lambda call: True)
def encode3(call):
    if call.data== "encode":
        enc(call.message)
    elif call.data== "base64":
        encode2(call.message, "base64")
    elif call.data == "lambda":
        encode2(call.message, "lambda")
    elif call.data == "marshal":
        encode2(call.message, "marshal")
    elif call.data == "zlib":
        encode2(call.message, "zlib2")
    elif call.data == "zlib_base16":
        encode2(call.message, "zlib_base16")
    elif call.data == "marshal_zlib":
        encode2(call.message, "marshal_zlib")
    elif call.data == "base32_zlib":
        encode2(call.message, "base32_zlib")
    elif call.data == "marshall_zlib_base16":
        encode2(call.message, "marshall_zlib_base16")
    elif call.data == "marshall_zlib_base64":
        encode2(call.message, "marshall_zlib_base64")
    
       
#-----------------------[ SEND FILE ]----------------------#
def encode2(message,call):
    bot.send_message(message.chat.id, text=f" send File [{call}]")
    @bot.message_handler(content_types=['document'])
    def save(message):
        file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
        us=str("".join(random.choice('1234567890')for i in range(4)))
        file_name = f"{call}-{us}.py"
        with open(file_name, 'wb') as f:
            f.write(file_input)
        s3 = encode(call, file_name)
        with open(file_name, 'w') as f:
            f.write(s3)
        file_document = open(file_name, 'rb')
        bot.send_document(message.chat.id, file_document)
        os.system(f"rm -f {file_name}")
#-----------------------[code]----------------------#        
def encode(call, file_name):
#-----------------------[base64]----------------------#        
    if call == "base64":
        s3 = b64(open(file_name, "r").read().encode('utf8'))[::-1]
        return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)({s3}))")
#-----------------------[lambda]----------------------#        
    elif call == "lambda":
        s3  = repr(zlib.compress(open(file_name, "r").read().encode('utf-8')))        
        return (f"#Encoded By : @xYourKing\n\nimport zlib\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'module','exec'))({s3},compile))")
#-----------------------[Marshal]----------------------#                
    elif call == "marshal":
        s3= marshal.dumps(compile(open(file_name, "r").read(), 'module', 'exec'))
        return (f"#Encoded By : @xYourKing\n\nimport marshal\nexec(marshal.loads({s3}))")
#-----------------------[Zlib]----------------------#                
    elif call == "zlib2":
        s3 = str(base64.b64encode(zlib.compress(marshal.dumps(compile(open(file_name, "r").read(), "ru", 'exec')))))
        return (f"#Encoded By : @xYourKing\n\nimport base64\nimport zlib\nimport marshal\nexec(marshal.loads(zlib.decompress(base64.b64decode({s3}))))")
#-----------------------[Zlib_Base16]----------------------#                
    elif call =="zlib_base16":
    	s3 = b16(zlb(open(file_name, "r").read().encode('utf8')))[::-1]
    	return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)({s3}))")
#-----------------------[Base32_Zlib]]----------------------#            	
    elif call =="base32_zlib":
    	s3 = b32(zlb(open(file_name, "r").read().encode('utf8')))[::-1]
    	return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)({s3}))")
#-----------------------[Marshall_Zlib_Base16]----------------------#            	
    elif call == "marshall_zlib_base16":
    	s3 = b16(zlb(mar(open(file_name, "r").read().encode('utf8'))))[::-1]
    	return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));exec((_)({s3}))")
#-----------------------[Marshall_Zlib_Base64]----------------------#            	
    elif call =="marshall_zlib_base64":    	    	 
    	    	 s3 = b64(zlb(mar(open(file_name, "r").read().encode('utf8'))))[::-1]
    	    	 return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)({s3}))")
#-----------------------[Marshal_Zlib]----------------------#            	    	 
    elif call =="marshal_zlib":
    	    	s3 = zlb(mar(open(file_name, "r").read().encode('utf8')))[::-1]
    	    	return (f"#Encoded By : @xYourKing\n\n_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)({s3}))\n\n#Encoded By : @xYourKing")
#-----------------------[Cpython]----------------------#            	    	
    	    	
    
    	    	    	    	    	    	
    	    	
#programmer of bot @xYourKing
#NAME : SAJAD
#TOP ONE 1
# oh 120

bot.polling(True)

