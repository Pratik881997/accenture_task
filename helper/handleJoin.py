import pandas as pd
from flask import jsonify


class HandleJoin:
    # Constructor to initialized values on the time of object creation
    def __init__(self, left_dataframe_data, right_dataframe_data, join_type, join_key):
        self.left_dataframe = pd.DataFrame(left_dataframe_data['data'])
        self.right_dataframe = pd.DataFrame(right_dataframe_data['data'])
        self.join_type = join_type
        self.join_keys = join_key
        self.possible_joins = {'leftJoin': 'left',
                               'rightJoin': 'right',
                               'innerJoin': 'inner',
                               'fullOuterJoin': 'outer',
                               'crossJoin': 'cross'
                               }

    # Protected Private method to validate join type
    def _validate_join_type(self):
        if self.join_type in self.possible_joins.keys():
            return True
        else:
            return False

    # Protected Private method to get Keys from dictionary passed in request body
    def _get_lkeys_rkeys(self):
        l_keys = []
        r_keys = []
        for keys_data in self.join_keys:
            l_keys.append(keys_data['leftKey'])
            r_keys.append(keys_data['rightKey'])
        return l_keys, r_keys

    # pubic method to Validate data and return joined dataframe according to passed values
    def dataframe_join(self):
        try:
            if self._validate_join_type():
                if len(self.join_keys) >= 1:
                    left_keys, right_keys = self._get_lkeys_rkeys()

                    validate_left_keys = set(left_keys).issubset(set(self.left_dataframe.columns))
                    validate_right_keys = set(right_keys).issubset(set(self.right_dataframe.columns))

                    if validate_left_keys and validate_right_keys:
                        df_joined = self.left_dataframe.merge(self.right_dataframe,
                                                              left_on=left_keys,
                                                              right_on=right_keys,
                                                              how=self.possible_joins[self.join_type])

                        df_joined_dict = df_joined.to_dict(orient='records')
                        return jsonify(output={"data": df_joined_dict}), 200
                    else:
                        return jsonify(InvalidKey="Please pass a Key that available in dataframe"), 401
                else:
                    return jsonify(JoinKeyRequired="please pass atleast 1 join key"), 401
            else:
                return jsonify(joinTypeError="Invalid Join Type, please choose valid Join type. valid join types are " + str(list(self.possible_joins.keys()))), 401

        # handling runtime error that did not handle in above code
        except Exception as e:
            return jsonify(Error="contact admin with this error: " + str(e)), 401
