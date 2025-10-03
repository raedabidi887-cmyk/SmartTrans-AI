from langdetect import detect, DetectorFactory
import re

# Fixer la seed pour des résultats cohérents
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    """
    Détecte la langue du texte fourni
    
    Args:
        text (str): Le texte à analyser
        
    Returns:
        str: Code de langue détecté (ex: 'fr', 'en', 'es', 'ar', etc.)
    """
    try:
        # Nettoyer le texte
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        
        if not cleaned_text:
            return "unknown"
        
        # Détecter la langue
        detected_lang = detect(cleaned_text)
        
        # Mapping des codes de langue vers des noms plus lisibles
        language_names = {
            'fr': 'Français',
            'en': 'Anglais',
            'es': 'Espagnol',
            'de': 'Allemand',
            'it': 'Italien',
            'pt': 'Portugais',
            'ru': 'Russe',
            'ar': 'Arabe',
            'zh': 'Chinois',
            'ja': 'Japonais',
            'ko': 'Coréen',
            'hi': 'Hindi',
            'nl': 'Néerlandais',
            'pl': 'Polonais',
            'tr': 'Turc',
            'sv': 'Suédois',
            'da': 'Danois',
            'no': 'Norvégien',
            'fi': 'Finnois',
            'hu': 'Hongrois',
            'cs': 'Tchèque',
            'sk': 'Slovaque',
            'ro': 'Roumain',
            'bg': 'Bulgare',
            'hr': 'Croate',
            'sl': 'Slovène',
            'et': 'Estonien',
            'lv': 'Letton',
            'lt': 'Lituanien',
            'mt': 'Maltais',
            'el': 'Grec',
            'he': 'Hébreu',
            'th': 'Thaï',
            'vi': 'Vietnamien',
            'id': 'Indonésien',
            'ms': 'Malais',
            'fa': 'Persan',
            'ur': 'Ourdou',
            'bn': 'Bengali',
            'ta': 'Tamoul',
            'te': 'Télougou',
            'mr': 'Marathi',
            'gu': 'Gujarati',
            'kn': 'Kannada',
            'ml': 'Malayalam',
            'pa': 'Punjabi',
            'or': 'Odia',
            'as': 'Assamais',
            'ne': 'Népalais',
            'si': 'Cingalais',
            'my': 'Birman',
            'km': 'Khmer',
            'lo': 'Lao',
            'ka': 'Géorgien',
            'am': 'Amharique',
            'sw': 'Swahili',
            'yo': 'Yoruba',
            'ig': 'Igbo',
            'ha': 'Hausa',
            'zu': 'Zoulou',
            'af': 'Afrikaans',
            'zu': 'Zoulou',
            'xh': 'Xhosa',
            'st': 'Sotho du Sud',
            'tn': 'Tswana',
            'ts': 'Tsonga',
            've': 'Venda',
            'nr': 'Ndebele du Sud',
            'ss': 'Swati',
            'nd': 'Ndebele du Nord',
            'sn': 'Shona',
            'rw': 'Kinyarwanda',
            'lg': 'Ganda',
            'ak': 'Akan',
            'tw': 'Twi',
            'ee': 'Ewe',
            'fon': 'Fon',
            'dyu': 'Dioula',
            'bam': 'Bambara',
            'man': 'Mandingue',
            'wol': 'Wolof',
            'ful': 'Peul',
            'son': 'Songhaï',
            'zul': 'Zoulou',
            'xho': 'Xhosa',
            'afr': 'Afrikaans',
            'nbl': 'Ndebele du Sud',
            'nso': 'Pedi',
            'sot': 'Sotho du Sud',
            'tsn': 'Tswana',
            'tso': 'Tsonga',
            'ven': 'Venda',
            'zul': 'Zoulou',
            'xho': 'Xhosa',
            'afr': 'Afrikaans',
            'nbl': 'Ndebele du Sud',
            'nso': 'Pedi',
            'sot': 'Sotho du Sud',
            'tsn': 'Tswana',
            'tso': 'Tsonga',
            'ven': 'Venda'
        }
        
        return language_names.get(detected_lang, detected_lang.upper())
        
    except Exception as e:
        print(f"Erreur lors de la détection de langue: {e}")
        return "unknown" 