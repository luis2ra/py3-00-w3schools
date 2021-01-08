

class Phone:

    def __init__(
        self,
        debtor_id,
        cod_area,
        phone,
        phone_type,
        rank,
        owner
    ):

        self._debtor_id = debtor_id
        self._cod_area = cod_area
        self._phone = phone
        self._phone_type = phone_type
        self._rank = rank
        self._owner = owner

    @classmethod
    def get_fields(self, should_print=False):

        b = [k for k, v in self.__dict__.items() if isinstance(v, property)]
        if should_print:
            [print(f"attr: {a[0]}") for a in b]
        return b

    @property
    def debtor_id(self):
        return self._debtor_id

    @debtor_id.setter
    def debtor_id(self, debtor_id):
        self._debtor_id = debtor_id

    @property
    def cod_area(self):
        return self._cod_area

    @cod_area.setter
    def cod_area(self, cod_area):
        self._cod_area = cod_area

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def phone_type(self):
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        self._phone_type = phone_type

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner
