class UserMail:
    _base = set()

    def __init__(self, login, email):
        self._login = None
        self.login = login
        self.email = email

    def get_login(self):
        return self._login

    def get_email(self):
        return self.__email
    
    def set_login(self, new_login):
        if not isinstance(new_login, str):
            raise TypeError(f"{new_login} не является строкой")
        if new_login in self._base:
            raise ValueError(f"Логин {new_login} уже имеется в системе")

        if self._login:
            self._base.discard(self._login)

        self._login = new_login
        self._base.add(new_login)

    def set_email(self, new_mail: str):
        if isinstance(new_mail, str) and new_mail.count('@') == 1 and '.' in new_mail.split('@')[1]:
            self.__email = new_mail
        else:
            raise ValueError(f'ErrorMail:{new_mail}')  

    email = property(fget=get_email, fset=set_email)

    login = property(fget=get_login, fset=set_login)

