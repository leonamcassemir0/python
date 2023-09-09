import os
# Indica qual o sistema operacional
print(os.name)

# Indica se existe o arquivo
print(os.path.exists('dicio.py'))

# Indica se existe o diretório
print(os.path.exists('exemploModulo'))

# Para acessar arquivos em diretórios específicos
print(os.path.exists('exemploModulo/outro.py'))

# Para criar diretórios
os.mkdir('exemplomkdir')
