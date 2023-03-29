## Creating an app to randomly generate a Caravan full of loot

## Model Walkthru

Trader model: This model would represent each trader in the caravan. It could have fields such as name, job (e.g. blacksmith, alchemist, etc.), and a foreign key to the caravan model. This model could also have a method to generate a list of items that the trader sells based on their job and the level of the caravan.

Caravan model: This model would represent the caravan itself. It could have fields such as name, location, biome, level, and a many-to-many field to the Trader model. The biome field could be a choice field with options such as "forest," "mountain," "desert," etc. The level field could be an integer field that dictates the rarity of some items you can find within the caravan. You could also add a method to this model that checks the number of traders with the same job and prevents the caravan from having too many traders of the same type of job.

Item model: This model would represent each item that can be sold by the traders. It could have fields such as name, description, price, and possibly a foreign key to the Trader model if you want to track which trader is selling the item. You could also add a field for rarity, which could be an integer that corresponds to the level of the caravan.

Loot model: This model could represent the loot that is randomly generated for the traders to sell. It could have fields such as name, description, and possibly a many-to-many field to the Item model if you want to specify which items are included in the loot. You could also add a field for rarity, which could be an integer that corresponds to the level of the caravan.

Job model: This model could represent the different jobs that traders can have (e.g. blacksmith, alchemist, etc.). It could have fields such as name and description, and could be used to populate the job field in the Trader model.
