## type checking for recipe words

## list taken from this project: https://github.com/tylrodg/CS337-Recipes/blob/484d2f04a3dc526cfb65e5165c4633a8ba8551fe/recipeDB.json

## ADD TO THIS (obv)
measurements = ["Tbsp",
      "Tbsps",
      "bottle",
      "bottles",
      "c",
      "cs",
      "cup",
      "cups",
      "dessertspoon",
      "dessertspoons",
      "fl oz",
      "fl ozs",
      "fluid ounce",
      "fluid ounces",
      "fluid oz",
      "fluid ozs",
      "gal",
      "gallon",
      "gallons",
      "gals",
      "jar",
      "jars",
      "liter",
      "liters",
      "milliliter",
      "milliliters",
      "ml",
      "mls",
      "pint",
      "pints",
      "pt",
      "pts",
      "qt",
      "qts",
      "quart",
      "quarts",
      "tablespoon",
      "tablespoons",
      "teaspoon",
      "teaspoons",
      "tsp",
      "tsps",
      "bag",
      "bags",
      "bunch",
      "bunches",
      "can",
      "cans",
      "clove",
      "cloves",
      "cube",
      "cubes",
      "dash",
      "dashes",
      "envelope",
      "envelopes",
      "gram",
      "grams",
      "head",
      "heads",
      "inch",
      "inches",
      "kilogram",
      "kilograms",
      "lb",
      "lbs",
      "ounce",
      "ounces",
      "oz",
      "ozs",
      "package",
      "packages",
      "packet",
      "packets",
      "piece",
      "pieces",
      "pinch",
      "pinches",
      "pound",
      "pounds",
      "sheet",
      "sheets",
      "slice",
      "slices",
      "strip",
      "strips"]

tools = ["apple corer",
    "apple cutter",
    "bag",
    "baking sheet",
    "balloon whisk",
    "basket skimmer",
    "baster",
    "basting brush",
    "beanpot",
    "bell whisk",
    "bench knife",
    "bench scraper",
    "biscuit mould",
    "blender",
    "blow torch",
    "blowlamp",
    "blowtorch",
    "boil oven preventer",
    "bottle opener",
    "bowl",
    "bread knife",
    "browning bowl",
    "browning plate",
    "browning tray",
    "bulb baster",
    "burger spatula",
    "burr grinder",
    "burr mill",
    "biscuit cutter",
    "biscuit press",
    "butcher's twine",
    "butter curler",
    "cake server",
    "cake shovel",
    "can opener",
    "candy thermometer",
    "carving knife",
    "cheese cutter",
    "cheese grater",
    "cheese knife",
    "cheese knives",
    "cheese slicer",
    "cheese spreader",
    "cheesecloth",
    "chef knife",
    "chef's knife",
    "chefs knife",
    "cherry pitter",
    "chinois",
    "chinoise",
    "citrus reamer",
    "clay pot",
    "cleaver",
    "colander",
    "cookie cutter",
    "cookie mould",
    "cookie press",
    "cooking twine",
    "corkscrew",
    "crab cracker",
    "cup",
    "cutting board",
    "deep spoon",
    "dish",
    "dough scraper",
    "drum sieve",
    "edible tableware",
    "egg piercer",
    "egg poacher",
    "egg separator",
    "egg slicer",
    "egg timer",
    "fat separator",
    "fillet knife",
    "fish scaler",
    "fish slice",
    "fish spatula",
    "flat coil whisk",
    "flat whisk",
    "flour sifter",
    "food mill",
    "food storage container",
    "french whisk",
    "frying pan",
    "funnel",
    "garlic press",
    "grapefruit knife",
    "grater",
    "gravy separator",
    "gravy strainer",
    "gravy whisk",
    "griddle",
    "herb chopper",
    "honey dipper",
    "ice cream scoop",
    "kitchen mallet",
    "kitchen scale",
    "kitchen scissor",
    "kitchen scraper",
    "kitchen string",
    "kitchen tool crock",
    "kitchen twine",
    "knife",
    "ladle",
    "lame",
    "lemon reamer",
    "lemon squeezer",
    "lobster fork",
    "lobster pick",
    "mandoline",
    "mashers",
    "mated colander pot",
    "measuring cup",
    "measuring jar",
    "measuring jug",
    "measuring spoon",
    "meat grinder",
    "meat tenderizer",
    "meat tenderizer",
    "meat thermometer",
    "melon ball",
    "melon baller",
    "metal tong",
    "mezzaluna",
    "microplane",
    "milk frother",
    "milk guard",
    "milk watcher",
    "mincer",
    "mini whisk",
    "mixing bowl",
    "mixing whisk",
    "molcajete",
    "mortar",
    "nutcracker",
    "nutmeg grater",
    "olive stoner",
    "oven glove",
    "oven mitt",
    "oven",
    "pan",
    "panini spatula",
    "pasta fork",
    "pastry bag",
    "pastry blender",
    "pastry brush",
    "pastry wheel",
    "peeler",
    "pepper grinder",
    "pepper mill",
    "pestle",
    "pie bird",
    "pie cutter",
    "pie funnel",
    "pie server",
    "pie vent",
    "pizza cutter",
    "pizza shovel",
    "pizza slicer",
    "pot holder",
    "pot minder",
    "pot",
    "pot-holder",
    "potato masher",
    "potato ricer",
    "potholder",
    "poultry shears",
    "ricer",
    "roast lifter",
    "roller docker",
    "rolling pin",
    "salt shaker",
    "santoku knife",
    "saucepan",
    "scale",
    "scissor",
    "scoop",
    "scraper",
    "serrated bread knife",
    "serving platter",
    "shredder",
    "sieve",
    "sifter",
    "silicone tong",
    "skillet",
    "slotted spoon",
    "spatula",
    "spider strainer",
    "spider",
    "spoon sieve",
    "spoon skimmer",
    "steak knife",
    "stove",
    "strainer",
    "sugar thermometer",
    "tablespoon",
    "tamis",
    "teaspoon",
    "tin opener",
    "tomato knife",
    "tong",
    "trussing needle",
    "turner",
    "twine",
    "urokotori",
    "utility knife",
    "vegetable peeler",
    "weighing scales",
    "whisk",
    "wooden spoon",
    "zester"]

