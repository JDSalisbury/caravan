## Creating an app to randomly generate a Caravan full of loot

Random Loot Generator
This Django application generates random loot for traders in a caravan. The loot is specific to each trader's job and the biome the caravan is traveling through.

Installation
To use this application, you'll need to have Python 3 and Django 3 installed. Once you have those installed, follow these steps:

Clone this repository to your local machine: git clone https://github.com/yourusername/random-loot-generator.git
Navigate to the project directory: cd random-loot-generator
Install the required packages: pip install -r requirements.txt
Run the Django development server: python manage.py runserver
Navigate to http://localhost:8000 in your web browser to use the application.
Usage
Once you have the application running, you can use it to generate random loot for a caravan of traders. The loot is specific to each trader's job and the biome the caravan is traveling through.

To generate loot, follow these steps:

Navigate to http://localhost:8000 in your web browser.
Click the "Generate Loot" button to generate a new caravan with random loot.
Scroll down to see the details of the caravan and the items being sold by each trader.
You can generate as many caravans as you like by clicking the "Generate Loot" button multiple times.

Customization
This application is highly customizable. You can modify the following aspects of the generated loot:

The number and types of traders in the caravan
The items sold by each trader, based on their job and the biome they're traveling through
The rarity of items in the caravan, based on the caravan's level
The types of items that can be generated, including weapons, armor, consumables, and more
To customize the application, you'll need to modify the Python code in the random_loot Django app. You can modify the Trader and Item models to change the types of traders and items that can be generated. You can also modify the generate_loot function in the views.py file to customize the logic for generating loot.

License
This application is released under the MIT License. See LICENSE.txt for more information.
