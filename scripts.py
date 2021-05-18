class Scripted(object):    


    PROGRESS_DIS = """\n
<b>📥ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ ꜱᴇʀᴠᴇʀ : {1} | {2}</b>\n
<b>⛓️ᴘᴇʀᴄᴇɴᴛᴀɢᴇ : {0}%</b>\n
<b>🚀ꜱᴘᴇᴇᴅ: : {3}/s</b>\n
<b>🕰️ᴇꜱᴛɪᴍᴀᴛᴇᴅ ᴛɪᴍᴇ: {4}</b>\n"""


    HELP_TEXT = """
<b> ꜱᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀꜱ ᴛʜᴜᴍʙɴᴀɪʟ (ᴏᴘᴛɪᴏɴᴀʟ)</b>\n
<b> ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ</b>\n
<b> ᴄᴏɴᴠᴇʀᴛ ꜰɪʟᴇꜱ ɪɴᴛᴏ ᴠɪᴅᴇᴏ ᴜꜱᴇ  /convert ᴄᴏᴍᴍᴀɴᴅ</b>\n
<b> ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ /rename ɴᴇᴡ ɴᴀᴍᴇ.ᴇxᴛ</b>\n
<b> ᴠɪᴇᴡ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴏ /sthumbnail ᴄᴏᴍᴍᴀɴᴅ</b>\n
<b> ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴏ /dthumbnail ᴄᴏᴍᴍᴀɴᴅ</b> """

    ABOUT_TEXT = """
<b>My Name : <a href='https://t.me/Jns_renamerpro_bot'>JNS RENAMER PRO</a></b>\n
<b>Channel : <a href='https://t.me/jns_bots'>ＪƝ⟆ ᗷ〇Ƭ⟆</a></b>\n
<b>Version : <a href='https://t.me/Jns_renamerpro_bot'>beta v1.01</a></b>\n
<b>Server : <a href='https://heroku.com'>Heroku</a></b>\n
<b>Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>Language : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>Developer : <a href='https://t.me/jintons'>JINTO NS</a></b>\n
<b>Powered By : <a href='https://t.me/jns_fc_bots'>SUPPORT GROUP</a></b>\n"""



    RENAMED_SUCCESS = "<b>ꜰɪʟᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🎊🎉</b>"
    RENAMING_VIDEO = "<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ... 📥</b>"
    CUSTOM_CAPTION = "<b>{}</b>"
    PROCESSING_TEXT = "<b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...⏳</b>"
    ACCESS_DENIED = "<b>¥ou Are Banned 🚫</b>"
    BANNED_USER_TEXT = "<b>¥ou Are Banned 🚫</b>"
    TRYING_TO_UPLOAD = "<b>ᴛʀʏɪɴɢ ᴛᴏ ᴜᴘʟᴏᴀᴅ....📤</b>"
    CURRENT_THUMBNAIL = "<b>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ🎭</b>"
    THUMBNAIL_SAVED = "<b>ʏᴏᴜʀ ɴᴇᴡ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ᴘᴇʀᴍᴇɴᴛʟʏ ꜰᴏʀ ᴀʟʟ ɴᴇxᴛ ᴜᴘʟᴏᴀᴅꜱ✅</b>"
    THUMBNAIL_DELETED = "<b>ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ! ꜰɪʟᴇ ᴜᴘʟᴏᴀᴅ ᴡɪᴛʜᴏᴜᴛ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏʀ ᴀʟʟ ɴᴇxᴛ ᴜᴘʟᴏᴀᴅꜱ , ꜱᴇɴᴅ ɴᴇᴡ ɪᴍᴀɢᴇ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ❗ ✅</b>"
    NO_THUMBNAIL_FOUND = "<b>ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏᴜɴᴅ🤷🧑🏻‍🦯 ꜱᴇɴᴅ ɪᴍᴀɢᴇ ꜰᴏʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>"
    TRYING_TO_DOWNLOAD = "<b>ᴛʀʏɪɴɢ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ....📥</b>"
    UPLOAD_SUCCESS = "<u><b>Tԋαɳƙ υ ϝσɾ υʂιɳɠ ɱҽ Sԋαɾҽ & Sυρρσɾƚ @JNS_BOTS 🥰</b></u>"
    REPLY_TO_VIDEO = "<b>ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ /convert</b>"
    UPLOAD_START = "<b>ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ꜰɪʟᴇ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...</b>\n"
    DOWNLOAD_START = "<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ꜰɪʟᴇ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...</b>\n"
    JOIN_NOW_TEXT = "<b>ʜᴇʏ ᴅᴜᴅᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ</b>"
    REPLY_TO_FILE = "<b>ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ <u>/ʀᴇɴᴀᴍᴇ ɴᴇᴡ ɴᴀᴍᴇ.ᴇxᴛ</u></b>"
    CONTACT_MY_DEVELOPER = "<b>Something Wrong Contact Our Support Group @jns_fc_bots 🤯</b>"
    REPLY_TO_MEDIA = "<b>ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ꜰɪʟᴇ ᴡɪᴛʜ <u>/rename_video ɴᴇᴡ ɴᴀᴍe</u></b>"
    START_TEXT = "<b>Hy..{}  🙋🏻‍♀️</b>\n\n<b>ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇʀ+ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴜᴘᴘᴏʀᴛ!💯
</b>\n\n<b>🤖PowerdeD By : <a href='https://t.me/jns_bots'>ＪƝ⟆ ᗷ〇Ƭ⟆</a></b>\n\n<b>👤Developer : <a href='https://t.me/jintons>JINTO NS </a></b>"
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/JINTONS'>[ Click Here ]</a></b>"
