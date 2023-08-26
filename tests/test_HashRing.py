from src.HashRing import HashRing


server = "ServerOne"
request = "/api/1230987/info"
response = "{name: Wahab, age: 22}"


def testHashInt():
    hashring = HashRing()
    testKey = "abc123"
    hashInt = hashring.hashInt(testKey)
    assert isinstance(hashInt, int), f"Expected type int, \
            but got {type(hashInt)}"


def testSimpleHashRing():
    cache = HashRing()
    cache.putNode(server)
    cache.putData(request, response)
    assert cache.getData(request) == response, "Data doesn't match"


def testSimpleReplacement():
    cache = HashRing()
    cache.putNode(server)
    cache.putData(request, response)

    serverTwo = "ServerTwo"
    cache.putNode(serverTwo)
    cache.removeNode(server)

    assert cache.getData(request) == response, "Data doesn't match"


def testModerateReplacement():
    cache = HashRing()
    startingServers = ["s1", "s2", "s3"]
    for s in startingServers:
        cache.putNode(s)

    data = [(str(r), str(r)) for r in range(8)]
    for req, res in data:
        cache.putData(req, res)

    newServers = ["s4", "s5", "s6"]
    for s in newServers:
        cache.putNode(s)

    for s in startingServers:
        cache.removeNode(s)

    for req, res in data:
        assert cache.getData(req) == res, "Data does not match"


def testComplexReplacement():
    cache = HashRing()

    # Initially add a number of servers to the hash ring
    initialServers = ["s1", "s2", "s3", "s4", "s5"]
    for s in initialServers:
        cache.putNode(s)

    # Insert a range of data into the hash ring
    initialData = [(str(r), str(r)) for r in range(50)]
    for req, res in initialData:
        cache.putData(req, res)

    # Now, add some new servers and remove some of the initial ones
    newServers = ["s6", "s7", "s8"]
    for s in newServers:
        cache.putNode(s)

    removedServers = ["s2", "s4", "s5"]
    for s in removedServers:
        cache.removeNode(s)

    # Insert some more data after the servers have been replaced
    additionalData = [(str(r+100), str(r+100)) for r in range(20)]
    for req, res in additionalData:
        cache.putData(req, res)

    # Ensure all data (initial and additional) is still accessible
    for req, res in initialData + additionalData:
        assert cache.getData(req) == res, f"Data mismatch for request {req}"

    # Let's now remove all new servers and add back the removed servers
    for s in newServers:
        cache.removeNode(s)

    for s in removedServers:
        cache.putNode(s)

    # Insert some final set of data
    finalData = [(str(r+200), str(r+200)) for r in range(10)]
    for req, res in finalData:
        cache.putData(req, res)

    # Ensure all data (initial, additional, and final) is still accessible
    for req, res in initialData + additionalData + finalData:
        assert cache.getData(req) == res, f"Data mismatch for request {req}"


def testEdgeCases():
    pass


def testInvalidScenarios():
    # Ex: Remove all nodes but without removing data
    pass


def runTests():
    # Test basic HashRing functions
    testHashInt()
    testSimpleHashRing()
    testSimpleReplacement()
    testModerateReplacement()
    testComplexReplacement()

    print("All HashRing tests passing!")


if __name__ == "__main__":
    runTests()
