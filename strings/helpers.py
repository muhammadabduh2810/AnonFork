HELP_1 = """🙄**<u>perintah admin:</u>**

cuma tambahkan **c** awal perintah untuk menggunakannya untuk saluran.

/pause : jeda streaming yang sedang diputar.
/resume : melanjutkan streaming yang sedang dijeda.
/mute : bisukan streaming yang sedang diputar.
/unmute : nyalakan lagi suara streaming.
/skip : lewati streaming yang sedang diputar dan mulai streaming trek berikutnya dalam antrean.
/end atau /stop : Anda dapat menghapus antrean dan mengakhiri aliran yang sedang diputar.
/shuffle : acak daftar antrian.
/seek : cari aliran dalam durasi yang diberikan..
/seekback : cari aliran secara mundur dalam durasi yang diberikan.
/reboot : restart bot untuk grup mu.

🥴<u>**Putaran berulang :**</u>

/loop [ᴅɪsᴀʙʟᴇ/ᴇɴᴀʙʟᴇ] atau [antara 1:10] 
    : Bot yang diaktifkan akan memutar aliran yang sedang diputar secara berulang sebanyak 10 kali atau sebanyak pengulangan yang diminta.

😜<u>**pengguna autentikasi :**</u>

Pengguna auth dapat menggunakan hak admin dalam bot tanpa hak admin dalam obrolan.

/auth [username]: menambahkan pengguna ke daftar autentikasi bot.
/unauth [username]: menghapus pengguna autentikasi dari daftar pengguna autentikasi.
/authusers: menampilkan daftar pengguna autentikasi dari grup.
"""

HELP_2 = """💞<u>**perintah putar:**</u>

perintah yang tersedia = putar, vplay, cplay

perintah forceᴩlay = playforce, vplayforce, cplayforce

**c** adalah singkatan dari channel play.
**v** adalah singkatan dari video ᴩlay.
**force** adalah singkatan dari force ᴩlay.

/play atau /vplay atau /cplay: mulai mengalirkan trek yang diminta pada obrolan video.

/playforce atau /vplayforce atau /cplayforce: **force ᴩlay** menyimpan aliran yang sedang berlangsung dan mulai mengalirkan trek yang diminta.

/channelplay [username atau id channel] atau [nonaktifkan]: hubungkan saluran ke grup dan mulai mengalirkan trek dengan bantuan perintah yang dikirim dalam grup.

🤨**<u>server  ᴩlaylists:</u>**

/playlist: periksa ᴩlaylist yang tersimpan di server.

/deleteplaylist: hapus semua trek yang tersimpan di ᴩlaylist Anda.

/play: mulai memutar dari ᴩlaylist yang tersimpan di server."""

HELP_3 = """😉<u>**perintah bot:**</u>

/stats: dapatkan 10 statistik global lagu, 10 pengguna bot, 10 obrolan di bot, 10 yang ada di obrolan, dan masih banyak lagi...
/sudolist: menunjukkan pengguna sudo bot musik.
/lyrics [nama lagu]: cari lirik untuk lagu yang diminta.
/song [nama lagu] atau [tautan yt]: unduh trek youtube apa pun dalam format audio atau video.
/player: dapatkan saluran ᴩlayer interaktif.
/queue: menunjukkan daftar trek yang diminta."""

HELP_4 = """😴<u>**perintah tambahan:**</u>

/start: memulai bot musik.

/help: mendapatkan menu bantuan dengan penjelasan perintah.

/ping: menunjukkan statistik sistem dan ᴩing bot.

🧐<u>**pengaturan grup:**</u>

/settings: menunjukkan pengaturan grup dengan menu sebaris interaktif."""

