import re
import numpy as np




stop_words_list = ['acaba', 'ama', 'ancak', 'arada', 'aslında', 'ayrıca', 'bana', 'bazı', 'belki', 'ben', 'benden',
                   'beni',
                   'benim', 'beri', 'bile', 'birçok', 'biri', 'birkaç', 'birkez', 'birşey', 'birşeyi', 'biz', 'bize',
                   'bizden',
                   'bizi', 'bizim', 'böyle', 'böylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunları',
                   'bunların',
                   'bunu', 'bunun', 'burada', 'çok', 'çünkü', 'da', 'daha', 'dahi', 'de', 'defa', 'değil', 'diğer',
                   'diye', 'dolayı',
                   'dolayısıyla', 'eğer', 'en', 'gibi', 'göre', 'halen', 'hangi', 'hatta', 'hem', 'henüz', 'hep',
                   'hepsi', 'her', 'herhangi',
                   'herkesin', 'hiç', 'hiçbir', 'için', 'ile', 'ilgili', 'ise', 'işte', 'itibaren', 'itibariyle',
                   'kadar', 'karşın', 'kendi',
                   'kendilerine', 'kendini', 'kendisi', 'kendisine', 'kendisini', 'kez', 'ki', 'kim', 'kimden', 'kime',
                   'kimi', 'kimse', 'mu',
                   'mü', 'mı', 'nasıl', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'niye', 'niçin', 'o',
                   'ona', 'ondan', 'onlar',
                   'onlardan', 'onları', 'onların', 'onu', 'onun', 'oysa', 'öyle', 'pek', 'rağmen', 'sadece', 'sanki',
                   'sen', 'senden', 'seni',
                   'senin', 'siz', 'sizden', 'sizi', 'sizin', 'şey', 'şeyden', 'şeyi', 'şeyler', 'şöyle', 'şu', 'şuna',
                   'şunda', 'şundan',
                   'şunları', 'şunu', 'tarafından', 'tüm', 'üzere', 've', 'veya', 'ya', 'yani', 'yerine', 'yine',
                   'yoksa', 'zaten', 'mi',
                   'onlari', 'acep', 'adeta', 'artık', 'aynen', 'az', 'bari', 'bazen', 'başka', 'biraz', 'bütün',
                   'dahil', 'daima', 'dair',
                   'dayanarak', 'fakat', 'halbuki', 'hani', 'hele', 'herkes', 'iken', 'ila', 'ilk', 'illa', 'iyi',
                   'iyice', 'kanımca', 'kere',
                   'keşke', 'kısaca', 'lakin', 'madem', 'meğer', 'nitekim', 'sonra', 'veyahut', 'yahut', 'şayet',
                   'şimdi', 'gerek', 'hakeza',
                   'hoş', 'kah', 'keza', 'mademki', 'mamafih', 'meğerki', 'meğerse', 'netekim', 'neyse', 'oysaki',
                   'velev', 'velhasıl',
                   'velhasılıkelam', 'yalnız', 'yok', 'zira', 'adamakıllı', 'bilcümle', 'binaen', 'binaenaleyh',
                   'birazdan', 'birden',
                   'birdenbire', 'birlikte', 'bitevi', 'biteviye', 'bittabi', 'bizatihi', 'bizce', 'bizcileyin',
                   'bizzat', 'buracıkta',
                   'buradan', 'büsbütün', 'çoğu', 'çoğun', 'çoğunca', 'çoğunlukla', 'çokça', 'çoklukla', 'dahilen',
                   'demin', 'demincek',
                   'deminden', 'derhal', 'derken', 'elbet', 'elbette', 'enikonu', 'epey', 'epeyce', 'epeyi', 'esasen',
                   'esnasında', 'etraflı',
                   'gibilerden', 'gibisinden', 'hemde','halihazırda', 'haliyle', 'hasılı', 'hulasaten', 'illaki', 'itibarıyla',
                   'iyicene', 'kala',
                   'külliyen', 'nazaran', 'nedeniyle', 'nedense', 'nerden', 'nerdeyse', 'nereden', 'neredeyse', 'neye',
                   'neyi', 'nice', 'nihayet',
                   'nihayetinde', 'onca', 'önce', 'önceden', 'önceleri', 'öncelikle', 'oracık', 'oracıkta', 'orada',
                   'oradan', 'oranca',
                   'oranla', 'oraya', 'peyderpey', 'sahiden', 'sonradan', 'sonraları', 'sonunda', 'şuncacık',
                   'şuracıkta', 'tabii',
                   'tam', 'tamam', 'tamamen', 'tamamıyla', 'tek', 'vasıtasıyla', 'doğru', 'gelgelelim', 'gırla',
                   'hasebiyle', 'zarfında',
                   'öbür', 'başkası', 'beriki', 'birbiri', 'birçoğu', 'birileri', 'birisi', 'birkaçı', 'bizimki',
                   'burası', 'diğeri',
                   'filanca', 'hangisi', 'hiçbiri', 'kaçı', 'kaynak', 'kimisi', 'kimsecik', 'kimsecikler', 'neresi',
                   'öbürkü', 'öbürü',
                   'onda', 'öteki', 'ötekisi', 'sana', 'şunlar', 'şunun', 'şuracık', 'şurası', 'nın', 'nin', 'nun',
                   'nün', 'ın',
                   'in', 'un', 'ün']
