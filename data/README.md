# Dataset: 130k wine reviews

The dataset used is that of [130k wine reviews](https://www.kaggle.com/datasets/zynicide/wine-reviews) from the [WineEnthusiast Magazine](https://www.winemag.com/?s=&drink_type=wine) in 2017, obtained via Kaggle. Full credit is due to [the original author](https://www.kaggle.com/zynicide) and Kaggle for curating/hosting this dataset.

For ease of use, the original data in JSON is re-formatted to newline-delimited JSON (`.jsonl`) format and compressed as a GZIP archive. There is no need to run the `convert.py` file to use the data in the `jsonl.gz` file; the code is provided here purely for reference.

A sample wine review JSON object is shown below.

```json
{
    "points": "90",
    "title": "Castello San Donato in Perano 2009 Riserva  (Chianti Classico)",
    "description": "Made from a blend of 85% Sangiovese and 15% Merlot, this ripe wine delivers soft plum, black currants, clove and cracked pepper sensations accented with coffee and espresso notes. A backbone of firm tannins give structure. Drink now through 2019.",
    "taster_name": "Kerin O'Keefe",
    "taster_twitter_handle": "@kerinokeefe",
    "price": 30,
    "designation": "Riserva",
    "variety": "Red Blend",
    "region_1": "Chianti Classico",
    "region_2": null,
    "province": "Tuscany",
    "country": "Italy",
    "winery": "Castello San Donato in Perano",
    "id": 40825
}
```