methods = ["bake",
      "boil",
      "broil",
      "fry",
      "pressure cook",
      "grill",
      "mix",
      "simmer",
      "blend",
      "roast",
      "steam",
      "stew",
      "saute",
      "stir-fry",
      "pan-fry",
      "searing",
      "braise",
      "bake",
      "beat",
      "boil",
      "brown",
      "brush",
      "cover",
      "cool",
      "combine",
      "cream",
      "cut",
      "dip",
      "drain",
      "chill",
      "crumble",
      "flour",
      "flip",
      "fold",
      "grease",
      "heat",
      "line",
      "mash",
      "measure",
      "mix",
      "melt",
      "pour",
      "garnish",
      "preheat",
      "pound",
      "layer",
      "stuff",
      "refrigerate",
      "rinse",
      "serve",
      "season",
      "shake",
      "simmer",
      "sift",
      "slice",
      "soak",
      "spoon",
      "spread",
      "sprinkle",
      "stir",
      "strain",
      "toast",
      "toss",
      "turn",
      "whisk"]


# taken from https://www.foodnetwork.com/recipes/articles/basic-pantry-101
pantry = ["canola oil", 
"extra-virgin olive oil", 
"toasted sesame",
"balsamic vinegar", 
"distilled white vinegar", 
"red wine vinegar", 
"rice vinegar",
"Ketchup",
"Mayonnaise",
"Dijon mustard",
"Soy sauce",
"Chili paste",
"Hot sauce",
"Worcestershire",
"Kosher salt",
"Black peppercorns",
"bay leaves", 
"cayenne pepper", 
"crushed red pepper", 
"cumin", 
"oregano", 
"paprika", 
"rosemary", 
"thyme leaves", 
"cinnamon", 
"cloves",
"allspice", 
"ginger", 
"nutmeg",
"chili powder", 
"curry powder", 
"Italian seasoning",
"Vanilla extract",
"black beans", 
"cannellini beans", 
"chickpeas beans", 
"kidney beans",
"Capers",
"Olives",
"Peanut butter",
"Preserves",
"jelly",
"Low-sodium stock",
"broth",
"Canned tomatoes",
"Tomato paste",
"Salsa",
"Canned tuna",
"regular breadcrumbs",
"panko breadcrumbs",
"Couscous"
"Dried lentils"
"regular pasta", 
"whole wheat pasta",
"Rice",
"Rolled oats",
"barley", 
"millet", 
"quinoa",
"wheatberries",
"Baking powder",
"Baking soda",
"Brown sugar",
"Cornstarch",
"All-purpose flour",
"Granulated sugar",
"Honey",
"Butter",
"sharp cheddar",
"feta", 
"Parmesan", 
"mozzarella",
"Large eggs",
"Milk",
"Plain yogurt",
"Corn tortillas",
"blackberries", 
"blueberries", 
"peaches", 
"strawberries",
"berry",
"broccoli", 
"bell pepper",
"onion",
"corn", 
"edamame", 
"peas", 
"spinach",
"Garlic",
"Potatoes",
"dried raisins", 
"dried apples", 
"dried apricots",
"almonds", 
"peanuts", 
"sunflower seeds"]

