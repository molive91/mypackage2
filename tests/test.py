from mypackage import myModule

def test_top_n():
    """to make sure it works correctly"""

    assert myModule.top_n([8,3,4,5],2) == [8,5], "Incorrect"
    assert myModule.top_n([8,3,4,5],2) == [8,5], "Incorrect"