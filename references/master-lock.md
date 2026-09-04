# Master Lock

## Purpose
Prevent visual drift between the approved Master Illustration and derivative assets.

## Lock after automatic selection
Record:
```yaml
master_id:
subject_identity:
subject_count:
silhouette:
relative_positions:
scale_relationships:
composition:
line_language:
palette_relationships:
texture_character:
approved_reference:
```

## Invariants
These should remain visually stable unless the workflow explicitly reopens the master:
- main subject identity
- major silhouette
- key spatial relationships
- composition logic
- overall line character
- principal palette relationships
- distinctive visual quirk/character

## Allowed transformations
A may change layout around the master.
B may isolate, crop, die-cut and add a sticker border.
C may convert color expression to monochrome.

## Forbidden downstream behavior
Do not re-interpret the source photograph to create B or C.
Do not redraw the master merely because the derivative asset needs a different format.
