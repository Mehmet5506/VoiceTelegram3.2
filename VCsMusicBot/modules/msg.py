import os
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba ben  müzik botu👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Groups'un sesli sohbetlerinde müzik çalmak için oluşturulan Mehmet_Bey tarafından düzenlenen müzik gelişmiş botuyum.\n\n✅ Daha fazla bilgi için/help."
      HELP_MSG = [
        ".",
f"""
**Merhaba ben Mehmet_Bey müzik botu, Hoşgeldiniz Abelia_Musicbot

⭕ Grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilirim.

⭕ Assistant: @Sesmusicasistan\n\nİleri'yi tıklatın ➡️ yönergeler için.**
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

- /cplay <song name>: İstediğiniz şarkıyı çal.
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

**Kanal c yerine de kullanılabilir** ( /cplay = /channelplay )

**⭕ Bağlantılı grupta oynamayı sevmiyorsanız:**

1) Kanal kimliğinizi alın.
2) Küçük bir grup oluşturma: Kanal Müziği: your_channel_id
3) Tam perms ile Kanal yöneticisi olarak bot ekleme
4) Add @{sesmusicasistan} yönetici olarak kanala.
5) Grubunuza komut göndermeniz yeterlidir.
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

**=>> Arama Araçları 🔍**
- /link [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Sudo Kullanıcıları için Komutlar 👮**
 - /userbotleaveall - yardımcıyı tüm sohbetlerden kaldırma
 - /broadcast <reply to message> - tüm sohbetlere genel olarak yayınlanan yanıtlanmış mesaj
 - /pmpermit [on/off] - pmpermit iletisini etkinleştirme/devre dışı bırakma
**Sudo Kullanıcıları herhangi bir gruptaki herhangi bir komutu yürütebilir.**
"""
      ]
