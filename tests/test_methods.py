from ..puzzles import methods as met


class TestMethods:

    def test_txt_opener(self):
        assert met.txt_opener('/../inputs/test_strings_by_commas.txt', ',') == ['first string', 'second string', 'third string', 'last string']
        assert met.txt_opener('/../inputs/test_strings_by_commas.txt', ',') == met.txt_opener('/../inputs/test_strings_by_rows.txt', '\n')

        assert met.txt_opener('/../inputs/test_ints_by_commas.txt', ',') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert met.txt_opener('/../inputs/test_ints_by_commas.txt', ',') == met.txt_opener('/../inputs/test_ints_by_rows.txt', '\n')
