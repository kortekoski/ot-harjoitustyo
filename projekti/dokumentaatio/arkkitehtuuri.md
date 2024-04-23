# Arkkitehtuurikuvaus

## Rakenne

Ohessa on sovelluksen rakenne yksinkertaistettuna. Sprites sisältää kaikki muut spritet kuin pelaajan, kuten kolikot, tasot jne.

```mermaid
 classDiagram
    GameLoop -- Clock
    GameLoop -- Level
    GameLoop -- EventQueue
    GameLoop -- Renderer
    Renderer -- Level
    Level -- Player
    Level -- Sprites
```

## Toiminnallisuus

Seuraavassa kaaviossa on kuvattuna pelin käynnistyminen ensimmäiseen pelisilmukkaan asti. Ensimmäisessä silmukassa on pelin aloitusruutu.

```mermaid
  sequenceDiagram
    create participant main
    create participant EventQueue
    main->>EventQueue: EventQueue()
    create participant Renderer
    main->>Renderer: Renderer(screen, screen_center)
    create participant Clock
    main->>Clock: Clock()
    create participant GameLoop
    main->>GameLoop: GameLoop(level_maps, renderer, event_queue, clock, CELL_SIZE)
    main->>GameLoop: start()
    GameLoop->>Renderer: render_introscreen()
    GameLoop->>Clock: tick(60)
```