from mypackage import myModule

def test_top_n():
    """ make sure top_n works correctly"""

assert myModule.top_n([8,3,7,9],4)==[9,8,7,3],'incorrect'
assert myModule.top_n([8,3,7,9],3)==[9,8,7],'incorrect'
assert myModule.top_n([10,3,7,9],2)==[10,9],'incorrect'