def parse_questions(input_text):
    # Séparer les questions par les délimiteurs
    questions = input_text.strip().split('-----------------------')

    parsed_questions = []

    for question_block in questions:
        # Ignorer les blocs vides
        if not question_block.strip():
            continue

        try:
            # Extraire la question
            lines = question_block.strip().splitlines()
            question_line = lines[0].strip()
            question = question_line.split(":", 1)[1].strip()

            # Extraire les options
            options = {}
            for line in lines[1:5]:  # les 4 premières lignes après la question sont les options
                if '.' in line:
                    key, value = line.split('.', 1)
                    options[key.strip()] = value.strip()

            # Extraire la bonne réponse
            bonne_reponse_line = next((line for line in lines if line.startswith("Bonne réponse")), None)
            if bonne_reponse_line:
                bonne_reponse = bonne_reponse_line.split(":", 1)[1].strip().strip('[]').replace("'", "").replace('"', '')

            # Créer le dictionnaire pour la question
            parsed_question = {
                'question': question,
                'options': options,
                'bonne_reponse': bonne_reponse
            }

            parsed_questions.append(parsed_question)

        except IndexError as e:
            print(f"Erreur de formatage dans le bloc : {question_block}")
            continue

    return parsed_questions