# AIOPlemmy: a Python package for accessing the Lemmy API asynchronously

<center>
    <img src="img/plemmy.png" alt="drawing" width="325"/>
</center>

[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/tjkessler/plemmy/master/LICENSE.txt)

AIOPlemmy allows you to interact with any Lemmy instance using Python and the [LemmyHttp API](https://join-lemmy.org/api/classes/LemmyHttp.html).

**WARNING:** Plemmy is still in development and needs testing!

## Installation ##

For the most up-to-date version of AIOPlemmy, clone and install from the repository:

```
git clone https://github.com/schicksal-hq/plemmy-aio
cd plemmy
pip3 install .
```

## Basic usage ##

+ Interact with a Lemmy instance using the _LemmyHttp_ object:

```python
import aiohttp
import asyncio
import orjson
from aioplemmy import LemmyHttp, responses

async def main():
    # Unlike in original Plemmy, Plemmy-AIO accepts aiohttp session from outside and relies on developer to set
    # base_url parameter
    sess = aiohttp.ClientSession(base_url="https://lemmy.ml", json_serialize=lambda x: str(orjson.dumps(x)))
    lemmy = LemmyHttp(client=sess, key=None) # login anonymously (as guest, no key)

    # The API requests are async :3
    resp = await lemmy.get_community(name="anime")
    resp = responses.GetCommunityResponse(resp)
    print(resp)

asyncio.run(main())
```

+ Logging in:

```python
import aiohttp
import asyncio
import orjson
from aioplemmy import LemmyHttp, responses

async def main():
    sess = aiohttp.ClientSession(base_url="https://lemmy.ml", json_serialize=lambda x: str(orjson.dumps(x)))
    
    # Use anonymous access to log in
    key = await LemmyHttp(client=sess, key=None).login("test@example.org", "j12345678")
    
    # And then create the LemmyHttp instance you'll actually use.
    # Of course, you can (and should) reuse the same aiohttp session.
    lemmy = LemmyHttp(client=sess, key=key)

    resp = await lemmy.get_community(name="anime")
    resp = responses.GetCommunityResponse(resp)
    print(resp)

asyncio.run(main())
```

+ Catching errors:

```python
import aiohttp
import asyncio
import orjson
from aioplemmy import LemmyHttp, LemmyError, responses

async def main():
    sess = aiohttp.ClientSession(base_url="https://lemmy.ml", json_serialize=lambda x: str(orjson.dumps(x)))
    lemmy = LemmyHttp(client=sess, key=None)

    try:
        resp = await lemmy.get_community(name="nonexistingcommunity")
        resp = responses.GetCommunityResponse(resp)
        print(resp)
    except LemmyError as e:
        # The error code will be in the `error` property
        # Keep in mind that this property will be set if and only if
        # the Lemmy API could generate a response.
        #
        # Unexpected I/O and HTTP errors will trigger LemmyError, but will 
        # not set the property.
        
        print(e.error) # should print COULDNT_FIND COMMUNITY

asyncio.run(main())
```

Full documentation and further API refinements are on their way, but in meantime you should check out source code
and [examples](https://github.com/tjkessler/plemmy/tree/main/examples) from upstream. The method names are essentially the
same after all, and you're unlikely to spot any difference if you just pipe LemmyHttp results to Response objects.
The important differences are:
+ aioplemmy has its LemmyHttp methods all async
+ ...and the methods return objects parsed from JSON response, not response itself
+ ...and methods occasionally throw LemmyError

## Reporting issues, making contributions, etc. ##

Pull requests and issues are welcome. You're also welcome to submit them to the upstream repository, I will pull the fixes from there :)