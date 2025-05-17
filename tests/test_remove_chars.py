from KindleClippings import remove_chars


def test_colon_replacement():
    assert remove_chars('Title: Subtitle') == 'Title - Subtitle'
    assert remove_chars('A:B') == 'A - B'
    assert remove_chars('Multi:part:colon') == 'Multi - part - colon'
    assert remove_chars('Title:Subtitle : Another') == 'Title - Subtitle - Another'


def test_remove_question_and_ampersand():
    assert remove_chars('Where & When?') == 'Where and When'
    assert remove_chars('Q? & A?') == 'Q and A'
    assert remove_chars('This & That & Those') == 'This and That and Those'
    assert remove_chars('??What?') == 'What'
    assert remove_chars(' weird??? &?? ') == 'weird and'


def test_trim_invalid_characters():
    assert remove_chars('???Title???') == 'Title'
    assert remove_chars('!@#My Book!!!') == 'My Book'
    assert remove_chars('Book (Edition)') == 'Book - Edition'

def test_length_limit():
    long_title = 'A' * 300
    assert len(remove_chars(long_title)) == 245
