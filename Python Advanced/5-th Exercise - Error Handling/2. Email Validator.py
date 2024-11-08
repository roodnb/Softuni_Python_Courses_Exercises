class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


min_len_name = 5
tls_names = ['.com', '.bg', '.net', '.org']

while True:
    command = input()
    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = command.split('@')

    if len(name) < min_len_name:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name, tls = domain.split('.')

    if f'.{tls}' not in tls_names:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")