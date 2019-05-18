### [A Generic Client](samples/client.py)

### Requests
1.  Running async requests:

    -   Use asyncio

        ```Python
        def async_request(self, request_methods: [str], paths: [str], data: [], use_rw_key=False):
            async def fetch(session, req_method, url, query):
                async with session.request(method=req_method, url=url, json=query, headers=headers) as response:
                    res_json = await response.json()
                    return res_json

            async def run():
                async with ClientSession() as session:
                    tasks = [fetch(session, request_methods[i], urls[i], queries[i])
                             for i in range(len(request_methods))]
                    responses = await asyncio.gather(*tasks)
                    return responses

            headers = {'Content-Type': 'application/json'}
            loop = asyncio.get_event_loop()
            responses = loop.run_until_complete(run())
            return responses
        ```

    -   It's also possible to group multiple tasks together:
        ```python
        async def run():
            async with ClientSession() as session:
                task1 = asyncio.gather(*[fetch(session, request_methods[i], full_paths[i], data[i])
                         for i in range(len(request_methods))])
                task2 = ...
                task3 = ...
                tasks = [task1, task2, task3]
                responses = await asyncio.gather(*tasks)
                return responses
        ```
