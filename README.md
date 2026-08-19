# Hero Planner
#### Video Demo: https://www.youtube.com/watch?v=82Vgeo6hhIY
#### Description:

**Hero Planner** is a web-based planning application for *Diablo II* characters. Its main purpose is to help players plan characters they intend to create in the future and keep track of the equipment they already own versus the equipment they still need to collect.

Planning a Diablo II character can become complicated, especially when a build requires specific unique items, sets, runewords, or equipment for both the hero and their mercenary. Hero Planner provides a central place where this information can be organized before a character is actually created. This makes it easier to prepare for future builds, identify missing equipment, and keep track of resources that have already been collected.

The application is implemented as a web application using **Python**, **Flask**, **Jinja**, and **SQLite3**. The user interface is built with **HTML** and **CSS**.

## Features

### Runes

Runes are special items in Diablo II that can be inserted into suitable socketed equipment. Individual runes can provide useful bonuses, but their most important purpose is often their use in **runewords**.

The **Runes** section allows users to view the available runes and use them as part of their planning process. Keeping track of runes is particularly useful when preparing a character because powerful runewords can require several specific runes, some of which may be relatively difficult to obtain.

Available operations:

- **Show** available runes

### Runewords

Runewords are combinations of specific runes placed into socketed items in a particular order. When the correct combination is used in a compatible item, it creates a powerful piece of equipment with a unique set of bonuses.

The **Runewords** section allows users to maintain a collection of the runewords that are relevant to their planned characters. A player can, for example, record a runeword they want to build in the future and then use the information when deciding which equipment and runes still need to be collected.

Available operations:

- **Show** runewords
- **Create** new runewords
- **Delete** existing runewords

### Items

Items are one of the most important parts of character progression in Diablo II. Weapons, armor, shields, helmets, gloves, boots, belts, rings, amulets, and other equipment can significantly affect a character's abilities and survivability.

The **Items** section allows users to keep track of equipment that is relevant to planned characters. This is especially useful for players who collect equipment over time and want to remember which items are already available for a future build and which items still need to be found.

Available operations:

- **Show** items
- **Create** new items
- **Delete** existing items

### Mercenary

Mercenaries are companions that can fight alongside the player's character. Depending on the selected mercenary and their equipment, they can provide additional damage, defensive benefits, or valuable auras and other effects.

The **Mercenary** section allows players to plan not only the equipment of their hero, but also the equipment of the mercenary who will accompany them.

This is important because a mercenary's equipment can be an essential part of a character build. A player may therefore want to plan a specific weapon, armor, or helmet for the mercenary and keep track of whether those items have already been collected.

Available operations:

- **Show** mercenaries
- **Create** new mercenaries
- **Edit** existing mercenaries
- **Delete** mercenaries

### Hero

The **Hero** section is the central part of Hero Planner. Heroes represent the characters that the player intends to create and develop in Diablo II.

A planned hero can be used to organize the equipment and other information associated with a future character. This allows players to think about a build before creating the actual character in the game.

The combination of heroes, mercenaries, and items is particularly useful for long-term planning. Instead of keeping notes in separate documents or trying to remember which equipment has already been collected, the player can use Hero Planner as a dedicated planning tool.

Available operations:

- **Show** heroes
- **Create** new heroes
- **Edit** existing heroes
- **Delete** heroes

## Main Purpose

The main purpose of Hero Planner is to make preparing future Diablo II characters easier and more organized.

Diablo II offers a large number of items, runes, and runewords, and a planned character can require equipment for both the hero and their mercenary. Some builds may require several specific items, while others may depend heavily on particular runewords.

Hero Planner provides a structured way to record these plans and, most importantly, distinguish between equipment that has already been collected and equipment that still needs to be obtained.

For example, a player could plan a new character several weeks before actually creating it. The required equipment can be recorded in Hero Planner, allowing the player to gradually collect the missing items. Once enough equipment has been gathered, the player can create the character in Diablo II knowing that the intended build is already prepared.

This makes Hero Planner useful as both a **character planning tool** and a **collection tracking tool**.

## Technology and Project Structure

The application is separated into several components that work together:

1. **Python / Flask** handles the application logic and routes.
2. **Jinja templates** generate the dynamic HTML pages.
3. **SQLite3** stores heroes, mercenaries, items, runes, and runewords.
4. **HTML** provides the structure of the individual pages.
5. **CSS** provides the styling and layout of the application.

This separation makes the project easier to understand and maintain while also demonstrating how the individual technologies can be combined to create a complete web application.

## Conclusion

Hero Planner was created to solve a practical problem for Diablo II players: keeping track of future character builds and the equipment required to create them.

Rather than relying on external notes, spreadsheets, or memory, players can use the application to organize their heroes, mercenaries, items, runes, and runewords in one place.

The application is especially useful for players who enjoy planning their next character in advance and collecting the necessary equipment before starting a new playthrough.

Ultimately, Hero Planner turns the preparation for a new Diablo II character into a more structured process by providing a dedicated place to plan builds, manage equipment, and track what has already been collected and what still needs to be found.









