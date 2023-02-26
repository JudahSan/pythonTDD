# pythonTDD
Python Test Driven Driven Development projects


TDD is a process for writing code that helps you take personal responsibility for the quality of your code.
- The process drives this by having you write the unit tests before the production code. This can seem pretty strange at first but after you’ve used the process for a
while it becomes the norm and you’ll find it hard to write code any other way.
- Even though the tests are written before the production code, that doesn’t mean that ALL the tests are written first. You write one unit test for one test case and
then you write the production code to make it pass.
- The tests and production code are written together with small tests being written and then small bits of production code that make those tests pass. This short
cycle of writing a unit test and then writing the production code to make it pass provides immediate feedback on the code. This feedback is one of the essential features
of TDD.

Benefits of using TDD:

- TDD gives you confidence to make changes in your code because you have a test before you begin that verifies the code is working and will tell you if any of your
changes have broken anything.
- This confidence comes from the immediate feedback the tests provide for each small change in the production code.
- The tests document what the production code is supposed to do. A new developer looking at the code can use the unit tests as a source of documentation for
understanding what the production code is doing.
- Writing the unit tests first helps drive good object oriented design as making individual classes and functions testable in isolation drives the developer to break
dependencies and add interfaces rather than linking concrete implementations together directly.

The TDD workflow is broken up into three phases referred to as the Red Phase, Green Phase, and Refactor phase.
- The first phase is the RED phase. In the RED phase you write a failing unit test for the next bit of functionality you want to implement in the production code.
- Next comes the GREEN phase where you write just enough production code to make the failing unit test pass.
- Last is the REFACTOR phase where you clean up the unit test and the production code to remove any duplication and make sure the code follows your team’s
coding standards and best practices.
- Then you repeat the process for all the functionality you need to implement and all the positive and negative test cases.

- Robert Martin aka “Uncle Bob” created the following Laws of TDD in his book “Clean Code: A Handbook of Agile Software Development”. These laws help ensure
you’re following the TDD process.

- The first law “You may not write any production code until you have first created a failing unit test” follows along with the idea of writing the unit tests first.
Seeing your new unit test fail before you’ve implemented the production is a sign that the unit test has been implemented properly.
- The second law “You may not write more of a unit test than is sufficient to fail” forces you to write only enough of a unit test for the next test case. And the next
test case should always be the simplest test case.
- The last law “You may not write more production code than is sufficient to pass the currently failing unit test” keeps you from writing production code without
any unit test to verify it.
- These three laws help to keep you in a small tight loop of writing a little test that fails, then writing a little production code to make it pass. Each iteration of the loop
should only be a few minutes long and you’re always running the unit tests to verify nothing has gotten broken. If something does get broken you can easily backout
the changes that caused the problem because you implemented them in just the last couple of minutes!

Test Driven Development Best Practices
=

- You should always do the next simplest test case.
- This allows you to gradually increase the complexity of the code, refactoring as you go. This helps keep your code clean and understandable.
- If you jump to the complex cases to quickly you can find yourself stuck writing a lot of code for one test case which breaks the short feedback cycle we look for with
TDD.
- Beyond just slowing you down this can also lead to bad design as you can miss some simple implementations that come from the incremental approach.

Use Descriptive Test Names
-

-  Always use descriptive test names.
- The code is read 1000’s of times more than it’s written as the years go by. Making the code clear and understandable should be the top priority.
- Unit tests are the best documentation for the developers that come after you for how you intended your code to work. If they can’t understand what the unit test is
testing that documentation value is lost.
- Test suites should name the class or function that is under test and the test name should describe the functionality that is being tested.

Keep Test Fast
-

- Keep your unit tests building and running fast.
- One of the biggest benefits of TDD is the fast feedback on how your changes have affected things.
- You lose this if the build and/or execution of your unit tests is taking a long time (i.e. more than a few seconds).
- To help your tests stay fast try to:
  - Keep console output to a minimum (or eliminate it all together). This output just slows down the test and clutters up the test results.
  - Mock out any slow collaborators that are being used with test doubles that are fast.


Use Code Coverage Tools
-

-  Use Code Coverage Analysis Tools
- Once you’ve implemented all your test cases go back and run your unit tests through a code coverage tool.
- It can be surprising some of the areas of your code you’ll miss (especially negative test cases).
- You should have a goal of 100% code coverage on functions with real logic. Don’t waste your time on one line getter and setter functions.

Run Your Tests Multiple Time and In Random Order
-

- - Make sure you run your unit tests multiple times and in a random order.
- Running your tests many times will help ensure that you don’t have any flaky tests that are failing intermittently.
- Running your tests in random order ensures that your tests don’t have dependencies between each other.
- You can use the pytest-random-order plugin to randomize the execution of the tests and pytest-repeat for repeating all or a sub-set of the unit tests as needed

Use a Static Code Analysis Too
-

- - Using a static code analysis tool regularly on your code base is another core requirement for ensuring code quality.
- Pylint is an excellent open source static analysis tool for python that can be used for detecting bugs in your code.
- It can also verify the code is formatted to the team’s standards
- And it can even generate UML diagrams based on it’s analysis
- In the last lecture I’ll review what was gone over in the course and where do go from here.


> [Clean Code: A Handbook of Agile Software Craftmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
> Test Driven Development: By Example - Kent Beck
> Working Effectively with Legacy Code - Michael Feathers