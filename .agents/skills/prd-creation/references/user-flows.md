# User flows for UI design

For applications with a UI, create one canonical structured flow document alongside the PRD, defaulting to `docs/product/user-flows.md` in the agreed output folder. Adapt an equivalent existing document instead of creating a competing authority. Scale detail to the agreed release and product complexity. For products without a UI, retain applicable actor/system journeys in the PRD and state why this design handoff is unnecessary.

## Authority and navigation

The PRD owns product intent, scope and requirements and explains the operating loop and critical journeys on its own. The flow document owns detailed user interaction sequences. Link specialist rules such as calculations, state guards and permission policies to their authoritative sections rather than redefining them. Before specialist context files exist, reference actual PRD sections; preparation can later reconcile those references.

Start with a flow inventory: **Flow ID | Goal | Actors | Module(s) | Release | Requirement/use-case references**. Provide indexes by user role and by module that point to the same canonical flows. Keep cross-role journeys together so handoffs and decisions remain visible. Reuse stable flow IDs across the PRD, designs and implementation plan; preserve them when a journey is revised. Separate later-release flows from the detailed first-release handoff.

## Per-flow contract

Each in-scope flow contains the following applicable substance:

| Element | Required substance |
| --- | --- |
| Purpose and scope | Stable ID, descriptive name, realistic scenario, user goal, release and linked requirements/use cases. |
| Actors and access | Initiator, supporting actors, relevant permissions and record scope; link exact policy rules. |
| Starting conditions | Trigger, prerequisites, entry point and relevant prior/subsequent flows. |
| Main sequence | Stable step references; user action and required input, visible response, resulting state and next step. Name planned workspaces where helpful. |
| Decisions and handoffs | Branch conditions, next responsible actor, approval points, notifications and how each actor discovers pending work. |
| Alternatives and recovery | Applicable validation, permission denial, cancellation/correction, empty/loading/pending states, stale/conflicting data, interrupted work, failure, retry and recovery. Describe the visible message or information and available next action. |
| Completion | User-visible result, records or notifications produced, and observable acceptance scenarios including consequential failure paths. |
| Design needs | Required information, actions, workspaces, relevant responsive/accessibility needs, state variants and unresolved UX questions. |

Use numbered steps or a table with **Step | User action and input | Workspace | Visible response and next state**. Shared interaction rules may have one linked home; document each flow's distinct exceptions. Use diagrams for branching or multi-actor handoffs when helpful, aligned with the written sequence. System-only work appears where it changes the user's experience; detailed worker/API mechanics belong to technical authorities.

For example, an import flow may need upload, mapping, validation review, preview, commit and results, including safe behavior after a lost connection. Whether invalid rows allow partial commit comes from the product/domain decision, not the designer's layout choice.

## Design handoff and reconciliation

Describe the experience before fixing page boundaries. Planned workspace names do not assert that approved screens exist. A designer may combine steps or split one step across screens while preserving the accepted behavior. Leave consequential product questions explicit with their affected flows and decision triggers; distinguish them from layout choices the designer can make.

Support any user-selected UI design tool connected to the coding agent, or supplied design material. Before design, record design references as pending in prose rather than linking nonexistent files or inventing screen IDs. Actual design creation follows the user's authorized design phase; this document does not select a vendor or authorize changes to external designs.

After designs are reviewed, map flow/step references and state variants to actual screen/frame identifiers or accessible design references, including the reviewed version where available. Allow many-to-many mapping: a screen may serve several flows, and a flow may span several screens. Keep review status and approval evidence in the implementation plan once it exists; the mapping identifies design sources rather than duplicating progress. Design-discovered behavior changes return to the PRD or relevant specialist authority, then affected flows, design mappings and plan dependencies are reconciled.

## Completion review

Audit coverage in both directions: every first-release use case and applicable role/module path reaches a substantive flow or explicit branch, and every documented flow traces to accepted scope. Check cross-role handoffs, permission boundaries, failure/recovery and outcomes, not just populated IDs. Inspect a representative critical journey from the designer's perspective: can its required information, actions, states and handoffs be designed without inventing consequential behavior? Resolve gaps or record specific decision dependencies before claiming design readiness. Completed UI screens are not required to pass this review.
