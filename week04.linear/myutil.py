def obj_explore(obj,what='all'):
    '''Lists attributes and methods of a class, arg=all,public,private,methods,properties'''
    import sys # this function will run rarely, so import here
    def trstr(s):
        if isinstance(s, str):
            return s[:30]
        else:
            return s
    def spacer(s):
        return " "*max(15-len(s),2)
    hr='-'*60
    print(obj)
    print('%s\nObject report on object = %r' % (hr,obj))
    cl=type(obj)
    print('Objec class    : %s' % cl)
    print('Parent classes : %r' % cl.__bases__)
    print('Occupied memory: %d bytes' % sys.getsizeof(obj))
    if what in 'all public properties':
        print('PUBLIC PROPERTIES')
        for name in dir(obj):
            attr=getattr(obj,name)
            if not callable(attr) and name[0:2]!='__':
                print('%s = %r %s' % (name+spacer(name),trstr(attr),type(attr)))
    if what in 'all private properties':
        print('PRIVATE PROPERTIES')
        for name in dir(obj):
            attr=getattr(obj,name)
            if not callable(attr) and name[0:2]=='__':
                print('%s = %r %s' % (name+spacer(name),trstr(attr),type(attr)))
    if what in 'all public methods':
        print('PUBLIC METHODS')
        for name in dir(obj):
            attr=getattr(obj,name)
            if callable(attr) and name[0:2]!='__':
                print('%s %s' % (name+spacer(name),type(attr)))
    if what in 'all private methods':
        print('PRIVATE METHODS')
        for name in dir(obj):
            attr=getattr(obj,name)
            if callable(attr) and name[0:2]=='__':
                print('%s %s' % (name+spacer(name),type(attr)))
                