from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import shutil
from pathlib import Path
import uuid

from utils.detect_language import detect_language
from utils.translate import translate_text
from utils.file_reader import read_file_content
from utils.file_writer import write_translated_file

app = FastAPI(title="SmartTrans AI", description="Application de traduction automatique")

# Configuration des templates
templates = Jinja2Templates(directory="backend/templates")

# Créer le dossier temp s'il n'existe pas
temp_dir = Path("temp")
temp_dir.mkdir(exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Page d'accueil avec l'interface utilisateur"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    """Analyse le fichier uploadé et détecte la langue"""
    try:
        # Vérifier le type de fichier
        allowed_extensions = {'.pdf', '.docx', '.txt'}
        file_extension = Path(file.filename).suffix.lower()
        
        if file_extension not in allowed_extensions:
            raise HTTPException(status_code=400, detail="Format de fichier non supporté")
        
        # Créer un nom unique pour le fichier
        file_id = str(uuid.uuid4())
        temp_file_path = temp_dir / f"{file_id}{file_extension}"
        
        # Sauvegarder le fichier
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Lire le contenu du fichier
        content = read_file_content(temp_file_path)
        
        if not content.strip():
            raise HTTPException(status_code=400, detail="Le fichier est vide ou ne contient pas de texte")
        
        # Détecter la langue
        detected_language = detect_language(content)
        
        return {
            "success": True,
            "detected_language": detected_language,
            "file_id": file_id,
            "file_extension": file_extension,
            "content_preview": content[:200] + "..." if len(content) > 200 else content
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse: {str(e)}")

@app.post("/translate")
async def translate_file(
    file_id: str = Form(...),
    file_extension: str = Form(...),
    target_language: str = Form(...)
):
    """Traduit le fichier vers la langue cible"""
    try:
        # Chemin du fichier original
        original_file_path = temp_dir / f"{file_id}{file_extension}"
        
        if not original_file_path.exists():
            raise HTTPException(status_code=404, detail="Fichier non trouvé")
        
        # Lire le contenu original
        original_content = read_file_content(original_file_path)
        
        # Traduire le contenu
        translated_content = translate_text(original_content, target_language)
        
        # Générer le fichier traduit
        output_filename = f"translated_{file_id}{file_extension}"
        output_path = temp_dir / output_filename
        
        write_translated_file(output_path, translated_content, file_extension)
        
        return {
            "success": True,
            "output_filename": output_filename,
            "message": f"Fichier traduit avec succès vers {target_language}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la traduction: {str(e)}")

@app.get("/download/{filename}")
async def download_file(filename: str):
    """Télécharge le fichier traduit"""
    file_path = temp_dir / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type='application/octet-stream'
    )

@app.on_event("startup")
async def startup_event():
    """Nettoyer les fichiers temporaires au démarrage"""
    for file in temp_dir.glob("*"):
        try:
            file.unlink()
        except:
            pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 