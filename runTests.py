def runTests(f,tv):
    fname = getattr(f, "__name__", str(f))
    print("Testing", fname, "...")
    triples = ( (args, f(*args), expected) for args, expected in tv )
    failures = [ (i, args, result, expected) for i, (args, result, expected) in enumerate(triples) if expected != result ]
    for i, args, result, expected in failures:
        print("  ["+str(i)+"]",fname+str(args), "==", result, "!=", expected, "(expected)")
    total = len(tv)
    passed = total - len(failures)
    print("passed", passed, "/", total, "tests")
    return (passed, total)