import os
from fpdf import FPDF

# Caminho da pasta principal onde estão seus arquivos txt
pasta_raiz = r'C:\Users\Isaac\Estudo\AgenteDigital_IA'

# Inicializa o PDF
pdf = FPDF()
pdf.set_font("Arial", size=12)

# Percorre todas as pastas e subpastas
for raiz, pastas, arquivos in os.walk(pasta_raiz):
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            caminho_txt = os.path.join(raiz, arquivo)
            
            try:
                # Lê o conteúdo do arquivo txt
                with open(caminho_txt, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                # Adiciona uma página ao PDF
                pdf.add_page()
                
                # Cabeçalho com caminho relativo do arquivo
                caminho_relativo = os.path.relpath(caminho_txt, pasta_raiz)
                pdf.set_font("Arial", 'B', 12)
                pdf.multi_cell(0, 10, txt=f"Arquivo: {caminho_relativo}")
                pdf.set_font("Arial", size=12)
                
                # Escreve o texto no PDF
                conteudo = conteudo.encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 10, txt=conteudo)
                
                print(f"Adicionado: {caminho_relativo}")
                
            except Exception as e:
                print(f"Erro ao converter {arquivo}: {e}")

# Salva o PDF único com todos os arquivos
caminho_pdf_final = os.path.join(pasta_raiz, "AgenteDigital_IA  .pdf")
pdf.output(caminho_pdf_final)

print("Conversão concluída! PDF único gerado:", caminho_pdf_final)
