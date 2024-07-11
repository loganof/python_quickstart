"""
if not var is True, when var is:
1. False
2. None
3. nil value(0, 0.0, 0j)
4. empty sequence('', [], {}, set())

if var is None, when var is:
1. None

"""
var = False
if not var:
    print(f"var type: {type(var)}")
    
var = None
if not var:
    print(f"var type: {type(var)}")
    
var = 0
if not var:
    print(f"var type: {type(var)}")
    
var = set()
if not var:
    print(f"var type: {type(var)}")
