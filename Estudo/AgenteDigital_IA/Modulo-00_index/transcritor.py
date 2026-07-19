import os
import yt_dlp
import webvtt
import json
import glob
import re
import subprocess

# Pasta onde estão os JSONs
json_dir = r"C:\Users\Isaac\Estudo\AgenteDigital_IA\Modulo-00_index\json"

# Lista todos os arquivos .json dentro da pasta
json_files = glob.glob(os.path.join(json_dir, "*.json"))

for json_file in json_files:
    print(f"\nProcessando arquivo: {json_file}")

# Pasta onde salvar as transcrições
output_dir = r"C:\Users\Isaac\Estudo\AgenteDigital_IA\Modulo-Automatico"
os.makedirs(output_dir, exist_ok=True)

# Carrega lista de links do JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    nome_video = item.get("titulo")
    url_video = item.get("url")
    if not url_video:
        continue

    print(f"\nBuscando transcrição do vídeo: {url_video}")

    ydl_opts = {
        'writeautomaticsub': True,
        'writesubtitles': True,
        'subtitleslangs': ['all'],
        'skip_download': True,
        'outtmpl': 'legenda_temporaria'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url_video])
            arquivo_vtt = 'legenda_temporaria.pt.vtt'

            if os.path.exists(arquivo_vtt):
                print("\n--- TRANSCRIÇÃO ENCONTRADA ---")

                linhas_limpas = []
                for bloco in webvtt.read(arquivo_vtt):
                    texto_bloco = bloco.text.strip().replace('\n', ' ')
                    if texto_bloco and (not linhas_limpas or linhas_limpas[-1] != texto_bloco):
                        linhas_limpas.append(texto_bloco)

                texto_completo = " ".join(linhas_limpas)
                
                
               # Sanitiza o nome do vídeo para ser usado como nome da pasta
            nome_video_limpo = re.sub(r'[\\/*?:"<>|]', "", nome_video)
            # Cria uma pasta específica para o vídeo
            pasta_video = os.path.join(output_dir, nome_video_limpo)
            os.makedirs(pasta_video, exist_ok=True)
            # Nome fixo para o arquivo de saída
            nome_saida = os.path.join(pasta_video, "Original.txt")
            with open(nome_saida, "w", encoding="utf-8") as f:
                
                print("Não encontramos nenhuma legenda ou transcrição em português para este vídeo.")

        except Exception as e:
            print(f"Ocorreu um erro ao processar o link: {e}")

# Remove o JSON após consumo
os.remove(json_file)
print(f"\n[Limpeza] O arquivo '{json_file}' foi removido.")

# Executar um script Python
subprocess.run(["python", r"C:\Users\Isaac\Estudo\AgenteDigital_IA\Modulo-00_index\conversor.py"])
print("indo para o conversor")
