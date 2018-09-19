import hadi_0_2
import cv2

while True:
    test                          = False
    use_auto_click_search_browser = True
    use_extract_white             = True
    use_google_search             = False
    area1                         = (1347,140,1861,588)

    if test == False:
        img  = hadi_0_2.capture(area1)

    if use_extract_white == True:
        img  = hadi_0_2.extract_white(img,resize=True)

    text = hadi_0_2.convert_to_text(img)

    # === Text edit && Auto search stuff === #
    try:
        question, answers          = hadi_0_2.seperate_q_a(text)
        answers_are_filled         = hadi_0_2.check_answers_bool(answers)
        question_not_deleted_words = hadi_0_2.character_edit(question)
        question, answers          = hadi_0_2.edit_text(question_not_deleted_words, answers)

        # === Fix answers list && Auto search stuff === #
        if answers_are_filled == True:
            answers = hadi_0_2.fix_junk_character(answers)
            hadi_0_2.decrease_list(answers,3)
            if use_auto_click_search_browser == True:
                hadi_0_2.auto_click_search_stuff(question,answers,answers_bool=True)

            # === Google Search === #
            if use_google_search == True:
                try:
                    print('\n',answers)
                    srch = hadi_0_2.g_search.Srch(question,answers[0],answers[1],answers[2],page=1)
                    srch.ask()
                except:
                    print("\nThere was a problem when googling the question and answers.")

                    a = input("\n\n'q' or Take again:")
                    if a == 'q': break
                    continue

        else:
            if use_auto_click_search_browser == True:
                hadi_0_2.auto_click_search_stuff(question,answers,answers_bool=False)

            a = input("\n\n'q' or Take again:")
            if a == 'q': break
            continue

    except:
        print('\nThere is no question here.')

        a = input("\n\n'q' or Take again:")
        if a == 'q': break
        continue
