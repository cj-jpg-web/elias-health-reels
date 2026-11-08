# Whole-sequence visual review

Review the reference-shot map before image generation and the actual image sequence before delivery. Keep the review concise and internal unless the user asks to see it.

## Before generation
- Map observed shot changes and distinguish visible action from narration. Sample transition/contact windows more densely when uncertain.
- Allocate clip lengths after mapping the action. A continuous source shot can occupy several clips; several short actions may fit one clip. Do not create a new editorial scene per sentence.
- Specify what changes during each clip and what remains unchanged. For a source-supported explanation hold, name the explanation and justify the unchanged physical state.
- Select composition for that purpose. Keep broad presenter framing when appropriate, but show the working contents when the action depends on them. Avoid arbitrary angle quotas or mandatory action changes.

## Inspect actual images together
1. Read the source map, clip action and image as one unit. Is the assigned action still possible from this starting pose?
2. Check the entering state against the preceding planned exit: ingredients, quantity, texture, wetness, utensil placement, grip and supporting identities. A generic small mound cannot stand for every stage.
3. Check for a missing process stage. An unmixed bowl must not become a presented finished spoonful before a mapped mixing action occurs.
4. Compare composition, dominant object, hand task and pose across neighbors. Minor camera drift or a changed facial expression does not by itself establish progression.
5. Evaluate repeated frames against the source. Preserve an intentional ongoing hold; merge unnecessary invented editorial scenes or make the actual mapped action legible. Do not repeat preparation to create visual activity.
6. Check the whole arc. Does it follow the source's problem/demo, preparation, explanation and ending as actually present? Do not force this sequence on references with a different structure.
7. Write specific pass/fix decisions. Repair the affected plan or frame and recheck neighbors. Do not claim generated motion, voice or retention has been validated from stills.

## Failure regression: repeated bowl-and-spoon batch
Observed failure: several consecutive generated images showed nearly the same waist-up presenter, bowl and raised spoon. Prop continuity was present, but the mixing stage was visually weak and the closing explanation was split into redundant presenter clips.

Use this as a counterexample, not as a mandatory new storyboard. The review must flag a premature finished-paste starting frame when mixing is assigned, and flag redundant splits unsupported by the source. It must also accept a similar starting pose when the source intentionally holds that shot and the clip continues its explanation.

Structural lint can verify declarations and duration totals only. A filled field, a nominal new angle or a claimed manual pass cannot replace inspection of the actual frames.
