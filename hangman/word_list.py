"""Random word generator"""

import random

word_list = [
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple", "blueberry", "mango",
    "peach", "pear", "plum", "cherry", "lemon", "lime", "apricot", "raspberry", "blackberry", "cranberry",
    "pomegranate", "fig", "date", "coconut", "avocado", "guava", "papaya", "dragonfruit", "lychee", "passionfruit",
    "melon", "nectarine", "tangerine", "kiwifruit", "grapefruit", "cantaloupe", "mulberry", "persimmon", "durian",
    "jackfruit", "quince", "starfruit", "honeydew", "boysenberry", "gooseberry", "rhubarb", "plantain", "kumquat",
    "elderberry", "clementine", "soursop", "tamarind", "soursop", "acai", "cashew", "chestnut", "pecan", "macadamia",
    "walnut", "almond", "hazelnut", "pistachio", "peanut", "sunflower", "sesame", "flaxseed", "chia", "pumpkin",
    "squash", "zucchini", "cucumber", "eggplant", "potato", "sweet potato", "yam", "carrot", "beetroot", "radish",
    "turnip", "rutabaga", "parnsip", "broccoli", "cauliflower", "cabbage", "kale", "lettuce", "spinach", "arugula",
    "chard", "collard greens", "bok choy", "celery", "asparagus", "green beans", "peas", "snap peas", "snow peas",
    "edamame", "fava beans", "lima beans", "kidney beans", "black beans", "garbanzo beans", "lentils", "mung beans",
    "split peas", "black-eyed peas", "chickpeas", "adzuki beans", "pinto beans", "navy beans", "cranberry beans",
    "green lentils", "red lentils", "brown lentils", "french lentils", "beluga lentils", "jasmine rice", "basmati rice",
    "arborio rice", "brown rice", "white rice", "wild rice", "black rice", "red rice", "quinoa", "bulgur", "barley",
    "farro", "couscous", "millet", "buckwheat", "amaranth", "oatmeal", "steel-cut oats", "rolled oats", "instant oats",
    "quinoa flakes", "whole wheat pasta", "spaghetti", "penne", "fettuccine", "linguine", "macaroni", "farfalle",
    "rigatoni", "gnocchi", "ramen", "udon", "soba", "vermicelli", "angel hair pasta", "cappellini", "lasagna",
    "ravioli", "tortellini", "cannelloni", "manicotti", "pappardelle", "tagliatelle", "spaghettini", "biscuit",
    "croissant", "baguette", "sourdough", "rye bread", "whole wheat bread", "multigrain bread", "ciabatta", "naan",
    "pita bread", "tortilla", "pancake", "waffle", "crepe", "french toast", "muffin", "scone", "biscotti", "donut",
    "cupcake", "cake", "pie", "cheesecake", "brownie", "cookie", "macaron", "mousse", "pudding", "parfait", "trifle",
    "tiramisu", "cannoli", "eclair", "custard", "sorbet", "gelato", "sherbet", "frozen yogurt", "ice cream", "sundae",
    "milkshake", "smoothie", "juice", "lemonade", "iced tea", "iced coffee", "hot chocolate", "coffee", "espresso",
    "cappuccino", "latte", "macchiato", "americano", "mocha", "chai", "matcha", "tea"
]


def random_word():
    """ Retruns a random word"""
    return random.choice(word_list)