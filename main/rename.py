import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    media = await c.get_messages(m.chat.id,m.reply_to_message.message_id)
    og_media = getattr(reply, media.value)
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
    await sts.delete()
