# Keira3 Internals

This is a collection of notes aiming to explain the internals of Keira3 for development purposes.

If you just want to *use* Keira3, you don't need any of the following — head to the [Keira3 website](https://www.azerothcore.org/Keira3/) instead.

## Main technologies

Keira3 is built upon the following open source web technologies:

- [**TypeScript**](http://www.typescriptlang.org/) is the main language of Keira3. It is a superset of JavaScript.
  If you know JavaScript and have some basic knowledge of OOP languages like Java and C#, you will feel pretty familiar with TypeScript already.
  Otherwise, you might find [this course](https://www.udemy.com/course/understanding-typescript/) helpful.
  If you don't know JavaScript at all, it would be better to get some basic knowledge first.

- [**Angular**](https://angular.dev/). This is the main framework behind Keira3.
  We absolutely recommend getting familiar with it before getting your hands inside Keira3's code.
  Keira3 uses **modern Angular**: **standalone components** (no NgModules), **OnPush** change detection (enforced via the `@angular-eslint/prefer-on-push-component-change-detection` lint rule), **zoneless** change detection (`provideZonelessChangeDetection()`), **Angular Signals** for reactive state, and the `inject()` function for dependency injection (instead of constructor injection).
  If you are looking for a complete Angular course, we can recommend [this one](https://www.udemy.com/course/the-complete-guide-to-angular-2/).

- [**SCSS**](https://sass-lang.com/) for styling. It's an extension of CSS.
  Knowing the CSS fundamentals is required in order to be able to change the Keira3's interface.

- [**Bootstrap**](https://getbootstrap.com/) is the CSS framework used as a base for Keira3's style.
  You don't have to be a Bootstrap expert, however we recommend being at least familiar with its [Grid system](https://getbootstrap.com/docs/5.3/layout/grid/) and Utilities like [spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/).
  We also use a few **ngx-bootstrap** modules (`Modal`, `Tabs`, `Tooltip`, `Dropdown`) and the `ngx-toastr` library for notifications.

- [**Electron**](https://electronjs.org/) is the software framework that allows building Desktop apps using web technologies.
  The Electron main process lives in the project root (`main.ts` → compiled to `main.js`); the Angular code never talks to `mysql2`/`sqlite3`/`ssh2` directly but through `window.require(...)` guarded by `ElectronService.isElectron()`.

- [**Nx**](https://nx.dev/) is the build system that manages the monorepo and keeps the project modular by dividing it into several libraries.
  Among several features, we leverage the powerful [affected](https://nx.dev/ci/features/affected) command of Nx to run checks (e.g. lint, test, ...) only against the parts of the application that have been modified and those which depend on them.

- [**Squel**](https://hiddentao.com/squel/) is the SQL builder used by `MysqlQueryService` to generate every UPDATE/INSERT/DELETE query Keira3 produces.

- [**@ngx-translate**](https://github.com/ngx-translate/core) powers i18n; translation files live in `apps/keira/src/assets/i18n/*.json`. The language picker is `@keira/shared/switch-language`.

## Testing

We use [test automation](https://en.wikipedia.org/wiki/Test_automation) in Keira3 in our development cycle. For every PR/commit, our CI automatically runs a lot of automated tests.

### Test runner

Keira3 runs unit and integration tests with **[Vitest](https://vitest.dev/)** on top of `@analogjs/vite-plugin-angular`. Every library has its own `vitest.config.ts` that wraps the shared `vitest.base.config.ts` in the workspace root:

```ts
// libs/features/creature/vitest.config.ts
import { createVitestConfig } from '../../../vitest.base.config';

export default createVitestConfig({ coverageDir: 'coverage/libs/features/creature' });
```

Use native Vitest APIs in specs: `vi.fn()`, `vi.spyOn(obj, 'method').mockReturnValue(...)`, `vi.spyOn(obj, 'method').mockImplementation(...)`, `expect.any(...)`, `expect.objectContaining(...)`, `it.skip` / `describe.skip`. For class mocking we use [`ts-mockito`](https://github.com/NagRock/ts-mockito).

### Categories of tests

- **Unit tests** (`*.spec.ts`): run with `npm run test` (which delegates to `nx affected:test`).
  Each unit test mocks all dependencies and asserts the unit's behaviour in isolation.
  We keep **100% coverage** ([this article](https://medium.com/@borzifrancesco/why-i-set-my-unit-test-coverage-threshold-to-100-4c7138276053) explains why). The thresholds (`statements`, `lines`, `branches`, `functions` all at `100`) are enforced in `vitest.base.config.ts`. Submitting untested code will make CI fail.

- **Integration tests** (`*.integration.spec.ts`): also run with `npm run test`, alongside the unit tests.
  Think of these as e2e tests where only the **DB layer** is mocked. They test an editor as a whole: form ↔ service ↔ query generation. They mostly live next to the editor components and follow a **PageObject** pattern via classes exported from `@keira/shared/test-utils`:
  - `PageObject` — base class, wraps `ComponentFixture` via `ngx-page-object-model`;
  - `EditorPageObject<T>` — adds `changeAllFields`, query-output assertions, etc.;
  - `MultiRowEditorPageObject<T>` — adds row-grid helpers (add/edit/delete/select row);
  - `SelectPageObject<T>` — for `Select*` components;
  - `QueryOutputComponentPage`, `translateModule` test helper, miscellaneous DOM helpers in `test-helpers`.

- Components are tested using **Component DOM Testing**. See [this article](https://medium.com/@borzifrancesco/component-dom-testing-in-angular-0d2256414c06) for context.

- **E2E tests** live in `apps/keira-e2e/` and use [Playwright](https://playwright.dev/). Today there is mostly a smoke test that checks the SQLite integration. `npm run e2e` runs them; you need `npm run build:prod` first.

### Why test automation?

Because every time you modify your app, you never know if you are breaking any existing functionality unless you manually test everything again and again. Automated tests don't make you 100% safe, but they catch the obvious regressions.

## File structure

The project is an Nx monorepo with apps in `apps/` and libraries in `libs/`. Library names use the pattern `keira-<scope>-<name>` (e.g. `keira-features-creature`, `keira-shared-utils`). All library path aliases are declared in `tsconfig.base.json` under `@keira/*` (e.g. `@keira/shared/acore-world-model`, `@keira/features/creature`).

### Apps (`apps/`)

- **`apps/keira`** — the main Angular app. Bootstraps in `src/main.ts`, registers global providers (HTTP, translate, hash-based router, toastr, modals, dropdowns, tabs, ui-switch, highlight.js) and binds the routes. The whole route table is in `src/app/routes.ts`. Routing uses **hash location** (`withHashLocation()`) because Electron loads the bundle from `file://`.
- **`apps/keira-e2e`** — Playwright tests for the packaged Electron app.

### Library scopes (`libs/`)

```
app (scope:app-keira)
  └─ main-window (scope:main-window)
       └─ features (scope:features)
            └─ shared (scope:shared)
```

This dependency graph is enforced via the `@nx/enforce-module-boundaries` ESLint rule (see `.eslintrc.json`). A feature can only import from `shared`; `main-window` can import from `features` and `shared`; shared libs can only import from other shared libs.

#### `libs/features/` (scope: `features`)

Each editor "domain" is its own library. A feature **cannot** import anything from another feature — if you need to share something, move it to `libs/shared`. Current features:

`creature`, `quest`, `item`, `gameobject`, `spell`, `smart-scripts`, `conditions`, `gossip`, `trainer`, `texts`, `other-loots`, `dashboard`, `sql-editor`, `game-tele`, `unused-guid-search`.

#### `libs/main/` (scope: `main-window`)

Shell components that aren't tied to a specific feature:

- `connection-window` — the login screen (MySQL credentials, optional SSH tunnel, optional SSL).
- `main-window` — the main shell after a successful login. Contains the sidebar, sidebar items, the routed `<router-outlet />`, the logout button, and the "unsaved" indicator that reads each feature handler's signal.

#### `libs/shared/` (scope: `shared`)

| Library | Purpose |
| --- | --- |
| `acore-world-model` | All TypeScript models for AzerothCore DB rows (entities), plus `options/*` arrays (for dropdowns) and `flags/*` arrays (for bitmasks). New tables get their definition added here first. |
| `base-abstract-classes` | Editor / handler / select base classes (see [Architecture](#architecture-design-and-fundamentals)). |
| `base-editor-components` | Reusable UI building blocks shared by every editor: `TopBarComponent`, `EditorButtonsComponent`, `QueryOutputComponent` (+ `QueryErrorComponent`), `CreateComponent`, `HighlightjsWrapperComponent`, `IconComponent`/`IconService`, `ModalConfirmComponent`. |
| `common-services` | `ElectronService` (wraps `window.require`), `ConfigService` (in-memory app config like debug mode), `LocationService`. |
| `config` | Static configuration: `KEIRA_APP_CONFIG_TOKEN`, Squel config, datatable config, highlight.js config, toastr config, ui-switch config. |
| `constants` | Shared types (`TableRow`, `Option`, `Flag`, `Class`, `StringKeys<T>`, etc.) and project-wide constants (`WIKI_BASE_URL`, `KEIRA3_REPO_URL`, …). |
| `db-layer` | `MysqlService` (mysql2 + ssh2 tunnel), `SqliteService` (read-only SQLite for bundled DBC data), `BaseQueryService`, `MysqlQueryService` (the heart of SQL generation, uses Squel), `SqliteQueryService`. |
| `login-config` | `LoginConfigService` + `LocalStorageService` — persists previously used DB connection profiles (without password). |
| `loot-editor` | The `LootEditorComponent` and `ReferenceViewerComponent` (used by every `*_loot_template` editor). |
| `model-3d-viewer` | The in-app 3D model preview (uses `ZamModelViewer` script + jQuery). |
| `preview` | `PreviewHelperService` and constants used by the tooltip previews (creature, item, quest preview boxes). |
| `sai-editor` | Reusable Smart-AI editor: editor service, comment generator, action/event/target constants, timed action list, sai-top-bar, `SaiHandlerService`. Used both by `smart-scripts` and embedded as a sub-editor in `creature` and `gameobject`. |
| `selectors` | All reusable modal selectors (see [Selectors](#selectors)). |
| `switch-language` | Language picker component + service, used by `connection-window`. |
| `test-utils` | Page Object base classes and helpers used by integration tests. |
| `utils` | Generic helpers: `compareObjFn`, `getNumberOrString`, `getPartial`, `ModelForm` type, `SubscriptionHandler` (base class that auto-unsubscribes in `ngOnDestroy`). |

## Architecture design and fundamentals

Keira3 is structured using [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) with [inheritance](https://www.typescriptlang.org/docs/handbook/classes.html#inheritance) and [generic types](https://www.typescriptlang.org/docs/handbook/generics.html) to maximise code reuse.

The directory `libs/shared/base-abstract-classes/src` contains a collection of abstract classes meant to be extended by concrete Angular [Components](https://angular.dev/guide/components) and [Services](https://angular.dev/guide/di) which implement Keira3 features.

### Class hierarchy

```
SubscriptionHandler (@keira/shared/utils)
├── EditorService<T>                       — generic editor base, holds form + diff/full query state
│   ├── SingleRowEditorService<T>          — one row per entity (UPDATE diff queries)
│   │   └── SingleRowComplexKeyEditorService<T>   — composite primary key
│   ├── MultiRowEditorService<T>           — multiple rows per entity (DELETE+INSERT)
│   │   └── MultiRowComplexKeyEditorService<T>
│   └── MultiRowExternalEditorService<T>   — child editor controlled from a parent
│
├── HandlerService<T>                      — selection state + unsaved signals
│   └── ComplexKeyHandlerService<T>        — composite-key main entity
│
└── SearchService<T>
    └── SelectService<T>                   — base for `Select*Service` classes
        └── (per-feature `Select*Service`)

EditorComponent<T> (Angular)
├── SingleRowEditorComponent<T>
└── MultiRowEditorComponent<T>
    └── LootTemplateComponent<T>           — *_loot_template editors
        └── LootTemplateIdComponent<T>     — loot-template ID variants

SelectComponent<T>                          — base for `Select*Component` classes
SelectComplexKeyComponent<T>                — composite-key variant
```

All of these are exported from `@keira/shared/base-abstract-classes`.

## Keira3 terminology and conventions

### Table types

All definitions of AzerothCore DB tables live in `libs/shared/acore-world-model`:

- `src/entities/*.type.ts` — TypeScript classes for each table row, plus exported `*_TABLE`, `*_ID`, `*_NAME`, `*_SEARCH_FIELDS` constants.
- `src/options/*.ts` — `Option[]` arrays for dropdowns (single-value selectors).
- `src/flags/*.ts` — `Flag[]` arrays for bitmask selectors.

**To add support for a new table, create its definition file here first**, then re-export it from `src/index.ts`.

### The Main Entity

For example, ***Creature*** is a main entity. Whether you want to modify a vendor (`npc_vendor`) or a creature loot (`creature_loot_template`), you still have to select (or create) a Creature first.

There is always a table (and so also an Editor) for the Main Entity. For creatures it's `creature_template`. You can't have an `npc_vendor` row without linking it to an existing entry of `creature_template`.

Another example: you can't have a row in `quest_template_addon` without linking it to an existing row of `quest_template`. Because `quest_template` is the Main Entity of the Quest editors.

Main-entity services set `protected override isMainEntity = true;`.

### Editor

An Editor is typically linked to a table. For example, the ***Creature*** → ***Vendor*** editor allows you to edit the `npc_vendor` table.

There are 2 main types of editors (plus complex-key variants for composite primary keys).

#### Single-row editors

Editors of tables with **one row per entity** (e.g. `creature_template_addon`). Every row is identified by a single primary key — the ID of the selected entity. In the DB those columns have inconsistent names (`id`, `ID`, `entry`, `Entry`, …); in Keira3 we always call this `entityIdField`.

Diffs are generated as `UPDATE … SET … WHERE id = ?` queries by `MysqlQueryService.getUpdateQuery()`.

#### Multi-row editors

Editors of tables with **multiple rows per entity** (e.g. `npc_vendor`). Every row has two keys; in Keira3 we call them `entityIdField` and `entitySecondIdField`. For `npc_vendor`, `entityIdField` is the Creature ID and `entitySecondIdField` is the Item ID. A few tables also need an `_entityExtraIdField` (when the secondary key alone isn't unique).

Diff persistence uses `DELETE … WHERE entityIdField = ?` + `INSERT INTO … VALUES …` so that the whole set of rows for that entity is replaced atomically.

#### Complex-key editors

A few tables (e.g. `smart_scripts`) have composite primary keys (`entryorguid`, `source_type`, `id`). For these we use the **complex-key** variants — `SingleRowComplexKeyEditorService<T>` / `MultiRowComplexKeyEditorService<T>` and `SelectComplexKeyComponent<T>` / `ComplexKeyHandlerService<T>` — which extend the base classes and handle the composite key as an object that gets serialised to JSON.

#### Editor Component and Service

Every Editor has its own Component and Service:

- the **Editor Component** is the "UI part" — typically a thin template binding form controls. Standalone, OnPush.
- the **Editor Service** holds the logic and **state** for the current row(s). It rebuilds the SQL queries (`_diffQuery`, `_fullQuery`) every time the user edits a field, by reacting to `form.valueChanges`.

A concrete single-row Editor Service usually only needs to declare `_entityClass`, `_entityTable`, `_entityIdField` (and optionally `_entityNameField` and `isMainEntity`):

```ts
import { Injectable, inject } from '@angular/core';
import { SingleRowEditorService } from '@keira/shared/base-abstract-classes';
import { CREATURE_TEMPLATE_ID, CREATURE_TEMPLATE_NAME, CREATURE_TEMPLATE_TABLE, CreatureTemplate } from '@keira/shared/acore-world-model';
import { CreatureHandlerService } from '../creature-handler.service';

@Injectable({ providedIn: 'root' })
export class CreatureTemplateService extends SingleRowEditorService<CreatureTemplate> {
  protected override readonly handlerService = inject(CreatureHandlerService);
  protected override _entityClass = CreatureTemplate;
  protected override _entityTable = CREATURE_TEMPLATE_TABLE;
  protected override _entityIdField = CREATURE_TEMPLATE_ID;
  protected override _entityNameField = CREATURE_TEMPLATE_NAME;
  protected override isMainEntity = true;

  constructor() {
    super();
    this.init();
  }
}
```

A multi-row Editor Service additionally declares `_entitySecondIdField` (and optionally `_entityExtraIdField`).

### Handler

Handlers are services that hold cross-editor state for a main entity:

- which entity has been selected (e.g. when you select a Creature, the ID is kept inside `CreatureHandlerService._selected`);
- which editors have unsaved changes — tracked with **Angular Signals** inside `_statusMap[tableName]`, exposed publicly via `is*Unsaved` readonly signals (consumed by the sidebar to show the "unsaved" dot);
- the route guard: handlers are registered as `canActivate` guards on their editor routes — they redirect to `/` when no entity is selected.

A group of editors that refer to the same main entity shares **one Handler**. All Creature editors use `CreatureHandlerService`; all Quest editors use `QuestHandlerService`, and so on. `creature` additionally uses `SaiCreatureHandlerService` for embedded SAI editing.

All Handler classes extend `HandlerService` (or `ComplexKeyHandlerService` for composite-key main entities).

### Select components

Each main entity has a `Select*Component` + `Select*Service` pair (e.g. `SelectQuestComponent` + `SelectQuestService`):

- `Select*Service` extends `SelectService<T>` and only needs to declare `entityTable`, `entityIdField`, optionally `entityNameField`, and a `fieldList` (the searchable fields).
- `Select*Component` extends `SelectComponent<T>` and renders the search form + results table (uses `@siemens/ngx-datatable`). Selecting a row calls `handlerService.select(false, id, name)`.

The "Create new" button (`CreateComponent`) calls `handlerService.select(true, newId)` to enter an editor in "new entity" mode.

## Selectors

Selectors let the user pick a value for a given field without leaving the editor. They appear as the small **`...`** button next to a numeric input:

![image](https://user-images.githubusercontent.com/75517/118693269-351a5000-b80b-11eb-81b5-15065634a5b4.png)

All selector components live in `libs/shared/selectors/src/selectors/` and are exported from `@keira/shared/selectors`.

### SingleValueSelectorBtnComponent

`SingleValueSelectorBtnComponent` lets the user select a **single value** from a list, for a given field. For example, the `exp` field of `creature_template`:

```
0 - Classic
1 - The Burning Crusade
2 - Wrath of The Lich King
```

Define the list as an array of `Option` in `libs/shared/acore-world-model/src/options/`:

```ts
// libs/shared/acore-world-model/src/options/expansion.ts
import { Option } from '@keira/shared/constants';

export const EXPANSION: Option[] = [
  { value: 0, name: 'Classic' },
  { value: 1, name: 'The Burning Crusade' },
  { value: 2, name: 'Wrath of The Lich King' },
];
```

Import the array in the component, expose it as `protected readonly`, and add `SingleValueSelectorBtnComponent` to the standalone component's `imports`:

```ts
import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CreatureTemplate, EXPANSION } from '@keira/shared/acore-world-model';
import { SingleRowEditorComponent } from '@keira/shared/base-abstract-classes';
import { SingleValueSelectorBtnComponent } from '@keira/shared/selectors';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'keira-creature-template',
  templateUrl: './creature-template.component.html',
  imports: [FormsModule, ReactiveFormsModule, SingleValueSelectorBtnComponent /* , ... */],
})
export class CreatureTemplateComponent extends SingleRowEditorComponent<CreatureTemplate> {
  protected readonly EXPANSION = EXPANSION;
  // ...
}
```

Use it in the template via `keira-single-value-selector-btn`:

- `[control]` the form control, e.g. `editorService.form.controls.exp`;
- `[config]` an object specifying `options` and `name`;
- `[modalClass]` optional, the CSS class of the modal (e.g. `modal-md`, `modal-lg`).

```html
<div class="form-group col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">
  <label class="control-label" for="exp">exp</label>
  <keira-single-value-selector-btn
    [control]="editorService.form.controls.exp"
    [config]="{ options: EXPANSION, name: 'exp' }"
    [modalClass]="'modal-md'"
  />
  <input [formControlName]="'exp'" id="exp" type="number" class="form-control form-control-sm" />
</div>
```

Result:

![image](https://user-images.githubusercontent.com/75517/118694803-c1794280-b80c-11eb-9099-00758983ca2e.png){width=300}

![image](https://user-images.githubusercontent.com/75517/118694841-cf2ec800-b80c-11eb-8719-b770a7fd0c98.png){width=500}

### FlagsSelectorBtnComponent

`FlagsSelectorBtnComponent` lets the user compose a value from a set of **flags** (bitmask). If terms like *bits*, *bitmask*, *flags* sound unfamiliar, [this page](https://en.wikipedia.org/wiki/Bit_field) explains them.

Define the list of bits as a `Flag[]` in `libs/shared/acore-world-model/src/flags/`:

```ts
// libs/shared/acore-world-model/src/flags/dynamic-flags.ts
import { Flag } from '@keira/shared/constants';

export const DYNAMIC_FLAGS: Flag[] = [
  { bit: 0, name: 'LOOTABLE' },
  { bit: 1, name: 'TRACK_UNIT - Creature’s location will be seen as a small dot in the minimap' },
  { bit: 2, name: 'TAPPED - Makes creatures name appear grey (Lua_UnitIsTapped)' },
  { bit: 3, name: 'TAPPED_BY_PLAYER - Lua_UnitIsTappedByPlayer usually used by PCVs (Player Controlled Vehicles' },
  { bit: 4, name: 'SPECIALINFO' },
  { bit: 5, name: 'DEAD - Makes the creature appear dead (this DOES NOT make the creature’s name grey or not attack players).' },
  { bit: 6, name: 'REFER_A_FRIEND' },
  { bit: 7, name: 'TAPPED_BY_ALL_THREAT_LIST - Lua_UnitIsTappedByAllThreatList' },
];
```

Bits start from zero. Then expose `DYNAMIC_FLAGS` and import `FlagsSelectorBtnComponent` in the component:

```ts
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CreatureTemplate, DYNAMIC_FLAGS } from '@keira/shared/acore-world-model';
import { SingleRowEditorComponent } from '@keira/shared/base-abstract-classes';
import { FlagsSelectorBtnComponent } from '@keira/shared/selectors';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'keira-creature-template',
  templateUrl: './creature-template.component.html',
  imports: [FlagsSelectorBtnComponent /* , ... */],
})
export class CreatureTemplateComponent extends SingleRowEditorComponent<CreatureTemplate> {
  protected readonly DYNAMIC_FLAGS = DYNAMIC_FLAGS;
  // ...
}
```

Template:

```html
<div class="form-group col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">
  <label class="control-label" for="dynamicflags">dynamicflags</label>
  <keira-flags-selector-btn
    [control]="editorService.form.controls.dynamicflags"
    [disabled]="editorService.form.controls.dynamicflags.disabled"
    [config]="{ flags: DYNAMIC_FLAGS, name: 'dynamicflags' }"
  />
  <input [formControlName]="'dynamicflags'" id="dynamicflags" type="number" class="form-control form-control-sm" />
</div>
```

Inputs:

- `[control]` the form control (e.g. `editorService.form.controls.dynamicflags`);
- `[config]` an object specifying `flags` and `name`;
- `[modalClass]` optional CSS class of the modal.

Result:

![image](https://user-images.githubusercontent.com/75517/118697264-685ede00-b80f-11eb-9609-6b4af903bcdc.png){width=300}

![image](https://user-images.githubusercontent.com/75517/118697333-790f5400-b80f-11eb-8795-cdeae8ebfd64.png)

### Other selectors

There are many other selectors that search either the MySQL world DB or the bundled SQLite DBC data. Find their implementations in `libs/shared/selectors/src/selectors/`:

- `area-selector` — DBC area search.
- `base-selector` — the shared base used by every selector (extends `SearchService`).
- `boolean-option-selector` — quick yes/no toggle as a selector.
- `creature-selector` — search creatures in `creature_template`.
- `faction-selector` — DBC factions.
- `flags-selector` — generic bitmask picker (used by `FlagsSelectorBtnComponent`).
- `game-tele-selector` — teleport locations.
- `gameobject-selector` — search gameobjects in `gameobject_template`.
- `generic-option-selector` — quick dropdown variant.
- `holiday-selector` — DBC holidays.
- `icon-selector` — DBC spell icons.
- `item-enchantment-selector` — DBC item enchantments.
- `item-extended-cost-selector` — DBC item extended cost.
- `item-limit-category-selector` — DBC item limit categories.
- `item-selector` — search items in `item_template`.
- `language-selector` — in-game languages.
- `map-selector` — DBC maps.
- `npc-text-selector` — `npc_text` search.
- `quest-selector` — search quests in `quest_template`.
- `single-value-selector` — generic single-value picker (used by `SingleValueSelectorBtnComponent`).
- `skill-selector` — DBC skills.
- `sound-entries-selector` — DBC sound entries.
- `spell-selector` — DBC spells.

Example: the **item-selector**.

![image](https://user-images.githubusercontent.com/75517/118697495-a2c87b00-b80f-11eb-9db4-69357704d5f5.png)

```html
<div class="form-group col-12 col-sm-6 col-md-4 col-lg-2 col-xl-2">
  <label class="control-label" for="item">
    <keira-icon [itemId]="editorService.form.controls.item.value" />
    item
  </label>
  <keira-item-selector-btn
    [control]="editorService.form.controls.item"
    [disabled]="editorService.form.controls.item.disabled"
    [config]="{ name: 'item' }"
  />
  <input [formControlName]="'item'" id="item" type="number" class="form-control form-control-sm" />
</div>
```

## Database layer

`@keira/shared/db-layer` exposes two service families:

- **`MysqlService`** — wraps `mysql2` (and optionally `ssh2` for SSH tunnels). Holds the live `Connection`, exposes `connectionLost$`, performs reconnection. Only loaded inside Electron (the web preview mode at `npm run ng:serve:web` does not have a real DB).
- **`SqliteService`** — wraps `sqlite3` against a bundled, read-only `.sqlite` file (`KEIRA_APP_CONFIG.sqlitePath`) that ships with the AzerothCore DBC data used by selectors (icons, spells, maps, factions, etc.).

Both expose `dbQuery<T>(queryString)` returning an `Observable<T[]>`.

On top of those, two **query** services build and execute domain SQL:

- **`MysqlQueryService` extends `BaseQueryService`** — the heart of Keira3. Every editor calls into it.
  - `getUpdateQuery<T>(table, idField, currentRow, newRow)` — diffs two row objects and produces a single `UPDATE … SET … WHERE`.
  - `getFullDeleteInsertQuery<T>(table, rows, idField, [secondIdField], [extraIdField])` — produces a `DELETE` followed by `INSERT INTO … VALUES (...)` for multi-row tables.
  - `query<T>(sql)` — runs a custom query.
  - Specialised helpers for quest reward reputation, SAI scripts, max-id lookup, etc.
  - Uses **Squel** (`squel.update(squelConfig).table(...)`, `squel.select(squelConfig).from(...)`, etc.). The `squelConfig` from `@keira/shared/config` standardises the SQL flavour and formatting.
- **`SqliteQueryService`** — reads from the bundled DBC sqlite (areas, factions, holidays, icons, etc.). Heavily used by selectors.

## Application flow

1. Electron boots `main.js` (compiled from `main.ts`) which creates a `BrowserWindow` and loads either `http://localhost:4200` (dev) or `dist/browser/index.html` (prod).
2. Angular bootstraps `AppComponent` (`apps/keira/src/app/app.component.ts`). It mounts `keira-connection-window` (login) until `MysqlService.connectionEstablished === true`, then switches to `keira-main-window`.
3. `MainWindowComponent` renders the sidebar + `<router-outlet />`. Routes live in `apps/keira/src/app/routes.ts`. Most editor routes have `canActivate: [SomeHandlerService]`.
4. A user picks a row via a `Select*Component`, which calls `handlerService.select(...)`. The router navigates to the main editor for that entity.
5. The editor component triggers `editorService.reload(...)`, which reads from MySQL, populates the form, and starts listening to `form.valueChanges` to rebuild diff/full queries on every change.
6. The user clicks "Execute" or "Save" → `editorService.save(...)` runs the diff query against MySQL, then reloads the entity.

## Adding a new editor: a checklist

Use this as a recipe when adding a new editor for a DB table. (Especially useful for AI agents.)

1. **Model the table** in `libs/shared/acore-world-model/src/entities/<table-name>.type.ts`:
  - Export a TypeScript class with public fields matching the DB columns and default values.
  - Export string constants for the table name and key column(s): `<NAME>_TABLE`, `<NAME>_ID`, optionally `<NAME>_NAME`, `<NAME>_SEARCH_FIELDS`.
  - Re-export the file from `libs/shared/acore-world-model/src/index.ts`.

2. **Decide the editor flavour**:
  - One row per main-entity → `SingleRowEditorService<T>` + `SingleRowEditorComponent<T>`.
  - Many rows per main-entity → `MultiRowEditorService<T>` + `MultiRowEditorComponent<T>`.
  - Composite PK → the `*ComplexKey*` variants.
  - `*_loot_template` table → extend `LootTemplateComponent<T>` or `LootTemplateIdComponent<T>`.

3. **Pick a feature library**. If it belongs under an existing main entity (creature, item, quest, …) put it there. Otherwise create a new feature lib under `libs/features/<name>` (mirror `libs/features/game-tele` for a minimal example) and register its tag `"tags": ["scope:features"]` in `project.json`.

4. **Create the service**: extend the right base class, set `_entityClass` / `_entityTable` / `_entityIdField` (and `_entitySecondIdField` for multi-row). Inject the feature's `*HandlerService`. Call `this.init()` in the constructor.

5. **Create the component**: extend the matching base component, inject the service via `editorService` and the `*HandlerService` via `handlerService`. Build the template using `keira-top-bar`, `keira-query-output`, and field inputs (with selectors where appropriate).

6. **Wire up the handler**: add the new `*_TABLE` to the handler's `_statusMap` and expose an `is*Unsaved` signal so the sidebar can show the dot.

7. **Route it**: add the component to `apps/keira/src/app/routes.ts`, with `canActivate: [TheHandlerService]`. Re-export the component from the feature library's `src/index.ts`.

8. **Add the sidebar entry** for the new editor in `libs/main/main-window/src/sidebar/...`.

9. **Tests**: write a `.service.spec.ts` (unit) and a `.integration.spec.ts` (uses a `*PageObject` extending `EditorPageObject`/`MultiRowEditorPageObject`). 100% coverage is enforced — verify with `nx test <project-name>`.

## Tips

- **Path aliases**: imports across libraries always use `@keira/<scope>/<name>` — never relative paths between libs. The full map lives in `tsconfig.base.json`.
- **No NgModules**: every component is `standalone: true` and lists its own `imports: [...]`. If you add a new dependency to a template (a directive, a selector component, a pipe), remember to add it to that `imports` array.
- **OnPush is mandatory** (ESLint enforced). After mutating state from a callback (HTTP, RxJS, etc.) you may need `changeDetectorRef.markForCheck()` — the base `EditorService` already does this in `save`/`reload`.
- **Console rules**: only `console.warn`, `console.info`, `console.error` are allowed (`no-console` rule). Use `ToastrService` for user-facing messages.
- **Module boundaries**: a feature cannot import another feature. If you find yourself wanting to, the code should move to `libs/shared`. Same for shared → only depends on other shared libs.
- **Squel is a global** (`declare const squel: ...`) in `mysql-query.service.ts`. Tests pull it in via the Vitest setup so no extra import is needed.
- **Tests live next to the code**: `foo.service.ts` ↔ `foo.service.spec.ts`. Integration tests use the `.integration.spec.ts` suffix and rely on the Page Object pattern from `@keira/shared/test-utils`.
- **Run only affected projects**: `npm run lint` and `npm run test` use `nx affected:*`. For a single project use `nx lint <name>` / `nx test <name>` (e.g. `nx test keira-features-creature`).
- **Hash routing**: links inside the app should use the router (`routerLink`) — full URLs include a `#` because Electron loads from `file://`.
- **Hot-reload dev**: `npm start` runs `nx serve keira` and Electron together. For pure browser dev (no Electron, no DB) use `npm run ng:serve:web` — the SQLite/MySQL services no-op outside Electron.
- **Coverage threshold is 100%** — code without tests will fail CI. If a branch is genuinely untestable, use `/* istanbul ignore next */` (already used in many places) and justify it.
- **Formatting**: Prettier with 140-char width, single quotes, trailing commas. The `format-staged` script runs via Husky's pre-commit hook.
