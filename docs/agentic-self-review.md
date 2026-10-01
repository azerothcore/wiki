# Agentic Self Review

At AzerothCore we strive for high code quality, and this is why we have a process that requires all contributors who submit PRs made with AI to carefully run a `/self-review` session.

The goal of this step is to make sure your PR does not introduce any regressions or undesired side effects, keeping the overall code quality high.

**This will cost you extra time and tokens.** We prefer fewer PRs of higher quality over more AI-slop PRs.

## For contributors: how to run the self-review process

### Installing the skill

The `/self-review` skill is part of the [agent-toolkit](https://github.com/eai-org/agent-toolkit) collection of open-source utilities.

You can quickly install it with:

```
git clone https://github.com/eai-org/agent-toolkit.git && cd agent-toolkit && ./install.sh
```

And remember to keep it up to date regularly with:

```
cd agent-toolkit && git pull && ./install.sh
```

### Choosing a powerful model

For the self-review, it is mandatory to use a powerful model such as Claude Fable, GPT Sol, or at least Claude Opus or an equivalent frontier model.

**Do not use cheap models**, as they do not produce good-quality results.

**Do not try to cheat this**: maintainers can always run the same process on your PR and compare the findings.

### Run it, and wait

Check out the branch of your PR locally, open your AI agent, and run:

```
/self-review
```

This will take a while. Be patient.

### Address the findings

After checking your code, the agent will come up with findings and give you recommendations about which ones should be addressed. **You decide**.

Please check this carefully: do not blindly accept changes that you are not sure of. Ask the agent for further explanation if anything is unclear.

The review will continue until there are no more findings that need to be addressed.

### Post the result

The self-review will generate a `<slug>.SELF-REVIEW.md` artefact (in the `.agents/plans/<slug>/` directory) with content that is ready to be copy-pasted **verbatim** as a comment on your PR.

Do NOT alter the contents of the artefact manually, and do NOT commit the artefact file itself to your PR.

The staff reserves the right to close any PR that does not provide such an artefact.

That's it.

## For maintainers: how to steer the self-review process

The behavior of the `/self-review` skill is defined in two parts:

- The [skill source code](https://github.com/eai-org/agent-toolkit/blob/main/skills/self-review/SKILL.md) and its dependencies, living in the [agent-toolkit repository](https://github.com/eai-org/agent-toolkit), which define the general behavior the skill has in all projects
- The AzerothCore project-specific rules that the skill is always instructed to follow, which live in the [.agents/docs/self-review-rules.md](https://github.com/azerothcore/azerothcore-wotlk/blob/master/.agents/docs/self-review-rules.md) file of the AC main repository

Also keep in mind that the skill is instructed to check any relevant governing docs in the AzerothCore repo, such as the other docs located under [.agents/docs/](https://github.com/azerothcore/azerothcore-wotlk/blob/master/.agents/docs/) and, of course, the [AGENTS.md](https://github.com/azerothcore/azerothcore-wotlk/blob/master/AGENTS.md) file.

To make changes to those, always invoke these skills:

- `/compact-docs-writer` whenever making changes to any `*.md` file
- `/compact-skill-creator` whenever making changes to a skill
