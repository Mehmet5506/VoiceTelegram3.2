import os
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba ben  müzik botu👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Groups'un sesli sohbetlerinde müzik çalmak için oluşturulan Mehmet_Bey tarafından düzenlenen gelişmiş müzik botuyum.\n\n✅ Daha fazla bilgi için /help."
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
 Userbot katıldıysa müziğin tadını çıkarın, Eklenmezse @sesmusicasistan grubunuza ve yeniden deneyin.

**Kanal Müziği Çalma İçin**
1) Beni kanalınızın yöneticisi yap.
2) Gönder /bağlantılı grupta userbotjoinchannel.
3) Şimdi bağlantılı grupta komut gönder.

**Komut**

**=>> Şarkı Çalma 🎧**

- /oynat <şarkı ismi>: Aşağıda Verilen Klavyeyi Seçin.
- /oynat <yt url>: Verilen YouTube URL'sini oynatma.
- /serioynat: YouTube Music üzerinden doğrudan şarkı çalma.
- /dplay: Deezer ile şarkı çal.
- /splay: Jio saavn ile şarkı çal.

**=>> kayıttan yürütme ⏯**

- /panel: Oynatıcının Ayarlar menüsünü aç.
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

- /cplay <şarkı ismi>: İstediğiniz şarkıyı çal.
- /cdplay <şarkı ismi>: İstediğiniz şarkıyı deezer üzerinden çalın.
- /csplay <şarkı ismi>: jio saavn aracılığıyla istediğiniz şarkıyı çalın.
- /cplaylist: Şimdi yürüttt listesini göster.
- /cccurrent: Şimdi oynatılır göster.
- /cplayer: Müzik çalar ayarları panelini açma.
- /cpause: Şarkı çalmayı duraklat.
- /cresume: Şarkı çalmaya devam et.
- /cskip: Sonraki şarkıyı çal.
- /cend: Müzik çalmayı durdurma.
- /userbotjoinchannel: Asistanı sohbetinize davet etme.

**Kanal c yerine de kullanılabilir** ( /cplay = /channelplay )

**⭕ Bağlantılı grupta oynamayı sevmiyorsanız:**

1) Kanal kimliğinizi alın.
2) Küçük bir grup oluşturma: Kanal Müziği: your_channel_id
3) Tam perms ile Kanal yöneticisi olarak bot ekleme
4) Add @sesmusicasistan yönetici olarak kanala.
5) Grubunuza komut göndermeniz yeterlidir.
""",

f"""
**=>> Diğer araçlar 😬**

- /durum: <on/off> : Müzik Çaları Etkinleştir/Devre Dışı Bırak
- /reload: Grubunuzun yönetici bilgilerini güncelleştirin. Bot yöneticiyi tanımıyorsa deneyin
- /katil: Davet etmek için @sesmusicasistan Sohbetinize komutu gönderiniz. 
""",
f"""
**=>> Şarkı/Vid İndir:📥**
- /video [şarkı ismi]: Youtube'dan video şarkı indirin
- /bul [şarkı ismi]: Youtube'dan ses şarkısı indirin
- /saavn [şarkı ismi]: Saavn'den şarkı indir
- /deezer [şarkı ismi]: Deezer'dan şarkı indirin

**=>> Arama Araçları 🔍**
- /link [şarkı ismi]: Youtube'da şarkı ara
- /lyrics [şarkı ismi]: Şarkı sözlerini al
""",

f"""
**=>> Sudo Kullanıcıları için Komutlar 👮**
 - /userbotleaveall - yardımcıyı tüm sohbetlerden kaldırma
 - /broadcast <reply to message> - tüm sohbetlere genel olarak yayınlanan yanıtlanmış mesaj
 - /pmpermit [on/off] - pmpermit iletisini etkinleştirme/devre dışı bırakma
**Sudo Kullanıcıları herhangi bir gruptaki herhangi bir komutu yürütebilir.**
"""
      ]
