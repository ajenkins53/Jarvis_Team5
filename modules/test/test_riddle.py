import modules

def test_riddle():
    assert('riddle' == modules.process_query('tell me a riddle')[0])
    assert('riddle' == modules.process_query('Do you know a riddle?')[0])
    assert('riddle' == modules.process_query('random riddle')[0])
    
