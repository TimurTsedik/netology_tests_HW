from main import get_name, get_directory, documents, directories, vote, add, solution
import pytest
class TestPytest():
    def test_get_name(self):
        assert get_name("10006") == "Аристарх Павлов"

    def test_get_directory(self):
        assert get_directory("11-2") == 1

    def test_add(self):
        add('international passport', '311 020203', 'Александр Пушкин', 3)
        assert documents[4]['type'] == 'international passport'
        assert documents[4]['number'] == '311 020203'
        assert documents[4]['name'] == 'Александр Пушкин'
        assert directories['3'] == '311 020203'

    @pytest.mark.parametrize('a, b, c, expected', [
        (1, 8, 15, '-3.0 -5.0'),
        (1, -13, 12, '12.0 1.0'),
        (1, 1, 1, 'корней нет'),
    ])
    def test_solution(self, a, b, c, expected):
        assert solution(a, b, c) == expected

    @pytest.mark.parametrize('votes, max_vote', [
        ([1,2,3,2,3,4,3,4,5,4,3,4,5,4,5,6], 4),
        ([1,2,3,2,3,4,3,4,5,4,3,4,5,4,5,6,5], 4),
        ([1,2,3,2,3,4,3,4,5,4,3,4,5,4,5,6,5,6], 4),
        ([1,2,3,2,3,4,3,4,5,4,3,4,5,4,5,6,5,6,6], 4)
    ])
    def test_vote(self, votes: list, max_vote):
        assert vote(votes) == max_vote