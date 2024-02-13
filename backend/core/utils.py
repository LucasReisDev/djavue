from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import os


def gerar_relatorio_pdf(dados):
    nome_arquivo = os.path.join('C:\\Users\\Mcluc\\OneDrive\\Área de Trabalho\\testevuedjango\\backend', 'relatorio.pdf')
    
    # Define o número de colunas e linhas desejadas
    num_colunas = 2
    num_linhas = (len(dados) + num_colunas - 1) // num_colunas
    
    # Calcula a largura e altura de cada célula
    largura_celula = (letter[0] - 100) / num_colunas
    altura_celula = 100
    
    # Inicia o canvas do PDF
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    
    # Define a posição inicial para renderizar os dados
    x_inicial = 50
    y_inicial = letter[1] - 50
    
    # Itera sobre os dados e renderiza cada venda
    for i, dado in enumerate(dados):
        # Calcula o índice da coluna e linha atual
        coluna_atual = i % num_colunas
        linha_atual = i // num_colunas
        
        # Calcula a posição x e y da célula atual
        x_atual = x_inicial + (coluna_atual * largura_celula)
        y_atual = y_inicial - (linha_atual * altura_celula)
        
        # Renderiza os dados na célula atual
        c.drawString(x_atual, y_atual - 20, f"Data: {dado['data']}")
        c.drawString(x_atual, y_atual - 40, f"Vendedor: {dado['vendedor_nome']}")
        c.drawString(x_atual, y_atual - 60, f"Cliente: {dado['cliente_nome']}")
        c.drawString(x_atual, y_atual - 80, f"Valor Total: {dado['valor_total']}")
        
        # Verifica se precisa iniciar uma nova página
        if i + 1 == num_linhas * num_colunas:
            c.showPage()
    
    # Fecha o canvas
    c.save()
    
    # Retorna o arquivo PDF
    return nome_arquivo

def gerar_relatorio_excel(dados):
    nome_arquivo = os.path.join('C:\\Users\\Mcluc\\OneDrive\\Área de Trabalho\\testevuedjango\\backend', 'relatorio.xlsx')
    
    # Cria um DataFrame com os dados
    df = pd.DataFrame(dados)
    
    # Salva o DataFrame em um arquivo Excel
    df.to_excel(nome_arquivo, index=False)
    
    # Retorna o arquivo Excel
    return nome_arquivo
