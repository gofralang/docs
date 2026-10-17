import pygments.lexers

from gofra_lexer import GofraLexer


def on_config(config, **kwargs):
    pygments.lexers.LEXERS["Gofra"] = (
        "gofra_lexer",
        GofraLexer.name,
        tuple(GofraLexer.aliases),
        tuple(GofraLexer.filenames),
        tuple(GofraLexer.mimetypes),
    )
    return config
