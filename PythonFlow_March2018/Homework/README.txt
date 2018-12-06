## Homework 1 ##
- Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden. 
- Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden.
- Implement your own _map function.
  first arg is collection, second arg - callback (mapper) 
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
- Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.

## Homework 2 ##
- Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
  print values using: next, loop
- Implement your own _find function using generator expression.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  generator expression usage required.
- Create iterator from tuple which created using comprehension
  print values using: next, loop
- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be print automatically
- Enjoy!

# Homework 3 ##
- Implement function which copying only duplication lines from one file two other.
  Retrieve path1, path2, new_filename, returns folder system path.
- Implement function which merge two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path.
- Handle IOException, and other possible exceptions.
- Use Exception handling. 
- Enjoy!

# Homework 4 ##
- Implement PhoneBook class.
- use OOP and SOLID 
- Class should be an iterable (interface).
- Class should contain methods: 
  add_contact method (take object: IContact and add it to phone book)
  find_contact method (first match by name)
  remove_contact method (by name)
  add_to_favorites method (take object: IContact and add it to phone book (only if exists))
  call method (take object: IContact and print 'Calling to <contact name>...'])
  recent_calls property (returns recent calls<IContact>)
  favorites property (returns favorites contacts<IContact>)
- add_contact should check contact's number with regex(or other)validator before add it to phone book
  (one validator per phone book instance)
- Enjoy!

## Homework 5 ##
- Implement metaclass which logs class, child class and their instances destruction (dispose).
- Also metaclass should add some method to the class. It could be used at class instance.
- Implement Context Manager which merge two files
  constructor has <path1, path2, mode, new_file_path=None>
  CM has method merge. merge method has optional param (line_numbers=1 - merge line_numbers by line_numbers)
  CM has property new_file_path which returns new file system path
  Use with statement for file merge
  Skip ValueError in __exit__
  log exceptions in __exit__
  handle Exceptions outside CM
- Enjoy MetaClasses and CMs!

## Homework 6 ##
- Implement Singleton metaclass 
  which may be used as metaclass for other classes making their instances Singletons
- Implement Facade pattern for some classes (up to you) (try not to use code from examples :) )
  Especially for Valera: subject - Animals :)
- Implement Factory pattern for some classes (up to you) (try not to use code from examples :) )
- Implement Adapter pattern for some classes (up to you)
- Implement Decorator(pattern, not Python Decorator) to decorate some instance of some class with some functionality
- Read about more patterns!
- Enjoy!

## Homework 7 ##
- All functionality from HW1(functions, classes, etc.) should be covered by tests. 
  Use built-in Python's Unittest framework
- All functionality from HW4(functions, classes, etc.) should be covered by tests. 
  Use Pytest framework
- All scenarios should be described in test cases (positive, negative, etc.)
- Enjoy!

## Homework 8 ##
- Find some RESTful api, f.e. http://jsonplaceholder.typicode.com/ 
  (could be taken from here https://github.com/toddmotto/public-apis)
  Cover this API with tests using pytest, requests lib
  It may be a good idea to use session object, different HTTP methods, custom request headers
  

- Cover some RESTful api with Load tests using Locust.
  (could be taken from here https://github.com/toddmotto/public-apis)
  Implement:
    several locust users
    base user behavior
    several users behaviors which are using base user behavior
    
- Append screenshots with Locust statistics and chart to README file (place it in HW folder)
-Enjoy!


## Homework 9 ##
- Write tests for youtube site
  -open page youtube.com 
  -search some video
  -open first search result
  -assert empty comments

- Use selenium web driver
- Use pytest
- Use PageObject Pattern
- Use OOP paradigm in Tests

-Enjoy!