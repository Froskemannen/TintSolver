# TintVision – Game Mechanics Reference

This document contains authoritative rules and logical behaviors for the game *tint.* by Lykke Studios, as relevant to the TintVision project. It defines how colour mixing, gates, and stroke mechanics work, including terminal and invalid states. This is intended for use during simulation design, solver development, and as a canonical reference for reproducing in-game logic.

---

## 🎨 Colour Mixing System

### 🎯 Goal

Create paint strokes that match target origami colours by mixing paint sources and interacting with game elements.

### ✅ Allowed Colours

* **Primary**: red, blue, yellow  
* **Secondary**: green, orange, purple  
* **Special**: white, grey

> All solvable levels only use the above **seven** colours.

---

## 🧪 Active Colour Rules

* You begin a stroke by picking up paint (droplet or canvas paint).
* Your **active colour** persists and evolves throughout the stroke.
* Colour changes result from:
  * Mixing with existing paint
  * Passing through gates

### 🔁 Mixing Rules

| **Active Colour** | **Mixed With**          | **Result**                 | **Notes** |
|------------------|--------------------------|----------------------------|-----------|
| Primary          | Primary                  | Secondary                  | e.g. red + yellow → orange |
| Primary/Secondary | Secondary                | ❌ Grey                    | Invalid mix (secondary + anything except white) |
| Primary          | Secondary                | ❌ Grey                    | Invalid mix |
| Any              | Grey                     | ❌ Grey                    | Grey is contagious |
| Any combination  | 3 Primaries total        | ❌ Grey                    | Overmixed |
| White            | Any colour (except white) | Ends stroke with short trail | Strategic use; terminates on mix |
| White            | White                    | Continues                  | Can draw indefinitely with white alone |
| Any (not white)  | White                    | Continues                  | White on canvas is non-reactive |

---

## ☠️ Grey (Ruined Colour)

* **Generated** by:
  * Mixing 3 or more primary colours
  * Mixing a primary with a secondary
  * Interacting with grey

* **Effects**:
  * Results in a short trailing stroke (1–2 tiles) then immediate stroke termination
  * Cannot solve puzzles or be used tactically
  * Overwrites everything visually, but has no value

> ⚠️ Grey is a **fail state**. Solver must avoid it completely.

---

## ⚪ White (Eraser Paint)

* Can be drawn **indefinitely**, **until** it touches another colour
* Upon touching any colour:
  * Colour becomes white briefly
  * Stroke ends after short tail
* **Use cases**:
  * Cut through strokes or clear paths surgically
  * Can be switched to other colour through gates accepting white

> ✅ White is **useful**, but fragile and situational.

---

## 🧱 Gate Types

### 1. 🔄 Negation Gates

* Gate with 1 colour entry (e.g. red, blue, etc.)
* Cannot be white or grey
* Behaves like a **colour subtraction or negation tool**
* Example effects:
  * Red negation gate + active red → becomes white
  * Purple (red+blue) through blue negation → becomes red
  * Blue through red negation → remains blue (red not in mix)

> 🗑 **All gates disappear after use.**

---

### 2. 🎨 Colour Switch Gates

* Bidirectional gate with 2–4 colours
* You may **enter or exit** through *any* endpoint
* Replaces your **active colour** with the colour on the exit path
* **White** is valid in switch gates

> 🟢 Valid example: enter on white, exit on red → active colour becomes red  
> ❌ Grey is **not** allowed in gate endpoints (cannot appear in gate definitions)

### Total Combinations

* 2-colour: 7² = 49  
* 3-colour: 7³ = 343  
* 4-colour: 7⁴ = 2,401

> 🗑 Gates **disappear after one use**, even if the stroke continues.

---

## ✍️ Stroke Mechanics Summary

* Begin a stroke by touching a droplet
* You carry an **active colour** which evolves through:
  * Mixing (droplets or strokes)
  * Negation gates
  * Colour switch gates

### ✅ A stroke **does NOT end** when reaching a target

* You may solve a target mid-stroke and continue drawing.
* A stroke ends **only when**:
  * You manually release your finger (or complete stroke in our game copy sandbox environment)
  * Your colour becomes grey (short tail)
  * White interacts with a colour (short tail)

> 🟢 You can solve multiple targets in one continuous stroke.

---

## 🧠 Solver Logic Guidelines

* Grey = **terminal state**, prune paths leading to it
* ✅ **White is a strategic tool**:
  * You can draw indefinitely with white **as long as you don’t mix** with other colours.
  * Mixing white with any colour causes the stroke to **terminate shortly after**, leaving a small white trail (i.e., a “cut”).
  * White is useful for:
    * Cutting through existing strokes (surgically removing paths),
    * Creating clear lanes for other colours to reach gates or targets,
    * Entering colour switch gates that accept white as a valid input.
  * White should be used deliberately, with awareness that **mixing ends the stroke**.
* Always simulate state transitions when moving across canvas
* Respect gates as **non-linear** effects — may change colour suddenly
* Origami targets must be reached with **exact matching colour**

---

## 🔗 Integration Notes

* This file should be updated if:
  * New mechanics are discovered
  * Gate logic or colour rules change
* Referenced by:
  * `solver/`
  * `sandbox/`
  * `docs/developer_guide.md`

---

## 📝 Revision History

* **v1.4** - Fixed markdown linting warning `MD004/ul-style: Unordered list style [Expected: asterisk; Actual: dash]`. Fixed date formatting to follow ISO 8601 date only format (YYYY-MM-DD). (2025-06-28)
* **v1.3** – Rewrote mixing rules using two-column input format (`Active Colour` + `Mixed With`); clarified directional behaviour of white; corrected that white only ends strokes when it is the *active* colour. (2025-06-17)
* **v1.2** – Clarified white behaviour: unlimited until mix, ends after mixing; added that white can be used in switch gates and drawn indefinitely unless interacting with colour. (2025-06-17)
  * Updated solver guidelines and gate logic accordingly. (2025-06-17)
* **v1.1** – Added white in colour switch gates, made gates consumable, clarified that targets do not terminate strokes. (2025-06-17)
* **v1.0** – Initial colour system and mixing logic. (2025-06-16)
