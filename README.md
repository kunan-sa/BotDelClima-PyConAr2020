# BotDelClima-PyConAr2020

## __Rasa: installation and execution__

## __Setting up the Virtual Environment__
Why set up a virtual environment? Virtual environments let you scope Python packages to a project directory, instead of installing the package on the system (global) level. This means you can use different versions of a package for different projects and helps to prevent conflicts.

We’re using **venv** in this demo to create the virtual environment, because it’s built into the Python standard library. This process is recommended for Mac and Linux users.

> **Note for Windows Users**: If you’re using Windows, we recommend using Anaconda to set up your virtual environment instead of **venv**. You can find detailed instructions [here](https://www.anaconda.com/products/individual/get-started) and in this [video tutorial](https://www.youtube.com/watch?v=4ewIABo0OkU) to help. The important parts to note are installing ujson, tensorflow, and the Visual Studio C++ build tools. Also, it is important to activate the option “Add Anaconda to my PATH environment variable" during the installation of Anaconda. 

> To create an environment in conda type ```conda create --name pydata_env python==3.7.6```

Be sure to clone this project using ```git clone https://github.com/kunan-sa/BotDelClima-PyConAr2020.git``` and install the dependencies (instructions below).

#### __Steps (Mac/Linux):__

* Inside the root directory of this project
* Create the virtual environment
    * ```python3 -m venv ./venv```
* Activate the virtual environment
    * ```source ./venv/bin/activate```

> NB: In order to leave the virtual environment simply use the command ```deactivate```; delete/ remove the environment with ```rm -rf venv```.

#### __Install dependencies__

To install [Rasa Open Source](https://rasa.com/docs/rasa/)

* Make sure you are in the root directory of this project
* Upgrade pip
    * ```pip install --upgrade pip```
* Install dependencies
    * ```pip install rasa```

> **Installing Rasa for Windows Users**: This [video](https://www.youtube.com/watch?v=4ewIABo0OkU) provides a guide to installing Rasa on a Windows operating system.

#### To use openweathermap API
You need to register to obtain the api key that you will use. https://openweathermap.org/appid
then, put this key in the constant API_KEY on api_key.py file.

#### __Train and Run the Assistant to use it on shell__
Before we can start talking to the assistant, we need to train the model and start the servers.
* Train the model

    ```rasa train```

* Once the model has finished training, run the action server in one terminal

    ```rasa run actions```

* In another terminal start the Rasa Open Source server. This will also start a session to chat with the assistant on the command line.

    ```rasa shell```

> Talk to the bot!
> To stop the Rasa Open Source server and the chat session, type /stop