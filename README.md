<!-- 
R1	Answers to all the documentation requirements below.
R2	Your README.md should have a separate heading for each documentation requirement and answers organised under the appropriate headings.
R3	Provide full attribution to referenced sources (where applicable).
R4	Provide a link to your source control repository
R5	
Identify any code style guide or styling conventions that the application will adhere to.

Reference the chosen style guide appropriately.

R6	Develop a list of features that will be included in the application. It must include:
- at least THREE features
- describe each feature

Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:
- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

Consult with your educator to check your features are sufficient .
R7	
Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 

> Your checklists for each feature should have at least 5 items.

R8	
Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application -->
# Battleship Lite

Battleship Lite is a solo game, played on a 10 * 10 map (grid), each grid square is identified with a letter and a number. The application automatically and randomly arranges the ships either vertically or horizontally on the map. Five ships are placed on the game board, their type determines how many grid squares they take up:

* Carrier (5)
* Battleship (4)
* Cruiser (3)
* Submarine (3)
* Destroyer (2)

It is important to note that the ships can not overlap, can not hang off the map, and are hidden from the Player.
After the map is built and the ships are arranged on the map, the Player can start the discovery of the ships by shooting at a target. The application provides feedback (graphically on the map and via textual information below the map) about the result of the shot (i.e.: which ship was hit, how much life the ship still has or if the given ship was sunk or missed, or already shot). The game continues until all of the ships were discovered or the Player type 'x'.

# Source control repository

