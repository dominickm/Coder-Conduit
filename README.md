```text
  ____          _               ____                _       _ _
 / ___|___   __| | ___ _ __    / ___|___  _ __   __| |_   _(_) |_
| |   / _ \ / _` |/ _ \ '__|  | |   / _ \| '_ \ / _` | | | | | __|
| |__| (_) | (_| |  __/ |     | |__| (_) | | | | (_| | |_| | | |_
 \____\___/ \__,_|\___|_|      \____\___/|_| |_|\__,_|\__,_|_|\__|

                       x   W a r p   O z
```

# Coder Conduit

Welcome to **Coder Conduit**! This repository is a joint community project and live sandbox created by Coder Radio and Warp.dev. 

A massive thank you to [Warp.dev](https://warp.dev) for sponsoring this project and providing the powerful AI orchestration technology that makes this possible!

The central goal of this initiative is to demonstrate the orchestration capabilities of Warp's Oz framework in a live, community-driven open-source environment. By participating, you can submit feature requests, report bugs, and contribute code while observing how a team of specialized AI agents collaborates to triage, plan, and implement changes.

---

## Meet the Agents

Coder Conduit is powered by five distinct AI agents, all orchestrated by Warp's Oz framework to handle different aspects of repository management:

* **The Code Critic (PR Review Agent):** Triggered when a PR is created or updated, this agent acts as a senior developer. It analyzes code diffs against our guidelines, leaves line-by-line comments, and requests changes if standards are not met.
* **The Triage Tech (Issue Diagnostic Agent):** When a new issue is created, this agent reads the description and categorizes it (e.g., bug, enhancement). If context is missing, it will ask the submitter for clarification before applying labels.
* **The Architect (Issue Creation Agent):** Running on a scheduled CRON job, this proactive agent scans the repository for technical debt, unhandled edge cases, or feature requests, and automatically drafts implementation-ready issues.
* **The Coder (Implementation Agent):** Triggered strictly by the `ready-to-implement` label, this agent generates code and submits a PR. To manage our token budget, it only takes on issues it is confident it can solve.
* **The Staff Engineer (Planning Agent):** Tackling larger feature requests using a "spec-driven development" philosophy, this agent generates a comprehensive plan and specification document for manual review before any implementation begins.

---

## How to Contribute

We encourage the Coder Radio community to interact with the repository! To keep the repository clean and ensure the Oz agents can parse your submissions reliably, please adhere to the following guidelines:

1.  **Use the Templates:** All issues and PRs **must** follow the predefined GitHub templates. Malformed requests will be automatically rejected by the Triage Tech.
2.  **Provide Clear Context:** Treat the AI agents like junior developers. Provide clear context, reproducible steps, and clean code to get the best automated reviews and interactions.
3.  **Labeling Permissions:** For security and token budget management, label setting is strictly locked down. Only human maintainers and the Triage Agent have permission to apply labels (such as `ready-to-implement`).

---

## Code of Conduct

Contributors must remain constructive. Any inappropriate behavior, trolling, or intentional attempts to "jailbreak" or spam the AI systems will result in immediate bans and closed PRs.

---

## License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for more details.
