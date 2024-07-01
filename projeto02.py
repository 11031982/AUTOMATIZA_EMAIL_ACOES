import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# Função para digitar ação e data inicial e final
ticket = input("Digite o código da ação desejada: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
dt_final = input("Digite a data final (aaaa-mm-dd): ")

# Buscando a ação no site yfinance com data inicial e final e armazenando na variável
dados = yfinance.Ticker(ticket)
tabela =dados.history(start= dt_inicial, end= dt_final)
fechamento = tabela.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "rafael@gmail.com"
assunto = "Analises do Projeto 2020"

mensagem = f"""

Bom dia,

Segue abaixo as análises solicitada da ação {ticket}

Referente as data inicial {dt_inicial} até data final {dt_final}

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R$ {valor_medio}

Qualquer dúvida, estou à disposição!!

At.te,

Rafael Macedo
"""

# Abrir o navegador e ir para email 
webbrowser.open("www.gmail.com")
time.sleep(3)

# Configurando pause de 3 segundos
pyautogui.PAUSE = 3 

# Clicar no botão escrever
pyautogui.click(x=80, y=207)

# Digitar e-mail do destinátario e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar assunto do email e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar menssagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Clicar no botão enviar
pyautogui.click(x=833, y=708)

# Fechar o gmail
pyautogui.click("ctrl", "f4")

print("Email enviado com sucesso")