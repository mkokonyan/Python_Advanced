class NameNotFound(Exception):
    pass


class MustContainSymbol(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


ALLOWED_DOMAINS = [".com", ".bg", ".net", ".org"]


def validate_email(email):
    if "@" not in email:
        raise MustContainSymbol("Email must contain @")
    username, domain, *rest = email.split("@")
    if len(rest) > 0:
        raise TooManyAtSymbols("The whole email must contain one @ symbol")
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if "." + domain.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")


while True:
    email = input()
    if email == "End":
        break
    validate_email(email)
