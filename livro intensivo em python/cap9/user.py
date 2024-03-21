class User:
    def __init__(self, first_name, last_name, *caracteristicas):
        self.nome = first_name
        self.sobrenome = last_name
    attempts = 0

    def describe_user(self):
        print(self.nome)
        print(self.sobrenome)
        print(str(self.attempts))

    def increment_login_attempts(self):
        self.attempts += 1

    def reset_login_attempts(self):
        self.attempts = 0

    def greet_user(self):
        print("Seja bem-vindo!")


class Privilege():
    def __init__(self, elogio=['can add post', 'can delete post', 'can ban user']):
        self.elogio = elogio

    def show_privilege(self):
        print(self.elogio)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()


my_User = Admin('Leonam', 'Cassemiro')
my_User.describe_user()
my_User.privileges.show_privilege()


'''
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


usuario = User("sdfghj", "zsxdcfvgb", "Programador", "Inteligente", "Simpatic")
usuario.describe_user()
usuario.greet_user()

usuario = User("szxdcfvgbhj", "dfghj", "Programador", "Inteligente")
usuario.describe_user()
usuario.greet_user()
'''
