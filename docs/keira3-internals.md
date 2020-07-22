# Keira3 Internals

This is a collection of notes aiming to explain the internals of Keira3 for development purposes.

If you just want to use Keira3, you don't need any of the following. If you want to modify Keira3, for example to improve it or to add new features, you may find this page useful.

## Main technologies

Keira3 is built upon the following open source web technologies:

- [**TypeScript**](http://www.typescriptlang.org/) is the main language of Keira3. It is a superset of JavaScript. 
If you know JavaScript and have some basic knowledge of OOP languages like Java and C#, you will feel pretty familiar with TypeScript already.
Otherwise you might find [this course](https://www.udemy.com/course/understanding-typescript/) helpful.
If you don't know JavaScript at all, it would be better to get some basic knowledge first.

- [**Angular**](https://angular.io/). This is the main framework behind Keira3. 
We absolutely recommend to get familiar with it before getting your hands inside Keira3's code.
If you are looking for a complete Angular course, we can recommend [this one](https://www.udemy.com/course/the-complete-guide-to-angular-2/).

- We use [**SCSS**](https://sass-lang.com/) to style our UI. It's an extension of CSS.
Knowing the CSS fundamentals is required in order to be able to change the Keira3's interface.
SCSS should be quite intuitive for anyone who can understand CSS.

- [**Bootstrap**](https://getbootstrap.com/) is the CSS framework used as a base for Keira3's style.
You don't have to be a Bootstrap expert, however we recommend to be at least familiar with its [Grid system](https://getbootstrap.com/docs/4.5/layout/grid/) and Utilities like [spacing](https://getbootstrap.com/docs/4.5/utilities/spacing/).

- [**Electron**](https://electronjs.org/) is the software framework that allows building Desktop apps using web technologies.
We don't use many native Electron features so usually you don't have to worry about it when developing Keira3.

## Testing

We use [test automation](https://en.wikipedia.org/wiki/Test_automation) in Keira3 in our development cycle. For every PR/commit, our CI automatically runs a lot of automated tests.

More specifically, we have:

- **Unit tests**. It's all `*.spec.ts` file, they run with `ng test`. We keep **100% coverage**.
  This means that if you try to submit untested code, the CI build of your PR will fail. We use the [Angular testing framework](https://angular.io/guide/testing) for it.

- **Integration tests**. It's all the `*.integration.spec.ts` file, they also run with `ng test`, together with the unit tests.
 You can see the integration tests of Keira3 almost like a set of e2e tests, the main difference is that all the DB interactions are mocked.
 The difference between unit tests and integration test is: in unit tests we test units by mocking all their dependencies, while in integration tests we test "big pieces" of Keira3 together. Mostly used to test the editors.
 
 - **E2E tests**. We have a tiny set of e2e tests based on [Spectron](https://www.electronjs.org/spectron). For example, to check the sqlite integration.
 
 ### Why test automation?
 
 Because every time you modify your app, you never know if you are breaking any existing functionality unless you manually test everything again and again.
 
 When you have automated tests in place, you are still not 100% sure about not breaking existing stuff, but at least they can give you some assurance.

## Architecture design

TODO 
