from os import path

TWITTER_CONSUMER_KEY ="rtSI6qY8er6klGgPFDwNVSWAA"
TWITTER_CONSUMER_SECRET ="1V2k01WMb5zyI40HQwyBuvr7tPSpqtxoDZhsPRDQiyroV7sfuw"
TWITTER_ACCESS_TOKEN ="174059917-9sEm5laVY7qKt8U3lCi072yvPOtJBVOCRknw4IqL"
TWITTER_ACCESS_TOKEN_SECRET = "QhUcqWk06yonYvRYPLonf4c9E3AloLbxCggzoVKkspUb6"

TWITTER_CURSOR_FILE = path.dirname(__file__) + '/data/twitter_cursor_output.p'
TWITTER_STREAM_FILE = path.dirname(__file__)  + '/data/twitter_stream_output.p'
TWITTER_CLEAN_DATA = path.dirname(__file__)  + '/data/twitter_clean_data.txt'

TWITTER_CUSTOM_STOPWORDS = path.dirname(__file__)  + '/data/custom_stopwords.txt'

STANFORD_NER = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
STANFORD_NER_CON11 = '/usr/share/stanford-ner/classifiers/english.conll.4class.distsim.crf.ser.gz'
STANFORD_NER_MUC7 = '/usr/share/stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz'
STANFORD_NER_JAR = '/usr/share/stanford-ner/stanford-ner.jar'