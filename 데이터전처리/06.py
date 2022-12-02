import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

multiclass_feature = [("Texas", "Florida"),
                        ("California", "Alabama"),
                        ("Texas", "Florida"),
                        ("Deleware", "Florida"),
                        ("Texas", "Florida")]
print(multiclass_feature)

one_hot_multiclass = MultiLabelBinarizer()
one_hot_multiclass.fit_transform(multiclass_feature)

one_hot_multiclass_classes = one_hot_multiclass.classes_

one_hot_data = one_hot_multiclass.inverse_transform(
    one_hot_multiclass.transform(multiclass_feature)
)
print("one_hot_multiclass >>", one_hot_multiclass_classes)
print("one_hot_data >>", one_hot_data)