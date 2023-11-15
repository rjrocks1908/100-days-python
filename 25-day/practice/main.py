import pandas as pd

PRIMARY_FUR_COLOR = "Primary Fur Color"
GRAY = "Gray"
CINNAMON = "Cinnamon"
BLACK = "Black"

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data[PRIMARY_FUR_COLOR]
gray_squirrel_count = len(data[fur_colors == GRAY])
cinnamon_squirrel_count = len(data[fur_colors == CINNAMON])
black_squirrel_count = len(data[fur_colors == BLACK])

new_data = {
    PRIMARY_FUR_COLOR: [GRAY, CINNAMON, BLACK],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

pd.DataFrame(new_data).to_csv("new_data.csv")
