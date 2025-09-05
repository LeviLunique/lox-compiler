import enum

class TokenType(enum.Enum):
    LEFT_PAREN = enum.auto()
    RIGTH_PAREN = enum.auto()
    LEFT_BRACE = enum.auto()
    RIGTH_BRACE = enum.auto()
    COMMA = enum.auto()

type Token = tuple[str, TokenType]

def tokenize(source: str) -> list[Token]:
    scanner = Scanner(source)
    return scanner.scan_tokens()

class Scanner:
    ...
    
    def scan_tokens(self) -> list[Token]:
        ...
        return self.tokens