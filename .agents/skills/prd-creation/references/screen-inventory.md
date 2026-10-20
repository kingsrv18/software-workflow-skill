# Screen inventory and design references

For UI applications, create a separate proposed screen inventory alongside the PRD and user flows, defaulting to `docs/ui/screen-inventory.md`. Reuse an equivalent existing authority. This inventory owns screen identity, canonical names and design lookup; user flows own interaction sequences, and the implementation plan owns progress and approval evidence. Products without a UI need no inventory.

## Naming and identity

Use these defaults for new projects; preserve equivalent existing stable conventions when adapting a project:

| Item | Convention | Example |
| --- | --- | --- |
| Flow | Stable ID and action/outcome name | `FL-004 — Create and issue invoice` |
| Step | Flow ID plus stable step ID | `FL-004.S03` |
| Screen/surface | Stable ID and canonical name | `SCR-012 — Invoice details` |
| Design frame | Screen ID, canonical name, viewport, state | `SCR-012 — Invoice details — Desktop — Default` |

Keep IDs independent of role, module, route and tool. Use the canonical name in document references and design frames; readable names may change while IDs remain stable. Step IDs remain stable when sequence changes; record execution order separately when needed. Add role/context to frame names when the same screen has genuinely distinct variants. A state or viewport variant normally retains its screen ID. Give a distinct page, dialog or drawer an ID when it needs independent design lookup; ordinary controls need no screen IDs.

## Inventory contents

Populate these fields at the depth needed for the application:

- Screen ID, canonical name, role(s), module and surface type.
- Linked flow/step IDs, supporting shared screens and many-to-many mappings.
- Required information/actions and state/viewport variants, referencing interaction and specialist rules rather than copying them.
- Design lookup per variant: selected tool, file/project reference, native screen/frame/node ID or exact accessible reference, and reviewed version/snapshot where available.
- Supersession/alias references when names or screen composition change.

Separate the logical screen list from a variant/design-reference table if multiple states or viewports would make a single table unwieldy. Before design, logical IDs identify proposed surfaces; native IDs, links and versions remain explicitly pending. Proposed composition is not an approved UI. Never invent tool-native IDs or link to nonexistent files. Keep approval records in the plan and link them from reviewed design references.

## Design reconciliation and retrieval

Design can combine or split proposed surfaces while preserving product behavior. Retain the ID when the same screen is renamed or refined. For splits/merges, preserve IDs for retained identities, assign new IDs for new surfaces, and keep retired entries pointing to replacements; never reuse retired IDs. Update flow-step mappings and actual frame names/references together. Where the tool cannot represent the naming convention, record the exact tool label and an explicit mapping to the canonical identity.

For implementation, resolve **flow → step → screen ID → required variant → reviewed design reference**. Prefer exact native identifiers or accessible links, then verify the retrieved screen's identity, context and version. A name search is a lookup aid, not proof of an approved match. Duplicate candidates or a missing/inaccessible reference leave dependent UI work unresolved until the source is clarified or an explicit alternative is accepted. Record that blocker in the plan; independently ready work can proceed.

## Completion checks

Before preparation handoff, confirm that flow references resolve to logical screens and every proposed screen supports accepted scope. Pending design links are valid at this stage. Before dependent UI implementation, verify that required variants resolve unambiguously to reviewed designs or documented accepted alternatives. Exercise a shared screen, multiple variants and a renamed/superseded screen when applicable. Structural file checks cannot establish the correctness of these mappings; inspect them as part of content review.