HELP_5 = """🥺**<u>tambahkan & hapus sudoers:</u>**
/addsudo [username atau reᴩly ke pengguna]
/delsudo [username atau reᴩly ke pengguna.]

🥶**<u>heroku:</u>**
/usage : menunjukkan penggunaan dyno bulan ini.

🤯**<u>variabel konfigurasi:</u>**
/get_var : dapatkan variabel konfigurasi dari heroku atau .env.
/del_var : hapus variabel konfigurasi pada heroku atau .env.
/set_var [nama variabel] [nilai] : tetapkan atau perbarui variabel konfigurasi pada heroku atau .env.

🤖**<u>perintah bot:</u>**
/restart : mulai ulang bot Anda.
/update : perbarui bot dari uᴩstream  reᴩo.
/speedtest: periksa kecepatan server bot.
/maintenance [aktifkan/nonaktifkan] 
/logger [aktifkan/nonaktifkan]: bot akan mulai mencatat aktivitas yang telah dilakukan pada bot.
/get_log [jumlah baris]: dapatkan log bot Anda [nilai default adalah 100 baris]
/autoend [aktifkan|nonaktifkan]: aktifkan akhiri streaming otomatis jika tidak ada yang mendengarkan.

🤑**<u>perintah statistik:</u>**
/activevoice: menunjukkan daftar obrolan suara aktif pada bot.
/activevideo: menunjukkan daftar obrolan video aktif pada bot.
/stats: menunjukkan statistik bot saat ini.

😒**<u>daftar hitam obrolan:</u>**
/blacklistchat [id obrolan]: daftar hitam obrolan agar tidak menggunakan bot.
/whitelistchat [id obrolan]: daftar putih obrolan yang masuk daftar hitam. 
/blacklistedchat: menunjukkan daftar obrolan yang masuk daftar hitam.

😤**<u>blokir pengguna:</u>**
/block [username atau reᴩly ke pengguna]: mulai mengabaikan pengguna, sehingga ia tidak dapat menggunakan perintah bot.
/unblock [username atau reᴩly ke pengguna]: membuka blokir pengguna yang diblokir.
/blockedusers: menunjukkan daftar pengguna yang diblokir.

🤬**<u>fitur gban:</u>**
/gban [username atau reᴩly ke pengguna]: secara global memblokir pengguna dari semua obrolan yang dilayani dan memasukkannya ke daftar hitam agar tidak menggunakan bot.
/ungban [username atau reᴩly ke pengguna]: secara global membuka blokir pengguna yang diblokir secara global.
/gbannedusers: menunjukkan daftar pengguna yang menggunakan banner secara global.

 🎥**<u>mode obrolan video:</u>**
/set_video_limit [jumlah obrolan]: mengatur jumlah maksimum obrolan video yang diizinkan pada bot. [nonaktif - 3]
/mode video [unduh|m3u8]: jika mode unduhan diaktifkan, bot akan mengunduh trek alih-alih menayangkannya dalam m3u8.

💔**<u>bot ᴩrivate:</u>**
/authorize [id obrolan]: mengizinkan obrolan untuk menggunakan bot.
/unauthorize [id obrolan]: melarang obrolan yang diizinkan.
/authorized: menunjukkan daftar obrolan yang diizinkan.

🍒**<u>fitur siaran:</u>**
/broadcast [pesan atau balas ke pesan]: menyiarkan pesan ke obrolan yang dilayani bot.

 <u>Mode penyiaran:</u>
**-pin**: memasukkan pesan yang disiarkan ke dalam obrolan yang disajikan.
**-pinloud**: memasukkan pesan yang disiarkan ke dalam obrolan yang disajikan dan mengirimkan pemberitahuan kepada anggota.
**-user**: menyiarkan pesan kepada pengguna yang telah memulai bot Anda.
**-assistant**: menyiarkan pesan Anda dari akun asisten bot.
**-nobot**: memaksa bot untuk tidak menyiarkan pesan.

**contoh:** `/broadcast -user -assistant -pin testing broadcast`"""

HELP_7 = """💌**<u>di sini Anda dapat menemukan fitur-fitur baru:</u>**

/alive: sekarang Anda dapat memeriksa apakah bot musik Haku aktif atau tidak
/id: untuk memeriksa ID pengguna dan obrolan
/gcast -user -assistant -pin testing broadcast`
/verify: verifikasi diri Anda di basis data Haku"""

HELP_8 = """💰**<u>ꜰfitur ꜰatau langganan siaran:</u>**

Sekarang Anda dapat membeli langganan siaran bulanan dan mingguan dari kami. Kami akan memberi Anda 3 langganan siaran mingguan dan 14 langganan siaran bulanan dengan batas pengiriman siaran setelah dua hari.

**hanya pemilik**
/addweekly [id pengguna]: tambahkan pengguna ke langganan siaran mingguan.
/addmonthly [id pengguna]: tambahkan pengguna ke langganan siaran bulanan.
/removesub [id pengguna]: hapus pengguna dari langganan siaran.
/checksubscription [id pengguna]: periksa sisa hari langganan pengguna dan siaran.
/substats: periksa jumlah total langganan dengan id dan jenis langganan beserta jumlah siaran.
/subscription_alert: untuk mengirim pesan peringatan ke pelanggan dengan sisa hari beserta jumlah siaran.

**siapa pun dapat menggunakan**
/mysubscription: Anda dapat  periksa langganan Anda dengan hari yang tersisa dan jumlah siaran.
/paidbroadcast: kirim pesan siaran ke semua pengguna dan grup sekaligus jika Anda memiliki langganan aktif."""