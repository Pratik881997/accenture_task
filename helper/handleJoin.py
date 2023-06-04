import pandas as pd
from flask import jsonify


class HandleJoin:
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

    def _validate_join_type(self):
        if self.join_type in self.possible_joins.keys():
            return True
        else:
            return False

    def _get_lkeys_rkeys(self):
        l_keys = []
        r_keys = []
        for keys_data in self.join_keys:
            l_keys.append(keys_data['leftKey'])
            r_keys.append(keys_data['rightKey'])
        return l_keys, r_keys

    # possible types leftJoin, innerJoin, fullOuterJoin, rightJoin
    def dataframe_join(self):
        try:
            if self._validate_join_type():
                if len(self.join_keys) >= 1:
                    left_keys, right_keys = self._get_lkeys_rkeys()

                    df_joined = self.left_dataframe.merge(self.right_dataframe,
                                                          left_on=left_keys,
                                                          right_on= right_keys,
                                                          how=self.possible_joins[self.join_type])

                    df_joined_dict = df_joined.to_dict()
                    return jsonify(output={"data":df_joined_dict}), 200
                else:
                    return jsonify(joinTypeError="please pass atleast 1 join key"), 401
            else:
                return jsonify(joinTypeError="Invalid Join Type, please choose valid Join type"), 401

        except Exception as e:
            return jsonify(joinTypeError="contact admin with this error: " + str(e)), 401
