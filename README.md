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

> [Clean Code: A Handbook of Agile Software Craftmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)