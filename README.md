# Pathfinding Algorithms Visualizer

> App that visualizes known algorithms for finding the shortest path

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

This project was created for learning purposes. The goal of this application is to illustrate how two the most famous pathfinding algorithms ([_A\* Search Algorithm_](https://en.wikipedia.org/wiki/A*_search_algorithm) and [_Dijkstra's Algorithm_](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)) work.

![Fig.1 - Map](assets/screenshots/Screen_Shot_Fig1.png) ![Fig.2 - Founded path](assets/screenshots/Screen_Shot_Fig2.png)

## Technologies

This project was built with Python v3.10.2 and uses following technologies:

- [Pygame](https://www.pygame.org) (v2.1.2) - GUI for application
- [Pyinstaller](https://pyinstaller.org/en/stable/) (v5.8.0) - creates a folder with executable that users can immediately run without any extra installation

## How To Use

### Download

You can download the package with finished executable version of this application from [here](https://1drv.ms/f/s!AlGBPTpcrcFXiBwcDFlZ0KNSeGgk?e=wYobQG)
(select version for your operating system and save this folder to your compupter).

### Lauching the application

Enter the downloaded folder and run (double click) the file:

- macOS - `Pathfinder.app`
- Windows - `Pathfinder.exe`

## Development setup

Follow the steps below to get started with this project's development environment.

> _Note_: this instruction assumes you have python installed on your computer

1. Clone this repository and navigate into it.

```sh
$ git clone https://github.com/mattkepa/pathfinding-visualizer.git
$ cd pathfinding-visualizer
```

2. Create python virtual environment.

```sh
$ python -m venv .venv
```

3. Activate virtual environment.

- MacOS / Linux

```sh
$ source .venv/bin/activate
```

- Windows

```sh
$ .\.venv\Scripts\activate
```

4. Install project's dependecies.

```sh
$ pip install -r requirements.txt
```

5. Run app.

```sh
$ python main.py
```

## Inspiration

This app is based on [_A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial_](https://www.youtube.com/watch?v=JtiK0DOeI4A) by [@Tech With Tim](https://www.youtube.com/@TechWithTim).

## License

All code is released under the [MIT](./LICENSE) License.
