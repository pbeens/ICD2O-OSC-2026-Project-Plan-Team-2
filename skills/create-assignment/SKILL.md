---
name: create-assignment
description: Generate paste-ready prompts for the Assignment Strengthener GPT when the user asks to create or strengthen an assignment for a specific lesson, topic, or notebook. Use for requests like "create assignment for lesson 02" and return the direct GPT link plus exact prompt text. Also use for pasted GPT output cleanup/writeback into repository assignment files.
---

# Create Assignment

## Overview
Support two workflows:
- Prompt mode: Build a paste-ready prompt for Assignment Strengthener.
- Writeback mode: Clean pasted Assignment Strengthener output and save a finalized assignment file in `lessons/`.

Assignment Strengthener URL:
`https://chatgpt.com/g/g-6921ca06cf208191b9f8374abc30f632-assignment-strengthener`

## Workflow
### Mode A: Prompt Generation
1. Resolve target lesson from user input.
2. Read matching lesson files:
- `lessons/NN-...-lesson-plan.md`
- `lessons/NN-...-tutorial.md` (if present)
3. Build a structured prompt with lesson context and assignment requirements.
4. Include expectations as `code + full expectation text`, one per line.
5. Provide optional attachment checklist (lesson plan/tutorial/notebook).

### Mode B: Writeback From Pasted Output
1. Accept pasted Assignment Strengthener output.
2. Keep assignment content only when the user wants assignment-only output.
3. Clean formatting while preserving intent:
- remove emojis
- normalize headings/spacing
- keep beginner-friendly classroom tone
- keep gist unchanged unless user requests deeper edits
- preserve `Teacher Notes (PACT-Based Rationale)` when present
- add `Teacher Notes (PACT-Based Rationale)` when the user explicitly requests it
4. Save as `lessons/NN-topic-assignment.md`.
5. Report file path and key edits made.

## Prompt Construction Rules
- Include lesson number and exact lesson title.
- Include assignment purpose and student-facing context.
- Include expectations as explicit `code + full text` entries (one per line). Required.
- If expectation text is missing, derive it from `resources/ICD2O_2023.md` using the lesson's expectation codes.
- Include success criteria and Growing Success evidence model (observation, conversation, product).
- Do not start with phrases like "Create one assignment document".
- Frame prompt as context + expectations + requirements.

## Output Format
Always return:
1. `Open:` the Assignment Strengthener URL.
2. `Paste this prompt:` in a fenced markdown block.
3. `Attach these files:` optional checklist (lesson plan, tutorial, notebook).
4. `Then return with:` short checklist asking user to paste back assignment output text.

## Attachment Guidance
When useful, suggest attaching:
- target lesson plan file
- target lesson tutorial file (if available)
- related notebook file(s)

Do not require attaching `references/expectations-compliance.md`.

## Quality Checks
- Confirm lesson filenames match repository naming conventions.
- Confirm expectation codes exist in `resources/ICD2O_2023.md`.
- Confirm final prompt includes one-per-line expectation entries with code and full text.

