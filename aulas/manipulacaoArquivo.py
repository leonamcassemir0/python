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
