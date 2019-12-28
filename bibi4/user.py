import dataclasses

@dataclasses.dataclass
class User:
    id: int = dataclasses.field(metadata = {'skip': True})
    email: str = dataclasses.field(metadata = {'unique': True, 'description': 'Email address'})
    username: str = dataclasses.field(metadata = {'unique': True, 'description': 'User name'})
    password: str = dataclasses.field(metadata = {'description': 'Password'})
