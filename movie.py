#import data
import pandas as pd
movie_data=pd.read_csv("jamesbond.csv").convert_dtypes()
print(movie_data.head())

#change column name
new_column_names = {"Release": "release_date",
"Movie": "movie_title",
"Bond": "bond_actor",
"Bond_Car_MFG": "car_manufacturer",
"US_Gross": "income_usa",
"World_Gross": "income_world",
"Budget": "movie_budget",
"Film_Length": "film_length",
"Avg_User_IMDB": "imdb",
"Avg_User_Rtn_Tom": "rotten_tomatoes",
"Martinis": "martinis_consumed",
"Kills_Bond": "bond_kills"}
data = movie_data.rename(columns=new_column_names)
print(data.columns)

#missing data
print(data.info())
print(data.loc[data.isna().any(axis="columns")])
print(data.isnull().sum()) #verify null values within each column

#handling financial column
print(data[["income_usa", "income_world", "movie_budget", "film_length"]].head())
data[["income_usa","income_world","movie_budget"]] = (data[["income_usa","income_world","movie_budget"]]
    .replace(r"[\$,]", "", regex=True).astype(float))
data["film_length"] = (data["film_length"].astype(str).str.replace("mins", "", regex=False).astype(int))
print(data[["income_usa","income_world","movie_budget","film_length"]].head())

#correcting invalid data type
pd.to_datetime(data["release_date"], format="%B, %Y")

#fixing inconsistency in data
data["movie_budget"] = data["movie_budget"] * 1000
print(data["movie_budget"].head())

#corrcting spelling error
data["bond_actor"].value_counts()
bond_actor=(data["bond_actor"].str.replace("Shawn", "Sean").str.replace("MOORE", "Moore"))
data["car_manufacturer"].value_counts()
car_manufacturer=(data["car_manufacturer"].str.replace("Astin", "Aston"))

#checking invalid outlier
data[["film_length","martinis_consumed"]].describe()
data["film_length"] = data["film_length"].replace(1200, 120)

#removing duplicate data
data.loc[data.duplicated(keep=False)]
data = data.drop_duplicates()

#storing leansed data
data.to_csv("movie_data_cleansed.csv", index=False)

#performing regression
data = pd.read_csv("movie_data_cleansed.csv").convert_dtypes()
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(data["imdb"], data["rotten_tomatoes"]) 
ax.set_title("Scatter Plot of Ratings")
ax.set_xlabel("Average IMDb Rating")
ax.set_ylabel("Average Rotten Tomatoes Rating")
fig.show()

from sklearn.linear_model import LinearRegression
x = data.loc[:, ["imdb"]]
y = data.loc[:, "rotten_tomatoes"]

model = LinearRegression()
model.fit(x, y)
r_squared = f"R-Squared: {model.score(x, y):.2f}"
best_fit = f"y = {model.coef_[0]:.4f}x{model.intercept_:+.4f}"
y_pred = model.predict(x)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x, y_pred, color="red")
ax.text(7.25, 5.5, r_squared, fontsize=10)
ax.text(7.25, 7, best_fit, fontsize=10)
ax.set_title("Scatter Plot of Ratings")
ax.set_xlabel("Average IMDb Rating")
ax.set_ylabel("Average Rotten Tomatoes Rating")
fig.show()

#Investigating a Statistical Distribution
fig, ax = plt.subplots()
length = data["film_length"].value_counts(bins=7).sort_index()
length.plot.bar(ax=ax,title="Film Length Distribution",xlabel="Time Range (mins)",ylabel="Count",)
fig.show()

data["film_length"].agg(["min", "max", "mean", "std"])

#finding no relationship
fig, ax = plt.subplots()
ax.scatter(data["imdb"], data["bond_kills"])
ax.set_title("Scatter Plot of Kills vs Ratings")
ax.set_xlabel("Average IMDb Rating")
ax.set_ylabel("Kills by Bond")
fig.show()