# Alien Invasion

Juego arcade 2D desarrollado en **Python** con **Pygame**, basado en el **Proyecto 1** del libro *Python Crash Course* (Eric Matthes). Este README está pensado para ayudarte a **instalar, ejecutar, entender** y **extender** el proyecto.

---

## 📦 Requisitos

* **Python 3.10+** (recomendado 3.11 o 3.12). Funciona en Windows/macOS/Linux.
* **Pygame** 2.x
* (Opcional) **Git** para clonar el repositorio

---

## 🔧 Instalación

### 1) Clonar el repositorio

```bash
# con SSH
git clone git@github.com:<tu-usuario>/<tu-repo>.git
# o con HTTPS
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
```

### 2) Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux (bash/zsh):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependencias


```bash
pip install pygame
```

---

## ▶️ Ejecución

```bash
python alien_invation.py
```

---

## 🎮 Cómo jugar

* **Movimiento:** Flechas **← →** 
* **Disparar:** **Espacio**
* **Salir:** **Q** o cerrar la ventana
* **Objetivo:** Derriba a todos los aliens sin que lleguen al fondo ni choquen con tu nave. Subes de **nivel** al limpiar la flota; la velocidad aumenta gradualmente.

---

## 🧱 Estructura del proyecto 

```
Alien-Invasion/
├─ images/                 # recursos gráficos
├─ store_information/      # (si guardas información del juego)
├─ alien_invation.py       # punto de entrada actual
├─ settings.py             # parámetros del juego
├─ ship.py                 # clase Ship (nave del jugador)
├─ bullet.py               # clase Bullet
├─ alien.py                # clase Alien
├─ game_functions.py       # funciones del juego (loop, eventos, colisiones, etc.)
├─ game_stats.py           # puntuación, vidas, estado del juego
├─ scorebard.py            # marcador (archivo con typo: sugerido renombrar a scoreboard.py)
├─ button.py               # botón Play
├─ .gitignore
└─ README.md
```

---


## 🧠 Mecánicas principales

* **Flota de aliens:** Movimiento horizontal con **descenso + inversión** de dirección (`fleet_direction`) al tocar bordes.
* **Colisiones** (manejadas típicamente en `game_functions.py`):

  * **bala vs alien**: elimina alien, suma puntos; si no quedan → **nuevo nivel** y aumento de velocidad.
  * **alien vs nave** o **alien al fondo**: pierdes una **vida** (`ship_limit`).
* **Marcadores:** `score`, `high_score`, `level` y **vidas** renderizados por `scorebard.py` (o `scoreboard.py` si renombras).

---

## ✅ Pruebas rápidas (manuales)

* Dispara hasta limpiar una flota → ¿sube **level** y aumenta la **velocidad**?
* Deja caer un alien hasta el fondo → ¿pierdes **una vida** y se **reinicia** la flota?
* Supera tu récord → ¿se actualiza `high_score`?

---

## 🌱 Roadmap (ideas de mejora)

* Sonidos (disparos/explosiones) y música.
* Animaciones de explosión y sprites personalizados.
* **Power-ups** (disparo triple, escudo temporal, slow-motion).
* Menú de **pausa** y selector de dificultad.
* Sistema de **guardado** de high score en archivo.
* Tabla de **leaderboard** local.
* Soporte para **mando**/gamepad.


---

## 🤝 Contribuir

1. Crea una rama: `git checkout -b feat/<mi-feature>`
2. Haz commits claros: `git commit -m "feat: agrega power-ups"`
3. Abre un PR describiendo cambios y capturas.

> Si trabajas solo, las **ramas** igual te ayudan a experimentar sin romper `main`.

---

## 🙌 Créditos

* Proyecto inspirado en *Python Crash Course* de **Eric Matthes**.
* Desarrollado por **Pablo Fuentealba** 


---

## 📚 Referencias útiles

* Documentación de Pygame: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
* Libro *Python Crash Course* (Proyecto Alien Invasion)
* Guía oficial de Python `venv`: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

---
