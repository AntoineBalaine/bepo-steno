# vim: set fileencoding=utf-8 :

# #QYPCTHVRIAEOcsthpr*ieao
KEYS = (
    'P', 'E', 'O', 'V', 'D', 'l', '$', 
    'A', 'U', 'I', 'Y', 'K', 'C', 'T', 'S', 'R', 'N', 'M', 'F', 'n', 
	#'P', 'A', 'E', 'U', 'O', 'I', 'V', 'R', 'N', 'Q', 'Y', 'T', 'c', 's', 't', 'n', 'p', 'r',
	#'i', 'e', 'a', 'o',
	'*', '#'
)
IMPLICIT_HYPHEN_KEYS = KEYS
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
UNDO_STROKE_STENO = ''
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None
KEYMAPS = {
	'Keyboard': {
		'#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'P': 'q',
        'E': 'w',
        'O': 'e',
        '*': 'r',
        'V': 'u',
        'D': 'i',
        'l': 'o',
        '$': 'p',
        'A': 'a',
        'U': 's',
        'I': 'd',
        'Y': 'x',
        'K': ('c', 'b'),
        'C': 'h',
        'T': 'j',
        'S': 'k',
        'R': 'l',
        'N': ';',
        'M': '\'',
        'F': '\\',
        'n': 'n',
#        'P': 'q',
#		'A': 'a',
#		'E': 'w',
#		'U': 's',
#		'O': 'e',
#		'I': 'd',
#		'V': 'r',
#		'R': 'f',
#		'N': 'c',
#		'Q': 'v',
#		'*': ('t', 'g', 'y', 'h'),
#		'Y': 'n',
#		'T': 'm',
#		'c': 'u',
#		's': 'j',
#		't': 'i',
#		'n': 'k',
#		'p': 'o',
#		'r': 'l',
#		'i': 'p',
#		'e': ';',
#		'a': '[', 
#		'o': '\'',
		'arpeggiate': 'space',
		# Suppress adjacent keys to prevent miss-strokes.
		'no-op': ('z', ',', '.', '/', ']'),
	},
}

DICTIONARIES_ROOT = 'asset:plover_bepo:dictionaries'
DEFAULT_DICTIONARIES = (DICTIONARIES_ROOT)
