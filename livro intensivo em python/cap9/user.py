class User:
    def __init__(self, first_name, last_name, *caracteristicas):
        self.nome = first_name
        self.sobrenome = last_name
        self.caracter = caracteristicas
    attempts = 0

    def describe_user(self):
        print(self.nome)
        print(self.sobrenome)
        print(self.caracter)
        print(str(self.attempts))

    def increment_login_attempts(self):
        self.attempts += 1

    def reset_login_attempts(self):
        self.attempts = 0

    def greet_user(self):
        print("Seja bem-vindo!")


usuario = User("Leonam", "Cassemiro", "Programador", "Inteligente", "Simpatic")
usuario.describe_user()
usuario.greet_user()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.describe_user()
usuario.reset_login_attempts()
usuario.describe_user()

'''
usuario = User("sdfghj", "zsxdcfvgb", "Programador", "Inteligente", "Simpatic")
usuario.describe_user()
usuario.greet_user()

usuario = User("szxdcfvgbhj", "dfghj", "Programador", "Inteligente")
usuario.describe_user()
usuario.greet_user()
'''
