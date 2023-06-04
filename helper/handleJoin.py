import pandas as pd

class handleJoin:
    def __int__(self, left_dataframe_data, right_dataframe_data, join_type, join_key):
        self.left_dataframe = pd.DataFrame(left_dataframe_data['data'])
        self.right_dataframe = pd.DataFrame(right_dataframe_data['data'])
        self.join_type = join_type
        self.join_key = join_key


    private
    # possible types leftJoin, innerJoin, fullOuterJoin, rightJoin
    def dataframe_join(self):
        possible_joins = {'leftJoin': 'left',
                          'rightJoin': 'right',
                          'innerJoin': 'inner',
                          'outerJoin': 'outer',
                          'crossJoin': 'cross'
                          }

        if join_type in possible_joins.keys():
            df_joined = left_dataframe_df.merge(right_dataframe_df, on=["column1", "column2"],
                                                how=possible_joins[join_type])

            return jsonify(joinTypeError="Invalid Join Type, please choose valid Join type"), 200
        else:
            return jsonify(joinTypeError="Invalid Join Type, please choose valid Join type"), 200
        # multiple joining keys are possible, in this example there  are 2 joining keys,
        # number of possible elements in ‘joiningKeys’ array is >= 1

        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200