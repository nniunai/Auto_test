import pytest




def func(a):

    return a+1

@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_a():

    assert func(3) == 5 #失败的

def test_b():

    assert 1 #成功

if __name__ == '__main__':
    pytest.main(["pytest_demo.py"])