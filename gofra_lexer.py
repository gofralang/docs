from pygments.lexer import RegexLexer, words
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Whitespace,
)

__all__ = ["GofraLexer"]


class GofraLexer(RegexLexer):
    name = "Gofra"
    aliases = ["gofra"]  # noqa: RUF012
    filenames = ["*.gf", "*.gofra"]  # noqa: RUF012
    mimetypes = ["text/x-gofra"]  # noqa: RUF012

    statements = (
        "func",
        "end",
        "if",
        "else",
        "while",
        "for",
        "do",
        "return",
        "import",
        "struct",
        "union",
        "inline_raw_asm",
        "pointer_of_proc",
        "offset_of",
        "align_of",
        "const",
        "typecast",
        "lambda",
        "type",
        "var",
    )

    stack_ops = (
        "call",
        "drop",
        "copy",
        "swap",
    )

    attributes = (
        "pub",
        "naked",
        "extern",
        "inline",
        "no_return",
        "reorder",
        "packed",
    )

    constants = (
        "true",
        "false",
    )

    preprocessor = (
        "#include",
        "#endif",
        "#ifdef",
        "#ifndef",
    )

    types = (
        "int",
        "i32",
        "i16",
        "i64",
        "i8",
        "char",
        "bool",
        "void",
        "string",
    )

    tokens = {  # noqa: RUF012
        "root": [
            (r"//.*?$", Comment.Single),
            (r'"', String, "string"),
            (r"\b0x[0-9a-fA-F]+\b", Number.Hex),
            (r"\b\d+\.\d+\b", Number.Float),
            (r"\b\d+\b", Number.Integer),
            (words(preprocessor, suffix=r"\b"), Keyword.Preprocessor),
            (words(attributes, suffix=r"\b"), Keyword.Declaration),
            (words(statements, suffix=r"\b"), Keyword),
            (words(stack_ops, suffix=r"\b"), Name.Builtin),
            (words(constants, suffix=r"\b"), Keyword.Constant),
            (words(types, suffix=r"\b"), Keyword.Type),
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name),
            (r"[+\-*/%<>=!&|^~]+", Operator),
            (r"[\[\]{}(),;:.]", Punctuation),
            (r"\s+", Whitespace),
        ],
        "string": [
            (r'[^"\\]+', String),
            (r"\\.", String.Escape),
            (r'"', String, "#pop"),
        ],
    }
