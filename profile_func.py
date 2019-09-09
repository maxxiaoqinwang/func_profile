import cProfile, io, pstats

def profile_dec(func):
    '''
    A decorator use cProfile to profile function
    '''
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        results = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return results
    return inner

