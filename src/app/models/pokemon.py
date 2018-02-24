class Pokemon():

    id = int()
    name = string()
    height = int()
    weight= int()
    abilities= []
    types = []

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'abilities': self.abilities,
            'types': self.types,
        }
        return data

    def from_dict(self, data, new_user=False):
        for field in ['id', 'name', 'height', 'weight', 'abilities', 'types']:
            if field in data:
                setattr(self, field, data[field])