[Battleship Lite Github Repository](https://github.com/KrisztaT/Battleship)  
[Presentation video](https://youtu.be/G9mrq57ohAU)  
[Trello Board](https://trello.com/b/aTdTEYkF/battleship-lite)

# Style Convention

**PEP 8** [^1] was utilised as a code style during the development of the terminal application. I enabled linting in VSC and installed the pycodestyle (pep8) extension to aid me.
Standard python code convention was also followed to achieve a code that has no syntactical error and runs smoothly.

[^1]: https://peps.python.org/pep-0008/

# Features

## 1. Greeting player

When the player starts the game, an ASCII art is printed, then the player name is asked and checked for validity (the name can contain lower and upper cases, numbers, spaces, underscores, and hyphens and it needs to be between 2 and 25 characters long). After a valid user name is given the player is greeted by the application. And the program prints out the map.

## 2. Game Map creation and printing

The map is created for the player to start the game, which first is an empty map, only filled with zeros. There are two printing services included in the game, one for the time of the development (print_game_map()) and one for the player (print_user_game_map()). The dev print method prints the map showing where the ships can be found, so during the development of the game ships’ placement and shot results can be tracked visually. Once the development stage is finished the print method is not used anymore. Only the second map printing method will be called, which hides the ships’ place from the player, however, it shows all the shot results and updates the screen after every shot.

## 3. Ship placement

The application automatically and randomly places the ships on the map, this process can not be observed by the player because it is hidden. There are two main rules of the ship placement that the application must follow:

* ships can not overlap
* ships can not hang off the map

To place the ships on the map first coordinates and orientation are randomly generated. To follow the rules, these coordinates are examined based on the orientation to see if there is another ship placed on any of the gird from the random location to random location plus ship length and if the ship would hang off the map if placement starts from the given coordinates. If another ship is placed or the ship would hang off using the generated coordinate, a new coordinate generation will take place and the examination starts from scratch. In case no other ship is on the ship length and wouldn't go out of the boundaries of the map, the ship is placed on the map.

Now let's see how these three features work together:

* the first textual section shows a successful greeting after entering the name.
* the first table shows the map printed out for development. 0 means there is nothing on the map, numbers from 1 to 5 represent the different types of ships. Using this method, we can make sure graphically that the ship placement was successful. (There are automated tests written to test this feature as well.)
* the second table is for the player, that is what is printed out at the start of the game

![Map for dev and players printed](./docs/greet_map_printing_ship_placement.png)

## 4. Handling shot coordinates

To hit the ship, the first step is for the player to enter shot coordinates. In the background, shot coordinates are checked and in case invalid coordinates are provided, a new coordinate pair is asked from the player. The process goes on until a valid coordinate is entered. Coordinates in the game need to be entered until any of the ships is alive on the map or the player wants to exit.

## 5. Shoot and feedback

After the player entered the valid coordinates, the shoot and feedback method is called from the handling shot coordinates method. The shoot and feedback method role is to examine the given coordinate on the map:

* if there is a ~ or X on the coordinate on the map, it means there was a shot there before, so the app gives back the message _Already shot there!_
* if there was no ship on the map (0) at the shot coordinate, then the app puts a _~_ in the map to that coordinate and gives the message _Missed_.
* if there is a ship on the map (1,2,3,4,5) at the shot coordinate, then the app puts an _X_ in the map to that coordinate and gives the message about _which ship was hit, how much life the ship still have or if the given ship was sunk_.

Let's see how these two features work together with the previous ones.

1. I made couple of shot to **g,6** and **i,7** coordinates, those two were both **misses**.
2. Then I shot to **a,4** and I found a destroyer ship there, so **X** is presented on the map to give feedback visually about my shot. The information below the map provides feedback textually: **Hit a destroyer that has 1 life left**.
3. So next I shot to **a,5**, where the destroyer’s second half was, the map shows that to me with an **X** and the text below informs me, that **Good job, you have sunk the destroyer**.
4. While I was shooting around I found a battleship as well, then I made my last shot to **d,10** and it was a **miss**.

![Shoot ships](./docs/ship_shooting.png)

## 6. End game

The end game is implemented in different methods (might not qualify as a separate feature), however it is a user story from the perspective of the player, hence I included it here. The purpose of the end game feature is to manage when the player wants to exit from the game before the game ends or the game must end when all ships were sunk. Depending on the exit condition (simple exit or end of the game), separate messages are printed out to the player.

|Exit game  | End of the game, ships were shot out  |
|------------------ | --------------------- |
| ![Exit message](./docs/game_exit.png) | ![win message](./docs/end_game.png) |

# Implementation plan

[Trello Board](https://trello.com/b/aTdTEYkF/battleship-lite)

Trello Board initial setup of the cards, as the development progresses the cards will be updated. The feature cards' order in the todo column define their priority order as well. It is also important, that the features build upon each other, for example there is no ship placement possible without a game map and so on.

![Trello Board 081222](./docs/221208Trello.png)

The first day of the development environment and Trello board setup was done, and the readme file, slide deck writing, and style sheet use all in-progress tasks for the project lifecycle. I started to develop the game map, hence it is in the progress column.

![Trello Board](./docs/221209TrelloBoard.png)

The game map card defines in the description the user story and additional information.

```txt
Who: As a Player
Functionality: I want to start the game and see the game map displayed
Benefit: so I can play.

To start the game first the game map needs to be built up and printed for the user and input from the player needs to be asked. Also, ships need to be placed on the map, which another card will address.
```

The checklist contains all the steps necessary to ask for user name, print a greetings out and build a map which is printed out.

![Start Game Trello card details](./docs/221209TrelloStartCard.png)

Trello Board on 11/12/2022, showing that the Start Game card was finished and the Place ships card was ongoing.

![Trello Board 101222](./docs/221211TrelloBoard.png)

The place ships card defines in the description the user story and additional information.

```txt
Who: As a Player
Functionality: I want ships to be placed on the map automatically
Benefit: so I can shoot them.

Ships need to be placed on the map before shots can be made. There are 5 types of ships in the game:

* Carrier(5),

* Battleship(4),

* Cruiser(3)

* Submarine(3)

* Destroyer(2)

To place the ships on the map random coordinates and orientation need to be generated and overlaps need to be examined. Ships can not overlap each other. For the player, these ship placements stay hidden.

```

The checklist contains all the steps necessary to create ships classes, and add ships objects to the map following the above discussed rules.

![Place ships Card 111222](./docs/221211PlaceShipCard.png)

Trello Board on 12/12/2022, showing that the Place ships card was done.

![Trello Board 121222](./docs/221212TrelloBoard.png)

I added an optional card to my trello board, it contains optional ideas that are not mandatory for the application to work, but they would be nice to haves.

![Optional Card](./docs/221212OptinalsCard.png)

Trello Board on 13/12/2022, showing that the Shoot card was placed on the ongoing column card was done.

![Trello Board 131222](./docs/221213TrelloBoard.png)

The shoot card defines in the description the user story and additional information.

```txt
Who: As a Player
Functionality: I want to make a shot
Benefit: so I can hit the ships.

An input is asked from the Player (i.e.: A,5 (column, row), this input needs to be translated into indexes of the 2D list used for creating the game map. 
```

The checklist contains all the steps necessary to ask for coordinates from the player, if coordinates are not valid handle errors and to translate valid coordinates to the language that the 2D list (game map) understands.

![Shoot Card 131222](./docs/221213ShootCard.png)

The end game card defines in the description the user story and additional information.

```txt
who: As a Player
Functionality: I want to end the game any time or want the game to end when I sank all of the ships.
Benefit: so I can quit.

Naturally, there are two ways to end the game, one is when the Player quit during the game, and the other is when the Player has hit all the ships. 
```

The checklist contains all the steps necessary to check the user input if that an x, write message and exit the game, in case there is no ships alive display the congratulation message and exit the game.

![End game Card 1412222](./docs/221214EndGameCard.png)

Most of the nice to have ideas were implemented in the game, such as ASCII art, some colors, meaningful messages at shots and statistics at the end of the game.

![Optional Card](./docs/221214OptionalCard.png)

Trello Board on 14/12/2022, showing that the features and optionals(most of them) were done. Bash script writing and documentation are ongoing tasks.

![Trello Board 141222](./docs/221214%20TrelloBoard.png)

Trello Board at the end of the day 14/12/2022, all other task is finished, only slide deck, presentation and zipping file left and to check if the mandatory requirements are fulfilled.

![Trello Board 141222 EOD](./docs/221214EOFDTrelloBoard.png)

Trello Board on 15/12/2022, showing that slide deck is in the ongoing column, next will be the youtube presentation.

![Trello Board 151222](./docs/221215TrelloBoard.png)

The day before the due date, I still need to record the presentation and then upload the file to canvas.

![Trello Board 171222](./docs/221217TrelloBoard.png)

And the project is officially done on 18/12/2022.

![Trello Board 171222](./docs/221218TrelloBoard.png)

# Help documentation

## Hardware and software requirements/ Prerequisites to install python from script

* A computer running Debian, debian type distributions (such as ubuntu), Windows using WSL2 terminal or MacOs.
* Minimum of 2GB RAM and 5GB of disk space
* Sudo access on the system/WSL2 to install Python on Linux.

To run the program the minimum hardware and software requirements are the same as for running python on your computer.

## How to run the python code the first time from a zip file

* Open your terminal
* Unzip files to a subdirectory (type in your terminal _unzip KrisztinaTesenyi_T1A3.zip -d battleship_)
* Go to the battleship/src directory (type in your terminal _cd battleship/KrisztinaTesenyi_T1A3/src_)

Linux/WSL2 | MacOS|
--- | --- |
To make the script executable run the following command in your terminal (_chmod +x setup.sh_) | To make the script executable run the following command in your terminal (_chmod +x setup_mac.sh_) |
Type _./setup.sh_ command in your terminal | Type _./setup_mac.sh_ command in your terminal |
The file checks if you have python3, pip3 and virtualenv installed on your computer. These are needed to run the code. In case you do not have any of that installed, the script will automatically install those for you. It is important to type Y and press enter when the terminal asks you to do the install. | The file checks if you have python3, pip3 and virtualenv installed on your computer. These are needed to run the code. In case you do not have python3 installed, first homebrew will be installed automatically and then the others.|
In the next step, a virtual environment is created in the folder, where you ran the ./setup.sh command. | In the next step, a virtual environment is created in the folder, where you ran the ./setup_mac.sh command. |

* Following the virtual environment creation, additional python packages that needed to run the code will be installed to your virtual environment.
  * Packages also can be found in the requirements.txt file
    * pyfiglet==0.8.post1
    * pytest==7.2.0 (only to run automated tests)
    * regex==2022.10.31
    * tabulate==0.9.0
    * termcolor==2.1.1
* Then at last the Battleship game will run and asks your name to start. Enjoy!

## How to run the python code the first time cloning it from GitHub

* Open your terminal
* Create a directory using _mkdir battleship_.
* Type _cd battleship_ to go to the created directory where you will clone the battleship game from GitHub.
* Type _git clone https://github.com/KrisztaT/Battleship.git_, then press enter and wait until cloning is finished.
* Then enter the src directory (_cd src_)

 Linux/WSL2 | MacOS|
--- | --- |
To make the script executable run the following command in your terminal (_chmod +x setup.sh_) | To make the script executable run the following command in your terminal (_chmod +x setup_mac.sh_) |
Type _./setup.sh_ command in your terminal | Type _./setup_mac.sh_ command in your terminal |
The file checks if you have python3, pip3 and virtualenv installed on your computer. These are needed to run the code. In case you do not have any of that installed, the script will automatically install those for you. It is important to type Y and press enter when the terminal asks you to do the install. | The file checks if you have python3, pip3 and virtualenv installed on your computer. These are needed to run the code. In case you do not have python3 installed, first homebrew will be installed automatically and then the others.|
In the next step, a virtual environment is created in the folder, where you ran the ./setup.sh command. | In the next step, a virtual environment is created in the folder, where you ran the ./setup_mac.sh command. |

* Following the virtual environment creation, additional python packages that needed to run the code will be installed to your virtual environment.
  * Packages also can be found in the requirements.txt file
    * pyfiglet==0.8.post1
    * pytest==7.2.0 (only to run automated tests)
    * regex==2022.10.31
    * tabulate==0.9.0
    * termcolor==2.1.1
* Then at last the Battleship game will run and asks your name to start. Enjoy!

Note: If any error happens during the execution of the script, the script will send you an error message and exits to help tou locate the problem. Once the problem solved, run the script again, so it can continue the setup.

## After the first run

* After the _setup.sh_ or _setup_mac.sh_ was run, you can use the _run.sh_ script to execute the battleship game in any of the folder on your computer.
* To do that type _chmod +x run.sh_ in your terminal
* Then type _./run.sh_ command in your terminal
* Now, that python3, pip3 and virtualenv are installed on your computer, the script install the packages used for running the code if you put it in a new directory with the game code, otherwise it just starts the game.

**Note**: This application was created with Python 3.11.0, however I made changes to the code so it should run on lower versions as well. Although, if you have issues, please run it on 3.11.

## How to play the Battleship Lite game

![How to 1](./docs/how_to_use_1.png)
![How to 2](./docs/how_to_use_2.png)
![How to 3](./docs/how_to_use_3.png)
![How to 4](./docs/how_to_use_4.png)
![How to 5](./docs/how_to_use_5.png)
