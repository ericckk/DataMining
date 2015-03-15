__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

from os import path

TWITTER_CONSUMER_KEY ="rtSI6qY8er6klGgPFDwNVSWAA"
TWITTER_CONSUMER_SECRET ="1V2k01WMb5zyI40HQwyBuvr7tPSpqtxoDZhsPRDQiyroV7sfuw"
TWITTER_ACCESS_TOKEN ="174059917-9sEm5laVY7qKt8U3lCi072yvPOtJBVOCRknw4IqL"
TWITTER_ACCESS_TOKEN_SECRET = "QhUcqWk06yonYvRYPLonf4c9E3AloLbxCggzoVKkspUb6"

TWITTER_CURSOR_FILE = path.dirname(__file__) + '/data/twitter_cursor_output.p'
TWITTER_STREAM_FILE = path.dirname(__file__)  + '/data/twitter_stream_output.p'
TWITTER_CLEAN_DATA = path.dirname(__file__)  + '/data/twitter_clean_data.txt'

TWITTER_CUSTOM_STOPWORDS = path.dirname(__file__)  + '/data/custom_stopwords.txt'
TWITTER_CUSTOM_PHRASES_LEFT = [' is hiring a ', ' is hiring ', ' is looking for a ', ' is looking for ', ' are hiring a ', ' are hiring ', ' opportunity with ',]
TWITTER_CUSTOM_PHRASES_RIGHT = [' needed in ', ' needed ', ' at ', ' with ', ' for ', ' opening at ']

STANFORD_NER = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
STANFORD_NER_JAR = '/usr/share/stanford-ner/stanford-ner.jar'


TWITTER_PUNCTUATION = r"(\w*\?|\w*!|-|;|:|\.|,|\|)"
TWITTER_HASHTAGS = r"#\w*"
TWITTER_ZIPCODE = r"[0-9]*"
TWITTER_MONEY = r"\$\d+\S*"
TWITTER_USERNAME = r"(@\w*|\w*@\w+)"
TWITTER_HYPERLINKS = r"http://\S*|https://\S*"
TWITTER_BRACKETS = r"(\(|\)|\[|\])"
TWITTER_SQUARE_BRACKETS_TEXT = r"\[(.+?)\]"
TWITTER_DASH_SLASH = r"(-|\/|\\)"
TWITTER_CUTOFF = r"\w*\.{3}"
TWITTER_US_STATES = r"((\w* View|\w* City)*\w*, A[LKSZRAEP]|(\w* View|\w* City)*\w*, C[AOT]|(\w* View|\w* City)*\w*, D[EC]|(\w* View|\w* City)*\w*, F[LM]|(\w* View|\w* City)*\w*, G[AU]|(\w* View|\w* City)*\w*, HI|(\w* View|\w* City)*\w*, I[ADLN]|(\w* View|\w* City)*\w*, K[SY]|(\w* View|\w* City)*\w*, LA|M[ADEHINOPST]|(\w* View|\w* City)*\w*, N[CDEHJMVY]|(\w* View|\w* City)*\w*, O[HKR]|(\w* View|\w* City)*\w*, P[ARW]|(\w* View|\w* City)*\w*, RI|(\w* View|\w* City)*\w*, S[CD]|(\w* View|\w* City)*\w*, T[NX]|(\w* View|\w* City)*\w*, UT|(\w* View|\w* City)*\w*, V[AIT]|(\w* View|\w* City)*\w*, W[AIVY])"
TWITTER_LOCATIONS = r"(Ala(bama|ska)|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|District of Columbia|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Miss(issippi|ouri)|Montana|Nebraska|Nevada|New (Hampshire|Jersey|Mexico|York)|North (Carolina|Dakota)|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South (Carolina|Dakota)|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])"

TWITTER_REGEX = [TWITTER_MONEY, TWITTER_HYPERLINKS, TWITTER_HASHTAGS, TWITTER_USERNAME, TWITTER_BRACKETS, TWITTER_SQUARE_BRACKETS_TEXT, TWITTER_US_STATES, TWITTER_CUTOFF, TWITTER_PUNCTUATION, TWITTER_ZIPCODE, ]









