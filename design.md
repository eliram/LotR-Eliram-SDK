# Design of The One API Python SDK

*The One API Python SDK has the following goals, in order:*
- To be easy to use
- To provide all possible usages
- To be hard to misuse
- To be consistent throw all the different Endpoints.

# Approach 

- Provide a single entry point with a clear definition for all the endpoints.
- Keep code consistent (all endpoints get a list the same and so on)
- make initialization of the code simple as possible


There are few option to do when creating an SDK
one is to create a separated Class for each endpoint, this is more relevant when there is little to no relationship between the endpoints, in our case there is a logic relationship (Movie has quote and so on...)
another approach is to have everything in the same file and just have a simple factory to define supported endpoints (like `list`, `single_object`, ...), this is not a bad approach except that it is harder to test and much harder to read and underhand the code. Still this is a valid approach

I choose to implement an approach that provides a common error and request handling but separates the actual endpoints implementations. I think this is easier to maintain, test, debug and use. It does add some extra boilerplating but I think it is worth it.
