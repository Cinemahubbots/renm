import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

log_channel = int(os.environ.get("LOG_CHANNEL", ""))

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

app = Client("test", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if len(msg.command) < 2 or not reply:
       return await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")
    media = reply.document or reply.audio or reply.video
    if not media:
       await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")
    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1]
    sts = await msg.reply_text("Trying to Downloading.....")
    c_time = time.time()
    downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("Download Started.....", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
            return
    else:
        cap = f"{new_name}\n\n💽 size : {filesize}"
    raw_thumbnail = temp.THUMBNAIL 
    if raw_thumbnail:
        og_thumbnail = await bot.download_media(raw_thumbnail)
    else:
        og_thumbnail = await bot.download_media(og_media.thumbs[0].file_id)
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))        
    except Exception as e:  
        await sts.edit(f"Error {e}") 
        return               
    try:
        os.remove(downloaded)
        os.remove(og_thumbnail)
    except:
        pass
    #await sts.delete()
     
    value = 2090000000
    if value < file.file_size:
        await sts.edit("```Trying To Upload```")
        try:
            filw = await app.send_document(log_channel,document = file_path,thumb=ph_path,caption = caption,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
            from_chat = filw.chat.id
            mg_id = filw.id
            time.sleep(2)
            await bot.copy_message(msg.from_user.id,from_chat,mg_id)
            await sts.delete()
            os.remove(file_path)
            try:
                os.remove(ph_path)
            except:
                pass
        except Exception as e:
            await sts.edit(e)
            os.remove(file_path)
            try:
                os.remove(ph_path)
            except:
                return
    else:
    		await sts.edit("```Trying To Upload```")
    		c_time = time.time()
     		try:
     			await bot.send_document(msg.from_user.id,document = file_path,thumb=ph_path,caption = caption,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))			
     			await sts.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await sts.edit(e)
     			os.remove(file_path)
     			return 
     			     	
