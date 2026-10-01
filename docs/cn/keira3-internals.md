# Keira3 内部机制

这是一组旨在解释 Keira3 内部机制以供开发用途的笔记。

如果你只是想*使用* Keira3，你不需要以下任何内容 —— 请前往 [Keira3 网站](https://www.azerothcore.org/Keira3/)。

## 主要技术

Keira3 构建于以下开源 Web 技术之上：

- [**TypeScript**](http://www.typescriptlang.org/) 是 Keira3 的主要语言。它是 JavaScript 的超集。
  如果你了解 JavaScript，并且具备一些 OOP 语言（如 Java 和 C#）的基础知识，你使用 TypeScript 时就会感到相当熟悉。
  否则，你可能会发现[这门课程](https://www.udemy.com/course/understanding-typescript/)有所帮助。
  如果你完全不了解 JavaScript，最好先获取一些基础知识。

- [**Angular**](https://angular.dev/)。这是 Keira3 背后的主要框架。
  我们强烈建议在接触 Keira3 的代码之前先熟悉它。
  Keira3 使用**现代 Angular**：**独立组件**（standalone components，无 NgModules）、**OnPush** 变更检测（通过 `@angular-eslint/prefer-on-push-component-change-detection` lint 规则强制）、**无 zone** 变更检测（`provideZonelessChangeDetection()`）、用于响应式状态的 **Angular Signals**，以及用于依赖注入的 `inject()` 函数（而非构造函数注入）。
  如果你在寻找一门完整的 Angular 课程，我们可以推荐[这门](https://www.udemy.com/course/the-complete-guide-to-angular-2/)。

- [**SCSS**](https://sass-lang.com/) 用于样式。它是 CSS 的扩展。
  了解 CSS 基础是修改 Keira3 界面所必需的。

- [**Bootstrap**](https://getbootstrap.com/) 是作为 Keira3 样式基础的 CSS 框架。
  你不必成为 Bootstrap 专家，但我们建议至少熟悉它的[栅格系统](https://getbootstrap.com/docs/5.3/layout/grid/)以及诸如[间距](https://getbootstrap.com/docs/5.3/utilities/spacing/)之类的工具类。
  我们还使用了几个 **ngx-bootstrap** 模块（`Modal`、`Tabs`、`Tooltip`、`Dropdown`）以及用于通知的 `ngx-toastr` 库。

- [**Electron**](https://electronjs.org/) 是允许使用 Web 技术构建桌面应用的软件框架。
  Electron 主进程位于项目根目录（`main.ts` → 编译为 `main.js`）；Angular 代码从不直接与 `mysql2`/`sqlite3`/`ssh2` 通信，而是通过由 `ElectronService.isElectron()` 保护的 `window.require(...)` 进行。

- [**Nx**](https://nx.dev/) 是管理 monorepo 的构建系统，通过将项目划分为多个库来保持其模块化。
  在众多功能中，我们利用 Nx 强大的 [affected](https://nx.dev/ci/features/affected) 命令，仅针对应用程序中被修改的部分以及依赖于它们的部分运行检查（例如 lint、test 等）。

- [**Squel**](https://hiddentao.com/squel/) 是 `MysqlQueryService` 用于生成 Keira3 产生的所有 UPDATE/INSERT/DELETE 查询的 SQL 构建器。

- [**@ngx-translate**](https://github.com/ngx-translate/core) 驱动 i18n；翻译文件位于 `apps/keira/src/assets/i18n/*.json`。语言选择器是 `@keira/shared/switch-language`。

## 测试

我们在开发周期中使用 [测试自动化](https://en.wikipedia.org/wiki/Test_automation)。对于每个 PR/提交，我们的 CI 都会自动运行大量自动化测试。

### 测试运行器

Keira3 使用 **[Vitest](https://vitest.dev/)** 在 `@analogjs/vite-plugin-angular` 之上运行单元测试和集成测试。每个库都有自己的 `vitest.config.ts`，它包装了工作区根目录中的共享 `vitest.base.config.ts`：

```ts
// libs/features/creature/vitest.config.ts
import { createVitestConfig } from '../../../vitest.base.config';

export default createVitestConfig({ coverageDir: 'coverage/libs/features/creature' });
```

在测试（spec）中使用原生 Vitest API：`vi.fn()`、`vi.spyOn(obj, 'method').mockReturnValue(...)`、`vi.spyOn(obj, 'method').mockImplementation(...)`、`expect.any(...)`、`expect.objectContaining(...)`、`it.skip` / `describe.skip`。对于类模拟，我们使用 [`ts-mockito`](https://github.com/NagRock/ts-mockito)。

### 测试类别

- **单元测试**（`*.spec.ts`）：通过 `npm run test` 运行（它会委托给 `nx affected:test`）。
  每个单元测试都会模拟所有依赖项，并独立断言该单元的行为。
  我们保持 **100% 覆盖率**（[这篇文章](https://medium.com/@borzifrancesco/why-i-set-my-unit-test-coverage-threshold-to-100-4c7138276053)解释了原因）。阈值（`statements`、`lines`、`branches`、`functions` 均为 `100`）在 `vitest.base.config.ts` 中强制执行。提交未经测试的代码会导致 CI 失败。

- **集成测试**（`*.integration.spec.ts`）：也通过 `npm run test` 与单元测试一起运行。
  可以将它们视为仅模拟了 **DB 层** 的 e2e 测试。它们整体测试一个编辑器：表单 ↔ 服务 ↔ 查询生成。它们大多位于编辑器组件旁边，并通过从 `@keira/shared/test-utils` 导出的类遵循 **PageObject** 模式：
  - `PageObject` —— 基类，通过 `ngx-page-object-model` 包装 `ComponentFixture`；
  - `EditorPageObject<T>` —— 添加 `changeAllFields`、查询输出断言等；
  - `MultiRowEditorPageObject<T>` —— 添加行网格辅助方法（添加/编辑/删除/选择行）；
  - `SelectPageObject<T>` —— 用于 `Select*` 组件；
  - `QueryOutputComponentPage`、`translateModule` 测试辅助、`test-helpers` 中的各种 DOM 辅助函数。

- 组件使用 **组件 DOM 测试** 进行测试。背景请参见[这篇文章](https://medium.com/@borzifrancesco/component-dom-testing-in-angular-0d2256414c06)。

- **E2E 测试**位于 `apps/keira-e2e/`，使用 [Playwright](https://playwright.dev/)。目前主要是一个检查 SQLite 集成的冒烟测试。`npm run e2e` 运行它们；你需要先运行 `npm run build:prod`。

### 为什么要测试自动化？

因为每次你修改应用时，除非一遍又一遍地手动测试所有内容，否则你永远不知道是否破坏了任何现有功能。自动化测试不能让你 100% 安全，但它们能捕获明显的回归问题。

## 文件结构

该项目是一个 Nx monorepo，应用位于 `apps/`，库位于 `libs/`。库名称使用 `keira-<scope>-<name>` 模式（例如 `keira-features-creature`、`keira-shared-utils`）。所有库路径别名都在 `tsconfig.base.json` 中以 `@keira/*` 声明（例如 `@keira/shared/acore-world-model`、`@keira/features/creature`）。

### 应用（`apps/`）

- **`apps/keira`** —— 主 Angular 应用。在 `src/main.ts` 中启动，注册全局提供者（HTTP、translate、基于 hash 的路由器、toastr、modals、dropdowns、tabs、ui-switch、highlight.js）并绑定路由。整个路由表在 `src/app/routes.ts` 中。路由使用 **hash 定位**（`withHashLocation()`），因为 Electron 从 `file://` 加载 bundle。
- **`apps/keira-e2e`** —— 针对打包后的 Electron 应用的 Playwright 测试。

### 库作用域（`libs/`）

```
app (scope:app-keira)
  └─ main-window (scope:main-window)
       └─ features (scope:features)
            └─ shared (scope:shared)
```

此依赖图通过 `@nx/enforce-module-boundaries` ESLint 规则强制执行（参见 `.eslintrc.json`）。一个 feature 只能从 `shared` 导入；`main-window` 可以从 `features` 和 `shared` 导入；shared 库只能从其他 shared 库导入。

#### `libs/features/`（scope: `features`）

每个编辑器"领域"都是自己的库。一个 feature **不能**从另一个 feature 导入任何内容 —— 如果你需要共享某些东西，请将其移到 `libs/shared`。当前 feature 有：

`creature`、`quest`、`item`、`gameobject`、`spell`、`smart-scripts`、`conditions`、`gossip`、`trainer`、`texts`、`other-loots`、`dashboard`、`sql-editor`、`game-tele`、`unused-guid-search`。

#### `libs/main/`（scope: `main-window`）

不绑定到特定 feature 的壳（shell）组件：

- `connection-window` —— 登录界面（MySQL 凭据、可选 SSH 隧道、可选 SSL）。
- `main-window` —— 成功登录后的主壳。包含侧边栏、侧边栏项目、路由后的 `<router-outlet />`、注销按钮，以及读取每个 feature 处理器信号的"未保存"指示器。

#### `libs/shared/`（scope: `shared`）

| 库 | 用途 |
| --- | --- |
| `acore-world-model` | AzerothCore DB 行（实体）的所有 TypeScript 模型，外加 `options/*` 数组（用于下拉框）和 `flags/*` 数组（用于位掩码）。新表首先在这里添加其定义。 |
| `base-abstract-classes` | 编辑器/处理器/选择器基类（参见 [架构](#architecture-design-and-fundamentals)）。 |
| `base-editor-components` | 每个编辑器共享的可复用 UI 构建块：`TopBarComponent`、`EditorButtonsComponent`、`QueryOutputComponent`（+ `QueryErrorComponent`）、`CreateComponent`、`HighlightjsWrapperComponent`、`IconComponent`/`IconService`、`ModalConfirmComponent`。 |
| `common-services` | `ElectronService`（包装 `window.require`）、`ConfigService`（内存中的应用配置，如调试模式）、`LocationService`。 |
| `config` | 静态配置：`KEIRA_APP_CONFIG_TOKEN`、Squel 配置、datatable 配置、highlight.js 配置、toastr 配置、ui-switch 配置。 |
| `constants` | 共享类型（`TableRow`、`Option`、`Flag`、`Class`、`StringKeys<T>` 等）以及项目级常量（`WIKI_BASE_URL`、`KEIRA3_REPO_URL`、…）。 |
| `db-layer` | `MysqlService`（mysql2 + ssh2 隧道）、`SqliteService`（用于打包 DBC 数据的只读 SQLite）、`BaseQueryService`、`MysqlQueryService`（SQL 生成的核心，使用 Squel）、`SqliteQueryService`。 |
| `login-config` | `LoginConfigService` + `LocalStorageService` —— 持久化之前使用过的 DB 连接配置（不含密码）。 |
| `loot-editor` | `LootEditorComponent` 和 `ReferenceViewerComponent`（被每个 `*_loot_template` 编辑器使用）。 |
| `model-3d-viewer` | 应用内的 3D 模型预览（使用 `ZamModelViewer` 脚本 + jQuery）。 |
| `preview` | `PreviewHelperService` 以及提示预览（生物、物品、任务预览框）使用的常量。 |
| `sai-editor` | 可复用的 Smart-AI 编辑器：编辑器服务、注释生成器、动作/事件/目标常量、定时动作列表、sai-top-bar、`SaiHandlerService`。同时被 `smart-scripts` 使用，并作为子编辑器嵌入到 `creature` 和 `gameobject` 中。 |
| `selectors` | 所有可复用的模态选择器（参见 [选择器](#selectors)）。 |
| `switch-language` | 语言选择器组件 + 服务，由 `connection-window` 使用。 |
| `test-utils` | 集成测试使用的 Page Object 基类和辅助函数。 |
| `utils` | 通用辅助函数：`compareObjFn`、`getNumberOrString`、`getPartial`、`ModelForm` 类型、`SubscriptionHandler`（在 `ngOnDestroy` 中自动取消订阅的基类）。 |

## 架构设计与基础 {#architecture-design-and-fundamentals}

Keira3 使用 [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming)、[继承](https://www.typescriptlang.org/docs/handbook/classes.html#inheritance) 和[泛型类型](https://www.typescriptlang.org/docs/handbook/generics.html)进行结构化，以最大化代码复用。

目录 `libs/shared/base-abstract-classes/src` 包含一组抽象类，供实现 Keira3 feature 的具体 Angular [组件](https://angular.dev/guide/components)和[服务](https://angular.dev/guide/di)继承。

### 类层次结构

```
SubscriptionHandler (@keira/shared/utils)
├── EditorService<T>                       — 通用编辑器基类，持有表单 + diff/full 查询状态
│   ├── SingleRowEditorService<T>          — 每个实体一行（UPDATE diff 查询）
│   │   └── SingleRowComplexKeyEditorService<T>   — 复合主键
│   ├── MultiRowEditorService<T>           — 每个实体多行（DELETE+INSERT）
│   │   └── MultiRowComplexKeyEditorService<T>
│   └── MultiRowExternalEditorService<T>   — 由父级控制的子编辑器
│
├── HandlerService<T>                      — 选择状态 + 未保存信号
│   └── ComplexKeyHandlerService<T>        — 复合键主实体
│
└── SearchService<T>
    └── SelectService<T>                   — `Select*Service` 类的基类
        └── （各 feature 的 `Select*Service`）

EditorComponent<T> (Angular)
├── SingleRowEditorComponent<T>
└── MultiRowEditorComponent<T>
    └── LootTemplateComponent<T>           — *_loot_template 编辑器
        └── LootTemplateIdComponent<T>     — loot-template ID 变体

SelectComponent<T>                          — `Select*Component` 类的基类
SelectComplexKeyComponent<T>                — 复合键变体
```

所有这些都从 `@keira/shared/base-abstract-classes` 导出。

## Keira3 术语与约定

### 表类型

AzerothCore DB 表的所有定义都位于 `libs/shared/acore-world-model`：

- `src/entities/*.type.ts` —— 每个表行的 TypeScript 类，外加导出的 `*_TABLE`、`*_ID`、`*_NAME`、`*_SEARCH_FIELDS` 常量。
- `src/options/*.ts` —— 用于下拉框（单值选择器）的 `Option[]` 数组。
- `src/flags/*.ts` —— 用于位掩码选择器的 `Flag[]` 数组。

**要添加对一张新表的支持，请先在此处创建其定义文件**，然后从 `src/index.ts` 重新导出它。

### 主实体（Main Entity）

例如，***Creature***（生物）是一个主实体。无论你是想修改一个商人（`npc_vendor`）还是一个生物掉落（`creature_loot_template`），你都必须先选择（或创建）一个 Creature。

总是有一个表（也因此有一个编辑器）对应主实体。对于生物来说它就是 `creature_template`。你不能在没有将其关联到 `creature_template` 的现有 entry 的情况下拥有 `npc_vendor` 行。

另一个例子：你不能在没有将其关联到 `quest_template` 的现有行的情况下拥有 `quest_template_addon` 行。因为 `quest_template` 是 Quest 编辑器的主实体。

主实体服务会设置 `protected override isMainEntity = true;`。

### 编辑器（Editor）

一个编辑器通常关联到一张表。例如，***Creature*** → ***Vendor***（商人）编辑器允许你编辑 `npc_vendor` 表。

有 2 种主要类型的编辑器（外加用于复合主键的复合键变体）。

#### 单行编辑器

针对**每个实体一行**的表（例如 `creature_template_addon`）的编辑器。每一行都由一个单一主键标识 —— 即所选实体的 ID。在数据库中这些列的名称不一致（`id`、`ID`、`entry`、`Entry`、…）；在 Keira3 中我们总是将其称为 `entityIdField`。

Diff 由 `MysqlQueryService.getUpdateQuery()` 生成为 `UPDATE … SET … WHERE id = ?` 查询。

#### 多行编辑器

针对**每个实体多行**的表（例如 `npc_vendor`）的编辑器。每一行都有两个键；在 Keira3 中我们称之为 `entityIdField` 和 `entitySecondIdField`。对于 `npc_vendor`，`entityIdField` 是生物 ID，`entitySecondIdField` 是物品 ID。少数表还需要一个 `_entityExtraIdField`（当副键单独不唯一时）。

Diff 持久化使用 `DELETE … WHERE entityIdField = ?` + `INSERT INTO … VALUES …`，以便该实体的整组行被原子地替换。

#### 复合键编辑器

少数表（例如 `smart_scripts`）具有复合主键（`entryorguid`、`source_type`、`id`）。对于这些表，我们使用 **complex-key** 变体 —— `SingleRowComplexKeyEditorService<T>` / `MultiRowComplexKeyEditorService<T>` 以及 `SelectComplexKeyComponent<T>` / `ComplexKeyHandlerService<T>` —— 它们扩展了基类，并将复合键作为一个被序列化为 JSON 的对象处理。

#### 编辑器组件与服务

每个编辑器都有自己的组件和服务：

- **编辑器组件**是"UI 部分" —— 通常是一个绑定表单控件的薄模板。独立组件、OnPush。
- **编辑器服务**持有当前行的逻辑和**状态**。它通过响应 `form.valueChanges`，在用户每次编辑字段时重建 SQL 查询（`_diffQuery`、`_fullQuery`）。

一个具体的单行编辑器服务通常只需声明 `_entityClass`、`_entityTable`、`_entityIdField`（以及可选的 `_entityNameField` 和 `isMainEntity`）：

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

一个多行编辑器服务还需要声明 `_entitySecondIdField`（以及可选的 `_entityExtraIdField`）。

### 处理器（Handler）

Handler 是持有主实体跨编辑器状态的服务：

- 已选择了哪个实体（例如当你选择一个 Creature 时，该 ID 保存在 `CreatureHandlerService._selected` 中）；
- 哪些编辑器有未保存的更改 —— 通过 `_statusMap[tableName]` 内的 **Angular Signals** 跟踪，并通过只读的 `is*Unsaved` 信号公开（侧边栏通过它显示"未保存"圆点）；
- 路由守卫：handler 被注册为其编辑器路由上的 `canActivate` 守卫 —— 当未选择实体时，它们会重定向到 `/`。

引用同一主实体的一组编辑器共享**一个 Handler**。所有 Creature 编辑器使用 `CreatureHandlerService`；所有 Quest 编辑器使用 `QuestHandlerService`，依此类推。`creature` 另外使用 `SaiCreatureHandlerService` 进行嵌入式 SAI 编辑。

所有 Handler 类都扩展 `HandlerService`（对于复合键主实体则为 `ComplexKeyHandlerService`）。

### 选择组件（Select components）

每个主实体都有一对 `Select*Component` + `Select*Service`（例如 `SelectQuestComponent` + `SelectQuestService`）：

- `Select*Service` 扩展 `SelectService<T>`，只需声明 `entityTable`、`entityIdField`、可选的 `entityNameField` 以及 `fieldList`（可搜索字段）。
- `Select*Component` 扩展 `SelectComponent<T>`，渲染搜索表单 + 结果表（使用 `@siemens/ngx-datatable`）。选择一行会调用 `handlerService.select(false, id, name)`。

"创建新项"按钮（`CreateComponent`）调用 `handlerService.select(true, newId)`，以"新实体"模式进入编辑器。

## 选择器（Selectors）

选择器让用户无需离开编辑器即可为给定字段选择值。它们以数字输入框旁边的小 **`...`** 按钮形式出现：

![image](https://user-images.githubusercontent.com/75517/118693269-351a5000-b80b-11eb-81b5-15065634a5b4.png)

所有选择器组件都位于 `libs/shared/selectors/src/selectors/`，并从 `@keira/shared/selectors` 导出。

### SingleValueSelectorBtnComponent

`SingleValueSelectorBtnComponent` 让用户为给定字段从列表中选择一个**单一值**。例如，`creature_template` 的 `exp` 字段：

```
0 - Classic
1 - The Burning Crusade
2 - Wrath of The Lich King
```

在 `libs/shared/acore-world-model/src/options/` 中将列表定义为 `Option` 数组：

```ts
// libs/shared/acore-world-model/src/options/expansion.ts
import { Option } from '@keira/shared/constants';

export const EXPANSION: Option[] = [
  { value: 0, name: 'Classic' },
  { value: 1, name: 'The Burning Crusade' },
  { value: 2, name: 'Wrath of The Lich King' },
];
```

在组件中导入该数组，将其暴露为 `protected readonly`，并将 `SingleValueSelectorBtnComponent` 添加到独立组件的 `imports` 中：

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

在模板中通过 `keira-single-value-selector-btn` 使用它：

- `[control]` 表单控件，例如 `editorService.form.controls.exp`；
- `[config]` 一个指定 `options` 和 `name` 的对象；
- `[modalClass]` 可选，模态框的 CSS 类（例如 `modal-md`、`modal-lg`）。

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

结果：

![image](https://user-images.githubusercontent.com/75517/118694803-c1794280-b80c-11eb-9099-00758983ca2e.png){width=300}

![image](https://user-images.githubusercontent.com/75517/118694841-cf2ec800-b80c-11eb-8719-b770a7fd0c98.png){width=500}

### FlagsSelectorBtnComponent

`FlagsSelectorBtnComponent` 让用户从一组**标志**（位掩码）中组合一个值。如果 *bits*、*bitmask*、*flags* 这些术语听起来陌生，[这个页面](https://en.wikipedia.org/wiki/Bit_field)会解释它们。

在 `libs/shared/acore-world-model/src/flags/` 中将位列表定义为 `Flag[]`：

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

位从零开始。然后在组件中暴露 `DYNAMIC_FLAGS` 并导入 `FlagsSelectorBtnComponent`：

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

模板：

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

输入项：

- `[control]` 表单控件（例如 `editorService.form.controls.dynamicflags`）；
- `[config]` 一个指定 `flags` 和 `name` 的对象；
- `[modalClass]` 可选的模态框 CSS 类。

结果：

![image](https://user-images.githubusercontent.com/75517/118697264-685ede00-b80f-11eb-9609-6b4af903bcdc.png){width=300}

![image](https://user-images.githubusercontent.com/75517/118697333-790f5400-b80f-11eb-8795-cdeae8ebfd64.png)

### 其他选择器

还有许多其他选择器，它们要么搜索 MySQL 世界库，要么搜索打包的 SQLite DBC 数据。在 `libs/shared/selectors/src/selectors/` 中查找它们的实现：

- `area-selector` —— DBC 区域搜索。
- `base-selector` —— 每个选择器使用的共享基类（扩展 `SearchService`）。
- `boolean-option-selector` —— 作为选择器的快速是/否切换。
- `creature-selector` —— 在 `creature_template` 中搜索生物。
- `faction-selector` —— DBC 阵营。
- `flags-selector` —— 通用位掩码选择器（由 `FlagsSelectorBtnComponent` 使用）。
- `game-tele-selector` —— 传送地点。
- `gameobject-selector` —— 在 `gameobject_template` 中搜索游戏对象。
- `generic-option-selector` —— 快速下拉变体。
- `holiday-selector` —— DBC 节日。
- `icon-selector` —— DBC 法术图标。
- `item-enchantment-selector` —— DBC 物品附魔。
- `item-extended-cost-selector` —— DBC 物品扩展花费。
- `item-limit-category-selector` —— DBC 物品限制类别。
- `item-selector` —— 在 `item_template` 中搜索物品。
- `language-selector` —— 游戏内语言。
- `map-selector` —— DBC 地图。
- `npc-text-selector` —— `npc_text` 搜索。
- `quest-selector` —— 在 `quest_template` 中搜索任务。
- `single-value-selector` —— 通用单值选择器（由 `SingleValueSelectorBtnComponent` 使用）。
- `skill-selector` —— DBC 技能。
- `sound-entries-selector` —— DBC 音效条目。
- `spell-selector` —— DBC 法术。

示例：**item-selector**。

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

## 数据库层

`@keira/shared/db-layer` 暴露两个服务家族：

- **`MysqlService`** —— 包装 `mysql2`（以及可选的用于 SSH 隧道的 `ssh2`）。持有实时的 `Connection`，暴露 `connectionLost$`，执行重连。仅在 Electron 内部加载（`npm run ng:serve:web` 的 Web 预览模式没有真实的数据库）。
- **`SqliteService`** —— 包装 `sqlite3`，针对一个随应用打包的、只读的 `.sqlite` 文件（`KEIRA_APP_CONFIG.sqlitePath`），该文件随 AzerothCore DBC 数据一起发布，供选择器（图标、法术、地图、阵营等）使用。

两者都暴露 `dbQuery<T>(queryString)`，返回一个 `Observable<T[]>`。

在它们之上，有两个**查询**服务来构建和执行领域 SQL：

- **`MysqlQueryService` 扩展 `BaseQueryService`** —— Keira3 的核心。每个编辑器都会调用它。
  - `getUpdateQuery<T>(table, idField, currentRow, newRow)` —— 比较两个行对象，生成一个 `UPDATE … SET … WHERE`。
  - `getFullDeleteInsertQuery<T>(table, rows, idField, [secondIdField], [extraIdField])` —— 为多行表生成一个 `DELETE`，后跟 `INSERT INTO … VALUES (...)`。
  - `query<T>(sql)` —— 运行自定义查询。
  - 用于任务奖励声望、SAI 脚本、最大 ID 查找等的专用辅助函数。
  - 使用 **Squel**（`squel.update(squelConfig).table(...)`、`squel.select(squelConfig).from(...)` 等）。来自 `@keira/shared/config` 的 `squelConfig` 标准化了 SQL 风格和格式。
- **`SqliteQueryService`** —— 从打包的 DBC sqlite 读取（区域、阵营、节日、图标等）。被选择器大量使用。

## 应用流程

1. Electron 启动 `main.js`（由 `main.ts` 编译），它创建一个 `BrowserWindow` 并加载 `http://localhost:4200`（开发模式）或 `dist/browser/index.html`（生产模式）。
2. Angular 启动 `AppComponent`（`apps/keira/src/app/app.component.ts`）。它挂载 `keira-connection-window`（登录），直到 `MysqlService.connectionEstablished === true`，然后切换到 `keira-main-window`。
3. `MainWindowComponent` 渲染侧边栏 + `<router-outlet />`。路由位于 `apps/keira/src/app/routes.ts`。大多数编辑器路由都有 `canActivate: [SomeHandlerService]`。
4. 用户通过 `Select*Component` 选择一行，它会调用 `handlerService.select(...)`。路由器导航到该实体的主编辑器。
5. 编辑器组件触发 `editorService.reload(...)`，它从 MySQL 读取、填充表单，并开始监听 `form.valueChanges` 以在每次更改时重建 diff/full 查询。
6. 用户点击"Execute"或"Save" → `editorService.save(...)` 针对 MySQL 运行 diff 查询，然后重新加载实体。

## 添加新编辑器：检查清单

将此作为为 DB 表添加新编辑器的配方。（对 AI 代理尤其有用。）

1. **为表建模**，在 `libs/shared/acore-world-model/src/entities/<table-name>.type.ts` 中：
  - 导出一个 TypeScript 类，其公共字段与 DB 列和默认值匹配。
  - 导出表名和键列的字符串常量：`<NAME>_TABLE`、`<NAME>_ID`，可选的 `<NAME>_NAME`、`<NAME>_SEARCH_FIELDS`。
  - 从 `libs/shared/acore-world-model/src/index.ts` 重新导出该文件。

2. **决定编辑器的风格**：
  - 每个主实体一行 → `SingleRowEditorService<T>` + `SingleRowEditorComponent<T>`。
  - 每个主实体多行 → `MultiRowEditorService<T>` + `MultiRowEditorComponent<T>`。
  - 复合主键 → `*ComplexKey*` 变体。
  - `*_loot_template` 表 → 扩展 `LootTemplateComponent<T>` 或 `LootTemplateIdComponent<T>`。

3. **选择一个 feature 库**。如果它属于某个现有主实体（生物、物品、任务、…），就放在那里。否则在 `libs/features/<name>` 下创建一个新的 feature 库（以 `libs/features/game-tele` 作为最小示例进行模仿），并在 `project.json` 中注册其标签 `"tags": ["scope:features"]`。

4. **创建服务**：扩展正确的基类，设置 `_entityClass` / `_entityTable` / `_entityIdField`（多行时为 `_entitySecondIdField`）。注入该 feature 的 `*HandlerService`。在构造函数中调用 `this.init()`。

5. **创建组件**：扩展匹配的基组件，通过 `editorService` 注入服务，通过 `handlerService` 注入 `*HandlerService`。使用 `keira-top-bar`、`keira-query-output` 以及字段输入（在合适处使用选择器）构建模板。

6. **接好 handler**：将新的 `*_TABLE` 添加到 handler 的 `_statusMap`，并暴露一个 `is*Unsaved` 信号，以便侧边栏显示圆点。

7. **配置路由**：将组件添加到 `apps/keira/src/app/routes.ts`，使用 `canActivate: [TheHandlerService]`。从 feature 库的 `src/index.ts` 重新导出该组件。

8. **添加侧边栏条目**，用于 `libs/main/main-window/src/sidebar/...` 中的新编辑器。

9. **测试**：编写一个 `.service.spec.ts`（单元）和一个 `.integration.spec.ts`（使用扩展 `EditorPageObject`/`MultiRowEditorPageObject` 的 `*PageObject`）。强制执行 100% 覆盖率 —— 使用 `nx test <project-name>` 验证。

## 提示

- **路径别名**：跨库的导入始终使用 `@keira/<scope>/<name>` —— 绝不在库之间使用相对路径。完整映射位于 `tsconfig.base.json` 中。
- **无 NgModules**：每个组件都是 `standalone: true`，并列出自己的 `imports: [...]`。如果你向模板添加新依赖（指令、选择器组件、管道），记得将其添加到该 `imports` 数组中。
- **OnPush 是强制的**（ESLint 强制执行）。在从回调（HTTP、RxJS 等）改变状态之后，你可能需要 `changeDetectorRef.markForCheck()` —— 基类 `EditorService` 已经在 `save`/`reload` 中这样做了。
- **控制台规则**：只允许 `console.warn`、`console.info`、`console.error`（`no-console` 规则）。面向用户的消息使用 `ToastrService`。
- **模块边界**：一个 feature 不能导入另一个 feature。如果你发现自己想要这样做，代码应该移到 `libs/shared`。shared 也一样 —— 只能依赖其他 shared 库。
- **Squel 是一个全局变量**（`declare const squel: ...`），位于 `mysql-query.service.ts` 中。测试通过 Vitest 设置将其引入，因此不需要额外导入。
- **测试紧邻代码**：`foo.service.ts` ↔ `foo.service.spec.ts`。集成测试使用 `.integration.spec.ts` 后缀，并依赖 `@keira/shared/test-utils` 中的 Page Object 模式。
- **只运行受影响的项目**：`npm run lint` 和 `npm run test` 使用 `nx affected:*`。对于单个项目使用 `nx lint <name>` / `nx test <name>`（例如 `nx test keira-features-creature`）。
- **Hash 路由**：应用内部的链接应使用路由器（`routerLink`）—— 完整 URL 包含 `#`，因为 Electron 从 `file://` 加载。
- **热重载开发**：`npm start` 同时运行 `nx serve keira` 和 Electron。对于纯浏览器开发（无 Electron、无 DB），使用 `npm run ng:serve:web` —— SQLite/MySQL 服务在 Electron 之外会变为 no-op。
- **覆盖率阈值为 100%** —— 没有测试的代码会导致 CI 失败。如果一个分支确实无法测试，使用 `/* istanbul ignore next */`（已在许多地方使用）并说明理由。
- **格式化**：Prettier，140 字符宽度、单引号、尾随逗号。`format-staged` 脚本通过 Husky 的 pre-commit 钩子运行。
