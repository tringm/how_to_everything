## Preprocessing

### LabelEncoder

Converting a column from string to int, and save encoder

```
from sklearn import preprocessing

label_encoders = preprocessing.LabelEncoder().fit(my_column)

classes = list(label_encoders.classes_)

transformed_column = label_encoders.transform(some_column)

reverse = label_encoders.inverse_transform(transformed_column)
```