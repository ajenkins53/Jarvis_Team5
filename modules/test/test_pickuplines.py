import modules

def test_pickuplines():
    assert('pick up line' == modules.process_query('tell me a pick up line')[0])
    assert('pick up line' == modules.process_query('pick up line')[0])
    assert('pick up line' == modules.process_query('pickup line')[0])
    assert('pick up line' == modules.process_query('give me a pickup line')[0])
    assert('pick up line' == modules.process_query('give me a pick up line')[0])
    assert('pick up line' == modules.process_query('Do you know a pick up line?')[0])
    assert('pick up line' == modules.process_query('random pick up lines')[0])
    assert('pick up line' != modules.process_query('something random')[0])
