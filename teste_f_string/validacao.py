nome_arquivo = "vendas.txt"
caminho = r'C:\Users\user\Downloads'
arquivo = open(f"{caminho}/{nome_arquivo}", "r")
print(arquivo.read())
arquivo.close()
