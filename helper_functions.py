def column_mapping(survey_data) -> list:
    '''
    Based on question codes, groups columns together if they belong to single question.
    Args:
        survey_data : pandas dataframe containing survey data
    Returns:
        A list of data columns. They are grouped in the sub-lists for single questions.
        A list of open-ended questions.
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
                
        # Extracting open-ended questions to a separate list
        open_ended = []

        for question in mapped_columns:
            if type(question) == list:
                for column in question:
                    if 'other' in column:
                        open_ended.append(column)
                        question.remove(column)
                        if len(question) == 1:
                            mapped_columns[mapped_columns.index(question)] = question[0]
            
            else:
                if 'other' in question:
                        open_ended.append(question)
                        mapped_columns.remove(question)
                
    return mapped_columns, open_ended
