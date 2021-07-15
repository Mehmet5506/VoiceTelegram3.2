import os
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba ben Mehmet_Bey müzik botu👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Groups'un sesli sohbetlerinde müzik çalmak için oluşturulan Mwhmet_Bey tarafından düzenlenen müzik gelişmiş botuyum.\n\n✅ Daha fazla bilgi için/help."
      HELP_MSG = [
        ".",
f"""
**Merhaba ben Mehmet_Bey müzik botu, Hoşgeldiniz {Abelia_Musicbot}

⭕ Grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilirim.

⭕ Assistant: @{Sesmusicasistan}\n\nİleri'yi tıklatın ➡️ yönergeler için.**
""",

f"""
**Ayarlama**

1) Bot yöneticisi yap (Cplay kullanıyorsanız grupla ve kanalda)
2) Sesli sohbet başlatma
3) Deneyin /oynat <şarkı ismi> ilk kez bir yönetici tarafından
 Userbot katıldıysa müziğin tadını çıkarın, Eklemezse @{sesmusicasistan} grubunuza ve yeniden deneyin.

**Kanal Müziği Çalma İçin**
1) Beni kanalınızın yöneticisi yap.
2) Gönder /bağlantılı grupta userbotjoinchannel.
3) Şimdi bağlantılı grupta komut gönder.

**Komut**

**=>> Şarkı Çalma 🎧**

- /oynat <şarkı ismi>: Aşağıda Verilen Klavyeyi Seçin.
- /oynat <yt url>: Verilen YouTube URL'sini oynatma.
- /ytplay: YouTube Music üzerinden doğrudan şarkı çalma.
- /dplay: Deezer ile şarkı çal.
- /splay: Jio saavn ile şarkı çal.

**=>> kayıttan yürütme ⏯**

- /player: Oynatıcının Ayarlar menüsünü aç.
- /atla: Geçerli parçayı atlar.
- /durdur: parçayı duraklat.
- /devam: Duraklatılmış parçayı devam ettiriyor.
- /kapat: Medya kayıttan yürütmeyi durdurur.
- /bilgi: Geçerli Çalma parçasını gösterir.
- /oynatlist: Çalma listesini gösterir.

**Player cmd ve diğer tüm cmd'ler /oynat, /geçerli ve /çalma listesi yalnızca grup yöneticileri içindir.**
""",
        
f"""
**=>> Kanal Müziği Çalma 👨‍🎤**

**⭕ Yalnızca bağlı grup yöneticileri için:**

- /cplay <song name>: Play song you requested.
- /cdplay <song name>: Play song you requested via deezer.
- /csplay <song name>: Play song you requested via jio saavn.
- /cplaylist: Show now playing list.
- /cccurrent: Show now playing.
- /cplayer: Open music player settings panel.
- /cpause: Pause song play.
- /cresume: Resume song play.
- /cskip: Play next song.
- /cend: Stop music play.
- /userbotjoinchannel: Invite assistant to your chat.

**Channel is also can be used instead of c** ( /cplay = /channelplay )

**⭕ If you donlt like to play in linked group:**

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> Diğer araçlar 😬**

- /musicplayer <on/off> : Müzik Çaları Etkinleştir/Devre Dışı Bırak
- /reload: Grubunuzun yönetici bilgilerini güncelleştirin. Bot yöneticiyi tanımıyorsa deneyin
- /userbotjoin: Invite @{sesmusicasistan} Sohbetinize userbot
""",
f"""
**=>> Şarkı/Vid İndir:📥**
- /video [song mame]: Download video song from youtube
- /bul [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 🔍**
- /link [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Commands for Sudo Users 👮**
 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
**Sudo Users can execute any command in any groups.**
"""
      ]
