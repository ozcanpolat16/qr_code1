from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Bu satırı buraya ekleyin
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    target_time = '2025-01-17 03:45:00'

    message = """
    Tanıştığımız o ilk günden bu yana, birlikte mutluluğun en saf halini yaşadığımız güzel günlerimiz de oldu, 
    birbirimize dayanamadığımız acı dolu günlerimiz de. Ama her duyguyu seninle yaşamayı o kadar çok sevdim ki, 
    her anının içimde bıraktığı izi tarif etmek imkânsız. Bir konuşabilsem diyişini ve gözlerime baktığındaki masumiyeti 
    unutmak mümkün değil.

    Artık “Neden olmadı?” ya da “Olur muydu?” diye düşünmenin hiçbir anlamı yok ama yine de, kendi kendime defalarca sordum: 
    “Denesek farklı olur muydu? Belki de bu, ömür boyu sürecek güzel bir hikâyenin ilk adımı olurdu… Ya da birbirine zarar 
    veren iki insan olarak hatırlanırdık. Bunu bilemeyeceğiz. Ve belki de asıl acı olan bu belirsizlik.

    Seninle bu zamana kadar sanki bir dizinin başrollerini paylaşıyor gibiydik. Sen “Son Yaz”ın Yağmur’u gibiydin, 
    ben de Akgünü. Ama bu bir dizi değildi ve biliyoruz ki her dizi mutlu sonla da bitmiyor zaten. Biz ayrı iki insanız, 
    Özcan ve Yağmur. Ve hikâyemizin bu noktası da bir veda oldu. Eğer bir gün yeniden “Akgün”ü bulmak istersen, sana başarılar dilerim. 
    Çünkü artık Akgün olmak istemiyorum. Beni “Özcan” olarak sevebilecek birine ihtiyacım var. Her şeyin saf haliyle, korkusuzca 
    yaşanabileceği, duygularını göz ardı etmek zorunda kalmayan, şakalarımın ardındaki gülümsemeyi görebilecek birine…

    Sana “Artık kızgın değilim” desem de, bu mesajı okuduğunda içimdeki kızgınlığın izlerini hissedeceksin, biliyorum. 
    Ama yine de, sana gerçekten kızgın kalamıyorum Yağmur. Çünkü ne kadar incinmiş olsam da içimdeki o kızgınlık gelip geçiyor. 
    Yerini, hep seni güzel hatırlayacak bir sevgiye bırakıyor.

    Şimdi, aşkı yaşayabileceğim kişiye veda ediyorum. Bir insan, başka bir insana kaç kere veda edebilir ki? Belki de bu da aslında 
    bir veda değil, sadece hikayemizin başka bir evresi. Bunu asla bilemeyeceğiz.

    Hayatın boyunca geçtiğin yollarda, elindeki çiçeğin huzurlu kokusu ve mutluluğu her zaman seninle olsun. 
    Seni hep güzel hatırlayacağım Yağmur. Umarım sen de beni güzel hatırlarsın. Hoşça kal, küçük Yağmur.
    """

    if current_time < target_time:
        message = "17 Ocak 03:45'da görüşmek dileğiyle :)"
    return render_template('message.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
