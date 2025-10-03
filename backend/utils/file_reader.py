import fitz  # PyMuPDF
from docx import Document
from pathlib import Path
import re

def read_file_content(file_path: Path) -> str:
    """
    Lit le contenu d'un fichier selon son extension
    
    Args:
        file_path (Path): Chemin vers le fichier
        
    Returns:
        str: Contenu textuel du fichier
    """
    file_extension = file_path.suffix.lower()
    
    try:
        if file_extension == '.pdf':
            return read_pdf_content(file_path)
        elif file_extension == '.docx':
            return read_docx_content(file_path)
        elif file_extension == '.txt':
            return read_txt_content(file_path)
        else:
            raise ValueError(f"Format de fichier non supporté: {file_extension}")
            
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        return ""

def read_pdf_content(file_path: Path) -> str:
    """
    Lit le contenu d'un fichier PDF
    
    Args:
        file_path (Path): Chemin vers le fichier PDF
        
    Returns:
        str: Texte extrait du PDF
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        doc.close()
        
        # Nettoyer le texte
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
        
    except Exception as e:
        print(f"Erreur lors de la lecture du PDF: {e}")
        return ""

def read_docx_content(file_path: Path) -> str:
    """
    Lit le contenu d'un fichier DOCX
    
    Args:
        file_path (Path): Chemin vers le fichier DOCX
        
    Returns:
        str: Texte extrait du DOCX
    """
    try:
        doc = Document(file_path)
        text = ""
        
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        # Nettoyer le texte
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
        
    except Exception as e:
        print(f"Erreur lors de la lecture du DOCX: {e}")
        return ""

def read_txt_content(file_path: Path) -> str:
    """
    Lit le contenu d'un fichier TXT
    
    Args:
        file_path (Path): Chemin vers le fichier TXT
        
    Returns:
        str: Contenu du fichier TXT
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Nettoyer le texte
        content = re.sub(r'\s+', ' ', content).strip()
        
        return content
        
    except Exception as e:
        print(f"Erreur lors de la lecture du TXT: {e}")
        return "" 