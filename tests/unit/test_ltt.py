from src import LTT


class TestLTT(object):

    def test_comment_has_keyword_simple(self):
        assert LTT.comment_has_keyword(['keyword'], 'this keyword exists')

    def test_comment_does_not_have_keyword(self):
        assert not LTT.comment_has_keyword(['keyword'], 'this does not exist')

    def test_comment_keyword_start(self):
        assert LTT.comment_has_keyword(['keyword'], 'Keyword at the start')

    def test_comment_keyword_end(self):
        assert LTT.comment_has_keyword(['keyword'], 'end KeYwOrd')

    def test_comment_keyword_with_period(self):
        assert LTT.comment_has_keyword(['keyword'], 'end keyword.')

    def test_comment_keyword_with_exclamation(self):
        assert LTT.comment_has_keyword(['keyword'], 'end keyword!')

    def test_comment_keyword_with_question(self):
        assert LTT.comment_has_keyword(['keyword'], 'end keyword?')

    def test_comment_keyword_with_parenthesis(self):
        assert LTT.comment_has_keyword(['not', 'keyword'], '(keyword)')
