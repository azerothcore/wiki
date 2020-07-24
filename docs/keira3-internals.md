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
 The difference between unit tests and integration test is: in unit tests we test units by mocking all their dependencies, while in integration tests we test "big pieces" of Keira3 together (mocking only the DB). Mostly used to test the editors.
 
 - **E2E tests**. We have a tiny set of e2e tests based on [Spectron](https://www.electronjs.org/spectron). For example, to check the sqlite integration. 
 The command `ng e2e` will automatically serve the app and run the e2e tests.
 
 ### Why test automation?
 
 Because every time you modify your app, you never know if you are breaking any existing functionality unless you manually test everything again and again.
 
 When you have automated tests in place, you are still not 100% sure about not breaking existing stuff, but at least they can give you some assurance.

## Files structure

Relevant directories:

- **e2e**: all e2e test cases, isolated from everything else;

- **src/assets**: images and **global** style files (the components' style files are located in `src/app`);

- **src/app**: source code of the application as well as the unit and integration tests;

- **src/app/config**: app configuration files, like routing and library-specific configurations;

- **src/app/features**: source code of the main Keira3 features (each one isolated from the others). **RULE**: a feature can NOT import anything from another feature.
If something is meant to be shared across features, then it must be placed under `src/app/shared`;

- **src/app/main**: components that don't belong to a specific feature, yet they are isolated. For example, the root component `AppComponent`, the Sidebar, the Login window, etc...

- **src/app/shared**: all kinds of utilities, modules, components, services, abstract classes, testing utilities, etc... that **are meant to be used by more than 1 feature**;

## Architecture design and fundamentals

Keira3 code is structured using [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) with techniques like [inheritance](https://www.typescriptlang.org/docs/handbook/classes.html#inheritance) and [generic types](https://www.typescriptlang.org/docs/handbook/generics.html) to maximise code reuse.

Inside the directory `src/app/shared/abstract` there is a collection of abstract classes that are meant to be extended by the concrete Angular [Components](https://angular.io/guide/architecture-components) and [Services](https://angular.io/guide/architecture-services) which will implement the Keira3 features.

*If you are not familiar with the terminology used so far, please check the above hyperlinks before proceeding.*

Keira3 is [**modular**](https://en.wikipedia.org/wiki/Modular_programming), you can see it as a collection of features and shared utilities that are organised into [Angular Modules](https://angular.io/guide/architecture-modules).

## Keira3 terminology and conventions

Typically, Keira3 features are caraterised by the following elements.

### The Main Entity

For example ***Creature*** is a main entity. Whether you want to modify a vendor (`npc_vendor`) or a loot of a creature (`creature_loot_template`), you still have to select (or create) a Creature.

There is always a table (and so also an Editor) for the Main Entity. For creatures it's `creature_template`.

You can't have a vendor, loot, etc... without having a creature first. In other words, you can't have an `npc_vendor` row without linking it to an existing entry of `creature_template`.

Another example could be: you can't have a row in `quest_template_addon` without linking it to an existing row of `quest_template`. Because `quest_template` is the Main Entity of the Quest editors.

### Editor

An Editor is typically linked to a table. For example, the ***Creature*** -> ***Trainer*** editor allows you to edit the `npc_trainer` table.

There are 2 main types of Editors in Keira3:

#### Single-row editors

They are the editors of tables containing **ONE row for each entity**.

For example, the table `creature_template_addon` can have only ONE row for each creature. You can never have 2 rows pointing to the same creature in this table.

Every row is uniquely identified by a primary key, that is the ID of the selected entity. Typically in the DB they are called `id`, `ID`, `entry`, `Entry`, etc... yes, they are completely inconsistent, but that's what we inherited from MaNGOS/TrinityCore. In Keira3 we call it just `entityIdField`.

#### Multi-row editors

They are the editors containing **MULTIPLE rows for each entity**.

For example, the table `npc_vendor` can have multiple rows that belongs to the same Creature. Every row of `npc_vendor` represents a specific Item that is sold by a specific Creature. And a Creature can sell 0, 1 or many items. Then every Creature can have 0, 1 or many rows in the `npc_vendor` table. Makes sense right?

Every row has 2 primary keys, typically (but not always) called `id` and `guid`. In Keira3 we always call them `entityIdField` and 
`entitySecondIdField`. The `entityIdField` is the ID of the selected entity.

Back to the example of `npc_vendor`:

- `entityIdField` would be the ID of the Creature
- `entitySecondIdField` would be the ID of the Item

#### Editor's Component and Service

Every Editor in Keira3 has its own [Component](https://angular.io/guide/architecture-components) and [Service](https://angular.io/guide/architecture-services) counterparts, where:

- you can see an **Editor Component** as the "UI part" of the Editor. It reflects the status of the table being edited and contains a form that allows the user to change its properties. Components are typically "dumb" (without much logic code) and are mostly about the HTML code. Of course it's linked to the Editor Service;

- the **Editor Service** contains all the logic that powers an Editor, as well as the **status** for the current table being edited. It's responsible for calling the `QueryService` whenever the user edits any property in order to re-generate the SQL queries.

In order to maximise code reuse, the following abstract classes have been created:

- `EditorService`: base of all Editor Services;
- `SingleRowEditorService`: extends `EditorService`, base of all Single-row Editor Services (e.g. `CreatureTemplateService` extends this class);
- `MultiRowEditorService`: extends `EditorService`, base of all Multi-row Editor Services (e.g. `CreatureLootTemplateService` extends this class);

- `EditorComponent`: base of all Editor Components
- `SingleRowEditorComponent`: extends `EditorComponent`, base of all Single-row Editor Components (e.g. `CreatureTemplateComponent` extends this class);
- `MultiRowEditorComponent`: extends `EditorComponent`, base of all Multi-row Editor Components (e.g. `CreatureLootTemplateComponent` extends this class);

