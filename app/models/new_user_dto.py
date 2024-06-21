class NewUserDto(object):
    def __init__(self, name, location):

        if name is None or location is None:
            raise ValueError("Name/Location required")
        
        self.name = name
        self.location = location