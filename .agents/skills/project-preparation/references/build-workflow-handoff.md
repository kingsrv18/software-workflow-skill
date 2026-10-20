# Design-and-build workflow handoff

Project preparation creates this project spec from the agreed implementation plan, PRD, relevant product specs, and actual scaffold. It explains how an agent follows the plan and works with the user. The implementation plan remains authoritative for phases, slices, dependencies, checkpoints, progress, evidence, feedback, and approval history.

## Create the project spec

Reuse an existing authoritative workflow document or create `docs/build-workflow.md`. Populate it with project-specific conventions so another coding agent can follow it without any skills installed. Link the actual plan, product/technical specs, design sources, and preview/setup instructions. Keep product-specific screen and state rules in their UI/domain authority and reference them.

Explain preparation versus feature implementation and the verified baseline. Record actual preview commands, provider/mock boundaries, safe fixtures, approval ownership, and known access/setup blockers. Preserve unknowns as explicit inputs needed before dependent work.

When UI design follows preparation, route design tasks to the structured user-flows document, proposed screen inventory and relevant specialist rules. Use any user-selected connected design tool or supplied design material; design creation requires an authorized design task. Preserve the inventory's screen IDs and naming convention in design frames. After review, reconcile flow-step/screen mappings, populate actual variant/frame references in the inventory and update affected plan dependencies. Pending designs do not block scaffold preparation, but remain inputs required before dependent UI implementation. Layout choices can refine page boundaries; product-behavior changes return to their authoritative specs.

## Development initiation prompt

Generate `PROJECT_INITIATION_PROMPT.md` in the project root as a ready-to-paste instruction for a fresh coding-agent chat. Adapt an existing equivalent prompt in place and link its actual location from README. Populate it with the project's real names and repository-relative document paths, interpreted from the project root. Keep it usable without any workflow skills installed. This is an entry instruction; the plan and workflow spec remain the live authorities.

The prompt directs the receiving agent to:

1. Work in this project, read its actual agent instructions, README, PRD overview, implementation plan and build-workflow spec, then load the relevant specialist context for the selected work. Include links to applicable flows and screen inventory.
2. Inspect source/configuration, repository changes and recorded verification before trusting baseline or completion claims; preserve existing work. Follow actual setup instructions and verify prerequisites within available access.
3. Read the plan's current progress/resume record and select the next ready slice whose dependencies and prior review gates are satisfied. State the outcome and applicable contracts before implementation. Derive the starting point at runtime rather than hardcoding a slice into the prompt.
4. For UI work, follow flow → step → screen → required variant in the inventory, retrieve and inspect the exact reviewed design from the connected tool or supplied material, and resolve missing or ambiguous references before dependent UI implementation.
5. Implement the bounded flow/slice through UI, backend, persistence, authorization and integrations as applicable, following the linked contracts and completion criteria. Intermediate UI mocks do not complete the connected flow.
6. Run the plan's checks, repair failures, record real evidence, and demonstrate working behavior at the existing review checkpoint. Follow feedback and approval rules in the workflow spec before advancing past that gate.
7. Maintain progress, blockers and the resume point in the existing plan. When an input is unavailable, record the dependency and continue independently ready work that does not cross a pending approval gate; request the specific missing input when needed.

Keep the prompt concise and project-specific. Link setup commands, product rules, design conventions and review procedures instead of duplicating them. It must not imply completed design/provider readiness or expand authority to deploy, provision services or modify external designs. Finish preparation by walking through this prompt against the actual package: references resolve, the live plan determines the next action, and an agent without installed skills can follow the handoff.

## Follow the plan and obtain design inputs

At each session, read project agent instructions, current plan, workflow spec, and the relevant source docs. Check actual files and verification evidence before trusting recorded progress. Select the next ready slice or flow whose dependencies and previous approval gates are satisfied.

For design-dependent implementation, locate the flow/module in the plan and its structured flow contract. Resolve its step IDs through the screen inventory to canonical screen IDs and required role/state/viewport variants, then retrieve the exact reviewed design references. Inspect relevant frames, transitions, components and states through available tools, verifying identity/context/version rather than trusting a name search alone. Use existing supplied material when it covers the flow; avoid asking the user to resupply accessible inputs. Record the source/version or frame identity used in the plan's evidence.

If the relevant design is missing, ambiguous or inaccessible, resolve the specific gap or ask for an accessible source or explicitly accepted alternative. Record the blocker and keep dependent UI work pending; independently ready work may proceed within existing review gates. Do not invent an approved design. Apply this design step to work that needs it; setup, backend-only work, and non-UI modules use their applicable contracts.

## Implement, verify, and review

Mark the selected work in progress, read its inputs, implement the bounded slice, and run its planned checks. Failed checks keep the work unfinished. Record actual outputs, verification commands/results, limitations, blockers, and next action in the implementation plan.

At each completed UI flow or module checkpoint, launch and verify an accessible working demonstration and show it to the user. Provide preview access and a short walkthrough, with safe representative mock/test data, usable navigation, and relevant states and edge cases. Screenshots supplement the demonstration. Non-UI modules use a working product view, runnable API, CLI, or other appropriate demonstration. Identify what is mocked and what is connected; mock approval does not approve an unshown real integration.

Ask the user to review the demonstrated flow/module. Record feedback as concrete revision work linked to its checkpoint, implement and verify revisions, then show the updated demonstration. Obtain explicit approval of the demonstrated version and scope before closing the checkpoint and advancing past its gate. Passing tests, silence, or elapsed time do not establish user approval. An inaccessible preview leaves the checkpoint pending with its blocker.

## Progress and resumption

Use the plan's stable identifiers and conventions. Distinguish planned, ready, in-progress, blocked, awaiting-approval, complete, and superseded work, and pending, in-review, changes-requested, and approved checkpoints, or the project's equivalent states. Readiness requires inputs, predecessor work, and earlier approvals; completion requires technical checks and applicable user approval.

Keep one progress record per ID in the plan. Record checkpoint scope, demonstrated revision/environment/date, verification and preview access, limitations, feedback/revisions, and explicit approval with its source conversation/date. Preserve earlier records as history. Store no credentials in access details.

Before ending a session, record the active slice/checkpoint, last verified result, pending decisions/feedback, next action/readiness, and preview launch/access details. Pause progression past pending review gates and keep the preview accessible when feasible. On resumption, verify that prior approvals cover the current implementation.

When requirements, designs, or implementation change, update affected authoritative specs and plan work together; reopen checkpoints when prior approval no longer covers the behavior. Resolve consequential contradictions with the owner. External provisioning stays within user authorization; unavailable checks, design access, or provider setup remain concrete blockers rather than claimed evidence.

## Navigation and handoff checks

Route building, verification, review, and resumption from `AGENTS.md` to both the existing implementation plan and workflow spec, and UI lookup to flows and inventory. Explain the three-stage handoff and link the development initiation prompt in `README.md`. Link actual files rather than future nonexistent paths.

Before handoff, check that named flows/modules and gates match the approved plan, linked specs exist, design-access instructions cover accessible and missing inputs, demonstrations and approval rules cover UI and non-UI work, and readiness claims match performed checks. Record preparation results and the next ready action in the plan. This spec owns procedures, not a duplicate task list or progress record.
