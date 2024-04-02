## Caching
In computing, a <b>cache</b> is a hardware or software component that stores data so that future requests for that data can be served faster; the data stored in a [cache](./https://en.wikipedia.org/wiki/Cache_(computing)) might be the result of an earlier computation or copy of data stored elsewhere.
### Learning Objectives
* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have <br><br>

All classes must inherit from `BaseCaching` defined below:<br>

```
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

### Tasks:
[0. Basic dictionary](./0-basic_cache.py)<br>
Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* This caching system doesn’t have limit
* `def put(self, key, item):`
  * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  * If `key` or `item` is `None`, this method should not do anything.
* `def get(self, key):`
  * Must return the value in `self.cache_data` linked to `key`.
  * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`. <br>
```
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$
```

[1. FIFO caching](./1-fifo_cache.py)<br>
Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item):`
  * Must assign to the dictionary `self.cache_data` the item value for the key `key`.
  * If `key` or `item` is `None`, this method should not do anything.
  * If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    * you must discard the first item put in cache (FIFO algorithm)
    * you must print `DISCARD`: with the `key` discarded and following by a new line
* `def get(self, key):`
  * Must return the value in `self.cache_data` linked to `key`.
  * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`. <br>
```
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
simam@DESKTOP-5QTVNRV:~/alx-backend/0x01-caching$
```

[2. LIFO Caching](./2-lifo_cache.py)<br>
Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item):`
  * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  * If `key` or `item` is `None`, this method should not do anything.
  * If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    * you must discard the last item put in cache (LIFO algorithm)
    * you must print `DISCARD:` with the `key` discarded and following by a new line
* `def get(self, key):`
  * Must return the value in `self.cache_data` linked to `key`.
  * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

[3. LRU Caching](./3-lru_cache.py)<br>
Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item):`
  * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  * If `key` or `item` is `None`, this method should not do anything.
  * If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    * you must discard the least recently used item (LRU algorithm)
    * you must print `DISCARD:` with the `key` discarded and following by a new line
* `def get(self, key):`
  * Must return the value in `self.cache_data` linked to `key`.
  * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

[4. MRU Caching](./4-mru_cache.py)<br>
Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item):`
  * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  * If `key` or `item` is `None`, this method should not do anything.
  * If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    * you must discard the most recently used item (MRU algorithm)
    * you must print `DISCARD:` with the `key` discarded and following by a new line
* `def get(self, key):`
  * Must return the value in `self.cache_data` linked to `key`.
  * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

