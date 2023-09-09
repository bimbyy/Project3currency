### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python is compiled to bytecode while JavaScript is interpreted. So python is complied and then ran while JavaScript is ran line by line so python in most cases will be faster.
  Python has a larger standard library than JavaScript and has simpler syntax.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

1. If you use get() it will return a default value for C 
2. You can use a conditinal check such as key=c if key in my_dict: value = my_dict[key] else: value = None -----This will check if C exists if not then it will output None and not crash.

- What is a unit test?

A unit test is a form of testing each individual unit or componet of the software to ensure that they work as intended independitly of the other units.

- What is an integration test?

A integration test is a test in which you combine the units or componets to ensure that they work together as intended.

- What is the role of web application framework, like Flask?

To provide a set of tools, libraries and conventions to make building web applications easier. It can handle routing, request and response, url, templates, middleware, database integration, session managment,security, testing, extensions, and scalability help.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Depends on how you want it to look visualy, you would also have to consider Security if the visable url is ok to include or if you dont want the user to know about it. Route paramaters are generally better for security. You would also consider which Libraries you use and their limitations as well as being consistent throughout.

- How do you collect data from a URL placeholder parameter using Flask?

You would define a route with a placeholder and then access that parameter within the route function.

- How do you collect data from the query string using Flask?

You would access the request object that contains the information about the incoming HTTP request.

- How do you collect data from the body of the request using Flask?

using 'request' Usually used in conjunction with POST or PUT.

- What is a cookie and what kinds of things are they commonly used for?

Cookies are data that is sent from the web server to the user and store small data such as preferences and interactions within the webpage. It can be used for session mamangment or analytics or Authentications or Load balancing even.

- What is the session object in Flask?

Allows you to store and have persistant user data across different HTTP requests during a session.

- What does Flask's `jsonify()` do?

It allows you to convert python data structures into JSON format for JavaScript.