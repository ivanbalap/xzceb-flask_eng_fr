from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)

    return frenchText

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)

    return englishText

if __name__ == '__main__':
    mText="I want to watch a movie"
    print(englishToFrench(mText))
    print(frenchToEnglish(englishToFrench(mText)))