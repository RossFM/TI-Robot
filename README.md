## TI-Robot
A program which "navigates an imaginary robotic hoover through an equally imaginary room". Submitted in fulfilment of the requirements of a technical excercise.

<b>Built with</b>
- [Python](https://www.python.org/)

## Installation & Usage
This application requires Python to run, and as such can run on a wide variety of systems. No dependancies or additional modules are required to run this application.

Python can be obtained from https://www.python.org/downloads/ Simply follow the installation guide relevant for your operating system.

This repo should then be cloned to a folder of your choosing. Within the folder will be 'input.txt', which can be editied depending on the data you wish to enter. Coordinates are entered with a single space seperating each x & y value, and a new line for each new coordinate. An example 'input.txt' is provided within the repo, with explanations for each line shown below:

`5 5` - This first line specifies the dimensions of the room to be cleaned  
`1 2` - Second line gives the starting position of the hoover  
`1 0` - Subsequent coordinates are the locations of patches of dirt to be cleaned  
`2 2`  
`2 3`  
`NNESEESWNWW` - Cardinal directions on the final line give moving instructions to the hoover  


The application is run using:  
`python Roomby.py`  
Ensure 'input.txt' is in the same directory before running the application.


<b>Output</b>  
Output from the application is provided via the terminal and will be in the following format:  
`1 3` - First line shows the final position of the hoover after completing the moving instrctions  
`1` - Second line shows the number of dirt patches which were cleaned along the way
