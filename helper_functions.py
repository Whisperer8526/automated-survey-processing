def column_mapping(survey_data) -> list:
    '''
    Based on question codes, groups columns together if they belong to single question.
    Args:
        survey_data : pandas dataframe containing survey data
    Returns:
        A list of data columns. They are grouped in the sub-lists for single questions.
    '''
    
    columns = list(survey_data.columns[1:])
    q_numbers = [col.split('_')[0] for col in survey_data.columns[1:]]
    q_index = [columns.index(col) for col in columns]

    mapped_columns = []
    temp_list = []

    for col, number, idx in zip(columns, q_numbers, q_index):
        try:   
            if idx == 0 and number != q_numbers[idx+1]:
                mapped_columns.append(col)
            elif idx == 0 and number == q_numbers[idx+1]:
                temp_list = [col]
            elif idx != 0 and number != q_numbers[idx-1] and number != q_numbers[idx+1]:
                mapped_columns.append(col)
            elif idx != 0 and number != q_numbers[idx-1] and number == q_numbers[idx+1]:
                temp_list = [col]
            elif idx != 0 and number == q_numbers[idx-1] and number == q_numbers[idx+1]:
                temp_list.append(col)
            elif idx != 0 and number == q_numbers[idx-1] and number != q_numbers[idx+1]:
                temp_list.append(col)
                mapped_columns.append(temp_list)

        except IndexError:
            if number != q_numbers[idx-1]:
                mapped_columns.append(col)
            elif number == q_numbers[idx-1]:
                temp_list.append(col)
                mapped_columns.append(temp_list)
                
    return mapped_columns
