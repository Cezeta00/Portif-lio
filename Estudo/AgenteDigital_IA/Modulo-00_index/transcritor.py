import os
import yt_dlp
import webvtt
import json
import glob
import re
import time
import shutil

# Marca o início
inicio = time.time()

# Caminho base
base_dir = os.path.dirname(os.path.abspath(__file__))

json_dir = os.path.join(base_dir, "AgenteDigital_IA", "Modulo-00_index", "json")
json_files = glob.glob(os.path.join(json_dir, "*.json"))

output_dir = os.path.join(base_dir, "AgenteDigital_IA", "Modulo-Automatico")
os.makedirs(output_dir, exist_ok=True)

for json_file in json_files:
    print(f"\nProcessando arquivo: {json_file}")
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        url_video = item.get("url")
        if not url_video:
            continue

        print(f"\nBuscando transcrição do vídeo: {url_video}")
        idiomas = ["pt", "de", "hi", "fr","es", "en" ]
        
        for idioma in idiomas:
            ydl_opts = {
                'writeautomaticsub': True,
                'writesubtitles': True,
                'subtitleslangs': [idioma],
                'skip_download': True,
                'outtmpl': os.path.join(output_dir, '%(id)s', '%(id)s.%(lang)s.vtt'),
                'sleep_interval': 0.2,
                'max_sleep_interval': 0.5
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(url_video, download=False)
                    canal = info.get("uploader", "CanalDesconhecido")
                    video_id = info.get("id")
                    canal_limpo = re.sub(r'[\\/*?:"<>|]', "", canal)
                    pasta_video = os.path.join(output_dir, f"{canal_limpo}_{video_id}")
                    os.makedirs(pasta_video, exist_ok=True)

                    ydl.download([url_video])
                    time.sleep(0.3)
                except Exception as e:
                    print(f"erro ao baixar o idioma {idioma}: {e}")

            # Procura legendas baixadas
            pasta_legendas = os.path.join(output_dir, video_id)
            arquivos_vtt = glob.glob(os.path.join(pasta_legendas, "*.vtt"))

            if arquivos_vtt:
                print("\n--- TRANSCRIÇÕES ENCONTRADAS ---")
                for arquivo_vtt in arquivos_vtt:
                    try:
                        linhas_limpas = []
                        for bloco in webvtt.read(arquivo_vtt):
                            texto_bloco = bloco.text.strip().replace('\n', ' ')
                            if texto_bloco and (not linhas_limpas or linhas_limpas[-1] != texto_bloco):
                                linhas_limpas.append(texto_bloco)

                        texto_completo = " ".join(linhas_limpas)
                        idioma_vtt = os.path.splitext(arquivo_vtt)[0].split(".")[-1]
                        nome_saida = os.path.join(pasta_video, f"Transcricao_{idioma_vtt}.txt")

                        with open(nome_saida, "w", encoding="utf-8") as f:
                            f.write(texto_completo)

                    except Exception as e:
                        print(f"Erro ao processar {arquivo_vtt}: {e}")
                        # Marca o fim
                        
fim = time.time()

# Calcula o tempo total em segundos
tempo_total = fim - inicio
print(f"Tempo total de execução: {tempo_total:.2f} segundos")
print(f"Tempo total de execução: {tempo_total/60:.2f} minutos")

# Caminha por todas as subpastas dentro de output_dir
for pasta in os.listdir(output_dir):
    caminho_pasta = os.path.join(output_dir, pasta)
    if os.path.isdir(caminho_pasta):
        arquivos = os.listdir(caminho_pasta)
        # Verifica se todos os arquivos são .vtt
        if all(arq.endswith(".vtt") for arq in arquivos):
            shutil.rmtree(caminho_pasta)  # apaga a pasta inteira
            print(f"Pasta removida: {caminho_pasta}")