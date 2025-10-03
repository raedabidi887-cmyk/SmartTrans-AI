from googletrans import Translator
import time

# Mapping des langues vers les codes Google Translate
LANGUAGE_CODES = {
    'Français': 'fr',
    'Anglais': 'en',
    'Espagnol': 'es',
    'Allemand': 'de',
    'Italien': 'it',
    'Portugais': 'pt',
    'Russe': 'ru',
    'Arabe': 'ar',
    'Chinois': 'zh-cn',
    'Japonais': 'ja',
    'Coréen': 'ko',
    'Hindi': 'hi',
    'Néerlandais': 'nl',
    'Polonais': 'pl',
    'Turc': 'tr',
    'Suédois': 'sv',
    'Danois': 'da',
    'Norvégien': 'no',
    'Finnois': 'fi',
    'Hongrois': 'hu',
    'Tchèque': 'cs',
    'Slovaque': 'sk',
    'Roumain': 'ro',
    'Bulgare': 'bg',
    'Croate': 'hr',
    'Slovène': 'sl',
    'Estonien': 'et',
    'Letton': 'lv',
    'Lituanien': 'lt',
    'Maltais': 'mt',
    'Grec': 'el',
    'Hébreu': 'he',
    'Thaï': 'th',
    'Vietnamien': 'vi',
    'Indonésien': 'id',
    'Malais': 'ms',
    'Persan': 'fa',
    'Ourdou': 'ur',
    'Bengali': 'bn',
    'Tamoul': 'ta',
    'Télougou': 'te',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Punjabi': 'pa',
    'Odia': 'or',
    'Assamais': 'as',
    'Népalais': 'ne',
    'Cingalais': 'si',
    'Birman': 'my',
    'Khmer': 'km',
    'Lao': 'lo',
    'Géorgien': 'ka',
    'Amharique': 'am',
    'Swahili': 'sw',
    'Yoruba': 'yo',
    'Igbo': 'ig',
    'Hausa': 'ha',
    'Zoulou': 'zu',
    'Afrikaans': 'af',
    'Xhosa': 'xh',
    'Sotho du Sud': 'st',
    'Tswana': 'tn',
    'Tsonga': 'ts',
    'Venda': 've',
    'Ndebele du Sud': 'nr',
    'Swati': 'ss',
    'Ndebele du Nord': 'nd',
    'Shona': 'sn',
    'Kinyarwanda': 'rw',
    'Ganda': 'lg',
    'Akan': 'ak',
    'Twi': 'tw',
    'Ewe': 'ee',
    'Fon': 'fon',
    'Dioula': 'dyu',
    'Bambara': 'bam',
    'Mandingue': 'man',
    'Wolof': 'wol',
    'Peul': 'ful',
    'Songhaï': 'son'
}

def translate_text(text: str, target_language: str) -> str:
    """
    Traduit le texte vers la langue cible
    
    Args:
        text (str): Le texte à traduire
        target_language (str): La langue cible (nom en français)
        
    Returns:
        str: Le texte traduit
    """
    try:
        # Obtenir le code de langue
        target_code = LANGUAGE_CODES.get(target_language, target_language.lower())
        
        # Créer l'instance du traducteur
        translator = Translator()
        
        # Diviser le texte en chunks si nécessaire (limite Google Translate)
        max_chunk_size = 4000
        chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        
        translated_chunks = []
        
        for chunk in chunks:
            if chunk.strip():
                # Traduire le chunk
                translation = translator.translate(chunk, dest=target_code)
                translated_chunks.append(translation.text)
                
                # Pause pour éviter les limitations de rate
                time.sleep(0.1)
        
        # Combiner les chunks traduits
        translated_text = ' '.join(translated_chunks)
        
        return translated_text
        
    except Exception as e:
        print(f"Erreur lors de la traduction: {e}")
        # En cas d'erreur, retourner le texte original
        return text 