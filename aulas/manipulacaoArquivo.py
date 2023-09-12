# import os
"""
O módulo OS fornece uma forma portátil de usar
funcionalidades dependentes do sistema operacional
"""

# .name fornece o sistema operacional (posix é mac e linux, nt é windows)
"""
print(os.name)
"""

# .path.exists indica se há o arquivo no diretório específico
"""
print(os.path.exists('aulas/casting.py'))
"""

# .mknod cria um arquivo
"""
os.mknod
"""

# .mkdir cria um diretório
"""
os.mkdir('novaPasta')
os.mkdir('aulas/mkdirteste')
"""

# .remove deleta arquivos do diretório atual
"""
os.remove('novaPasta/intro.txt')
"""

# .rmdir deleta diretórios específicos
"""
os.rmdir('novaPasta')
"""

# .rename podemos renomear diretórios ou arquivos
"""
os.rename('aulas/mkdirteste/intro.txt', 'aulas/mkdirteste/teste.txt')
"""

# open() é usado para abrir arquivos txt
"""
arquivo = open('aulas/receita.txt')
arquivo2 = open('aulas/receitas/brigadeiro.txt')
"""

# .read() é usado com o open para ler o arquivo txt
"""
print(arquivo2.read())
"""

# .closed() é usado para fechar o arquivo txt
"""
arquivo2.close()
print(arquivo2.closed)
"""

# Forma pythoniana: with open() as (apelido): {código}
"""
with open('./aulas/receitas/brigadeiro.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)
print(arquivo.closed)
"""

# .write() permite escrever no documento txt, precisa colocar 'w' no open
# 'w' é de write: reescreve sobre o documento
# 'r' é de read: permite somente leitura
# 'a' é de append: permite escrever na última linha, mantendo o arquivo
"""
with open('./aulas/receitas/brigadeiro.txt', 'a') as arquivo:
    arquivo.write('JKjjduuuu')
    arquivo.closed
print(arquivo.closed)
"""
