# Design a rate limiter

Questions:
1. What kind of rate limiter are we going to design? Is it a client-side rate limiter or
server-side API rate limiter?
2. Does the rate limiter throttle API requests based on IP, the user ID, or other
properties?
3. What is the scale of the system? Is it built for a startup or a big company with a
large user base?
4. Will the system work in a distributed environment?
5. Is the rate limiter a separate service or should it be implemented in application
code?