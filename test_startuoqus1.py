import startupqus
import pytest,os



def test_qone():
    a= {1: 'rashi', 2: 'komal', 3: 'varsh', 4: 'harry', 5: 'harly', 6: 'hira', 7: 'none', 8: 'none'}
    b=startupqus.qone()
    assert a==b

def test_passcheck1(capsys):
    input_values = 'harry78-gh@'

    def mock_input(s):
        return input_values.pop(0)

    startupqus.passwd= mock_input
    startupqus.passcheck1()

    out,err= capsys.readouterr()

    assert out == 'Password is valid.'
    assert err == 'Password invalid !!'


def test_passcheck2(capsys):
    input_values = 'harry78-gh'

    def mock_input(s):
        return input_values.pop(0)

    startupqus.passwd= mock_input
    startupqus.passcheck2(input_values)
    startupqus.qtwo()

    out, err = capsys.readouterr()

    assert out == 'Password is valid.'
    assert err == 'Password is invalid.'


def test_logread(tmpdir):
        q=open("access.log")

        p = tmpdir.mkdir("sub").join("access.log")
        p.write("content")
        assert p.read() == "content"
        assert len(tmpdir.listdir()) == 1
        assert 0