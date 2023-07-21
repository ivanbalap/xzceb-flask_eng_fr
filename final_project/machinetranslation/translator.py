'''
Python package using deep_translator
'''
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    '''
    Function: translating English to French
    '''
    ret_french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)

    return ret_french_text

def frenchToEnglish(french_text):
    '''
    Function: translating French to English
    '''
    ret_english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)

    return ret_english_text

if __name__ == '__main__':
    MY_TEXT="I want to watch a movie"
    print(englishToFrench(MY_TEXT))
    print(frenchToEnglish(englishToFrench(MY_TEXT)))
