# Framework Metrics Analysis with Python/Pharo

This project aims to collect various metrics on the NestJS and LoopBackJS frameworks to identify potential correlations and draw conclusions. It leverages both Python and Pharo for conducting the analysis.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Setting Up Python Environment](#setting-up-python-environment)
  - [Installing TS2Famix](#installing-ts2famix)
  - [Setting Up Pharo and Moose](#setting-up-pharo-and-moose)
- [Usage](#usage)
- [Contributing](#contributing)

## Prerequisites

Before you begin, make sure you have installed:

- Python 3 and pip3
- ts2famix (ensure you have at least version 10.4.0)

## Installation

### Setting Up Python Environment

After cloning the project, ensure Python3 and pip3 are installed on your machine.

### Installing TS2Famix

To install TS2Famix, you should follow the specific installation instructions provided for the tool, as it may require a different approach than a simple Node.js package.

### Setting Up Pharo and Moose

1. Install Pharo Launcher and create a Moose 10 image. The image must be named `Moose Suite 10 (stable)`. The folder of this image must be located in the `\Documents\Pharo\images\` folder of your computer. Please, be sure to not already have another image named `Moose Suite 10 (stable)`, if so, delete or rename it before creating the new image.

2. Once in Pharo, open your `Moose Suite 10 (stable)` image. Then open a Playground and execute the following commands to install NeoCSV:

   ```smalltalk
   Metacello new
       repository: 'github://svenvc/NeoCSV/repository';
       baseline: 'NeoCSV';
       load.
   ```

3. Then, install ts2famix with:

   ```smalltalk
   Metacello new
     githubUser: 'fuhrmanator' project: 'FamixTypeScript' commitish: 'master' path: 'src';
     baseline: 'FamixTypeScript';
     load.
   ```

4. Import the clone of this repository as a package into the image using Iceberg and load it. When opening the package, you should find a subpackage called Metrix. If so, save your image. After that you can close the image and the Pharo launcher.

5. Copy the `getMetrix.st` script from the `tools/PharoScript` folder into the `\Documents\Pharo\scripts` folder of your computer.

## Usage

To run the project:

- On Mac or Linux, navigate to the `src` folder and execute:

  ```bash
  ./run_on_Mac_Linux.sh
  ```

- On Windows, navigate to the `src` folder and double-click on `run_on_Windows.bat`.

After running the script, you can find the results in the `data` folder, and then in the `result` subfolder.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

## Notes

The project has only be tested on Windows and MacOS. Please note that running it with Linux could not work.
