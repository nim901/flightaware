Flightaware
==========

Flightaware is a module that should display flight information from flightaware.com

## Usage:

### get a flight information:
using the get() method will return a 3 tuple dict:

```python
flight_departure, flight_arrival , flight_general = flightaware().get('Flight Name')
```

flight_departure and flight_arrival holds:

```python
'Airport'
'Terminal'
'Time'
'Scheduled Time'
```

And flight_general holds:

```Python
'Name'
'Duration'
'Flight Date'
'Flight Status'
'Flight Aircraft'
```
## Note
This module is nowhere to be complete. it needs optimization and has some bugs, that I'm probably not going to fix.
I've created this while waiting at the air port for my dad's plane to land.

demo.py is a very simple use-case for this module. It uses VeryPrettyTable to display the information in a table form.

```
+-----------------+----------------------------------------------------------+
|   Flight info   |                           Data                           |
+-----------------+----------------------------------------------------------+
|     Duration    |                    1 hours 6 minutes                     |
|   Flight Date   |                 Wednesday, 25 June 2014                  |
| Flight Aircraft |                           E170                           |
|       Name      |                  Compass Airlines 5859                   |
|  Flight Status  | Scheduled (in 9 hours 56 minutes) (Track inbound flight) |
+-----------------+----------------------------------------------------------+
+----------------+------------------------+----------------+-------------------------+
|   Departure    |                        |    Arrival     |                         |
+----------------+------------------------+----------------+-------------------------+
|    Terminal    |        Gate A3         |    Terminal    |         Gate 59         |
|    Airport     | Sacramento Intl (KSMF) |    Airport     | Los Angeles Intl (KLAX) |
| Scheduled Time |        13:40PDT        | Scheduled Time |         14:46PDT        |
|      Time      |        13:50PDT        |      Time      |         14:56PDT        |
+----------------+------------------------+----------------+-------------------------+
```
