import pandas as pd

data = pd.read_csv("dwarf_stars.csv")

# head() will show the first 5 rows by default
print(data.head())

data = data.dropna()

data["Radius"] = 0.102763 *  data["Radius"]

# removing unnecessARY signs and changing the data type into float 
data['Mass']=data['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

data["Mass"] = 0.000954588 *  data["Mass"]


data.to_csv("converted_data.csv")

# apply(function(){})
# apply( ()=> {} )




