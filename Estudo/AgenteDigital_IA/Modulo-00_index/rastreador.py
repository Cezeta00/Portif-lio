import yt_dlp
import json
import os
import subprocess



base_dir = os.path.dirname(os.path.abspath(__file__))
url_canal = input("Qual a URL do canal? ")
limit = int(input("Quantos vídeos deseja rastrear? "))
opt = int(input("1) Rastear por popularidade\n2) Rastrear por data\n "))
url_canal_limpa = url_canal.split('?')[0].rstrip('/')
url_populares = f"{url_canal_limpa}/videos?sort=p"
canal_nome = url_canal_limpa.split('@')[-1]

subpasta = os.path.join(base_dir, "AgenteDigital_IA", "Modulo-00_index", "json")


print(f"Rastreando os vídeos mais assistidos do canal: {url_canal}...")
if(opt == 1):
    print(f"\n--- TOP {limit} VÍDEOS MAIS ASSISTIDOS ---")
elif(opt == 2):
    print(f"\n--- TOP {limit} VÍDEOS RECENTES---")
else: print("OPÇÃO INVALIDA")
ydl_opts = {
    'extract_flat': True,
    'quiet': True
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        info_dict = ydl.extract_info(url_populares, download=False)
        match opt:
         case 1:
          if 'entries' in info_dict:
            videos = sorted(
                info_dict['entries'],
                key=lambda v: v.get('view_count') or 0,
                reverse=True
            )[:limit]

            for i, video in enumerate(videos):
                titulo = video.get('title')
                views = video.get('view_count') or 0
                url_video = f"https://youtube.com/watch?v={video.get('id')}"
                print(f"{i+1}. {titulo} ({views} views) / {url_video}")
          else:
            print("Não foi possível encontrar vídeos.")

         case 2: 
            if 'entries' in info_dict:
             for i, video in enumerate(info_dict['entries'][:limit]):
                titulo = video.get('title')
                url_video = f"https://youtube.com/watch?v={video.get('id')}"
                print(f"{i+1}. {titulo} / {url_video}")
            else:
                print("Não foi possível encontrar vídeos.")

         case _:
            print("Opção inválida")
            
    except Exception as e:
        print(f"Erro ao rastrear: {e}")
            
            
        
        # Garante que a pasta existe
    if not os.path.exists(subpasta):
        os.makedirs(subpasta)
            # --- Salvar em JSON apenas com titulo e url ---
    data = [{
            "titulo": video.get('title'),
            "url": f"https://youtube.com/watch?v={video.get('id')}"
            }
                for video in info_dict['entries'][:limit]
                ]
            # Caminho completo do arquivo dentro da subpasta
    caminho_json = os.path.join(subpasta, f"{limit}videos-{canal_nome}.json")
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\nArquivo '{caminho_json}' criado com {limit} títulos e URLs.")
    # Executar o transcritor.py usando caminho relativo
    subprocess.run(["python", os.path.join(base_dir, "AgenteDigital_IA", "Modulo-00_index", "transcritor.py")])
    print("passando para o transcritor")
    
validos = []
for video in info_dict['entries']:
    titulo = video.get('title')
    video_id = video.get('id')
    url_video = f"https://youtube.com/watch?v={video_id}"

    # Se não tem título ou está indisponível, pula
    if not titulo or video.get("availability") == "unavailable":
        print(f"[INDISPONÍVEL] {url_video}")
        continue

    validos.append({
        "titulo": titulo,
        "url": url_video
    })

    # Para quando já tiver atingido o limite de válidos
    if len(validos) >= limit:
        break

# Salva só os válidos
caminho_json = os.path.join(subpasta, f"{len(validos)}videos-{canal_nome}.json")
with open(caminho_json, "w", encoding="utf-8") as f:
    json.dump(validos, f, ensure_ascii=False, indent=4)

print(f"\nArquivo '{caminho_json}' criado com {len(validos)} títulos e URLs válidos.")