contractions_convert_dictionary = {
    "amk": "amına koyayım",
    "aq": "amına koyayım",
    "a.q": "amına koyayım",
    "a.w": "amına koyayım",
    "ak": "amına koyayım",
    "a.k": "amına koyayım",
    "mq": "amına koyayım",
    "mk": "amına koyayım",
    "aqqq": "amına koyayım",
    "awk": "amına koyayım",
    "s.kine": "sikine",
    "fuck": "siktir",
    "as": "ananı sikim",
    "ananskm": "ananı sikim",
    "skm": "sikim",
    "s.ktigim": "siktiğim",
    "s.ktugm": "soktugum",
    "b.k": "bok",
    "g.t": "göt",
    "s..": "siktir",
    "ziktir": "siktir",
    "b.kunu": "bokunu",
    "s...": "siktir",
    "s*çımaya": "sıçmaya",
    "amkdjdkd": "amına koyayım",
    "lgbtli": "lezbiyen",
    "lgbt": "lezbiyen",
    "orrosspuu": "orospu",
    "yardagıma": "yarrağıma"
}

black_list = {"kopek": "köpek",
              "gotlu": "götlü",
              "got": "göt",
              "kotu": "kötü"}


class CLEANING:
    def __init__(self, raw_text, contractions, stopwords, blacklist):
        if isinstance(raw_text, float) and np.isnan(raw_text):
            raw_text = ''  # NaN değerini boş bir string ile değiştir

        raw_text = raw_text.replace("İ", "i")  # Bozuk i karakterlerine çözüm üretmek adına eklenmiştir.
        raw_text = raw_text.replace("Â", "a")
        raw_text = raw_text.replace("â", "a")
        self.Text = raw_text
        self.Contractions = contractions
        self.blacklist = blacklist
        self.StopWords = stopwords

    def convert_character(self, raw_text):
        raw_text = raw_text.replace("ş", "s")
        raw_text = raw_text.replace("ğ", "g")
        raw_text = raw_text.replace("ç", "c")
        raw_text = raw_text.replace("ü", "u")
        # raw_text = raw_text.replace("ı", "i")
        raw_text = raw_text.replace("Ş", "s")
        raw_text = raw_text.replace("Ğ", "g")
        raw_text = raw_text.replace("Ç", "c")
        raw_text = raw_text.replace("Ü", "u")
        raw_text = raw_text.replace("ö", "o")
        raw_text = raw_text.replace("Ö", "o")

        return raw_text

    def lowercase(self, text):
        return text.lower()

    def split(self, text):
        return text.split()

    def tweet_tag_clean(self, text):
        temp_text = re.sub("@[A-Za-z0-9_]+", "", text)
        return ' '.join(word for word in temp_text.split() if not word[0] == "#")

    def http_clean(self, text):
        regex = re.compile(r'<[^>]+>')
        temp_text = regex.sub('', text)
        return re.sub(r'http\S+', '', temp_text)

    def numeric_clean(self, text):
        return re.sub("[0-9]", "", text)

    def special_character_clean(self, text):
        return re.sub(r'[_"\-;%()|+&=^*%.”“’,!?¦‘:#$@\[\]/<>]', '', text)

    def stopwords_clean(self, text):
        return ' '.join(word for word in text.split() if word not in stop_words_list)

    def single_characters_clean(self, text):
        return ' '.join([w for w in text.split() if len(w) > 1])

    def remove_emojis(self,text):

        # Unicode aralıklarını kullanarak emojileri tanımlar
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # Yüz ifadeleri
            "\U0001F300-\U0001F5FF"  # Simgeler ve semboller
            "\U0001F680-\U0001F6FF"  # Ulaşım ve simgeler
            "\U0001F1E0-\U0001F1FF"  # Bayraklar
            "\U00002500-\U00002BEF"  # Çinli karakterler
            "\U00002702-\U000027B0"  # Diğer semboller
            "\U0001F900-\U0001F9FF"  # Ek simgeler
            "\U00002600-\U000026FF"  # Diğer semboller
            "\U0001F700-\U0001F77F"  # Alkimia simgeleri
            "\U0001F780-\U0001F7FF"  # Geometrik şekiller
            "\U0001F800-\U0001F8FF"  # İlginç semboller
            "\U00002B50-\U00002B55"  # Yıldızlar ve benzerleri
            "]+", flags=re.UNICODE
        )

        return emoji_pattern.sub(r'', text)

    def remove_character(self, text, char_to_remove):
        """
        Belirli bir karakteri metinden siler.
        :param text: İşlenecek metin
        :param char_to_remove: Silinecek karakter
        :return: Karakteri silinmiş metin
        """
        return text.replace(char_to_remove, '')

    def clean(self):
        temp_text = self.Text
        temp_text = self.lowercase(temp_text)
        temp_text = self.split(temp_text)

        if self.Contractions:  # Kısaltmaları dönüştür
            new_text = []
            for word in temp_text:
                if word in contractions_convert_dictionary:
                    new_text.append(contractions_convert_dictionary[word])
                else:
                    new_text.append(word)
            temp_text = " ".join(new_text)

        if self.StopWords:
            temp_text = self.stopwords_clean(temp_text)

        temp_text = self.tweet_tag_clean(temp_text)  # tweet ve tag temizle
        temp_text = self.http_clean(temp_text)  # http tag temizle
        temp_text = self.numeric_clean(temp_text)  # numeric değerleri temizle

        temp_text = self.remove_emojis(temp_text)  # emojileri silme

        temp_text=self.remove_character(temp_text, "'")  # ' silmek için

        temp_text = self.special_character_clean(temp_text)  # special karakterleri temizle
        temp_text = self.single_characters_clean(temp_text)  # special karakterleri ve emojileri temizle

        temp_text = temp_text.lstrip().rstrip()  # text baş ve sonundaki boşlukları at

        if len(temp_text) > 0:
            try:
                temp_text = self.convert_character(temp_text)
                if self.blacklist:  # blacklist
                    new_text = []
                    for word in temp_text.split(' '):
                        if word in black_list:
                            new_text.append(black_list[word])
                        else:
                            new_text.append(word)
                    temp_text = " ".join(new_text)
                return temp_text
            except Exception as e:
                print(f"Error: {e}, Text: {temp_text}")
                return temp_text

        return temp_text