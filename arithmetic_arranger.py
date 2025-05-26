def arithmetic_arranger(problems, display_answers=False):
    # Vérifie si le nombre de problèmes dépasse 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialisation des lignes pour l'affichage formaté
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for i, problem in enumerate(problems):
        # Découpe chaque problème en 3 parties : opérande1, opérateur, opérande2
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must consist of two operands and one operator."

        operand1, operator, operand2 = parts

        # Vérifie que l'opérateur est + ou -
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Vérifie que les deux opérandes sont composés uniquement de chiffres
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Vérifie que les opérandes ne dépassent pas 4 chiffres
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Trouve la largeur nécessaire pour aligner les nombres (le plus long + 2 pour l'opérateur et l'espace)
        width = max(len(operand1), len(operand2)) + 2

        # Crée chaque ligne formatée avec le bon alignement
        top = operand1.rjust(width)              # Aligne à droite operand1
        bottom = operator + operand2.rjust(width - 1)  # Aligne operand2 avec opérateur devant
        line = "-" * width                       # Ligne de tirets
        result = ""                              # Initialisation de la ligne de réponse

        # Calcule le résultat si l'option display_answers est activée
        if display_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            result = answer.rjust(width)         # Aligne la réponse à droite

        # Ajoute chaque bloc à la ligne correspondante, avec 4 espaces si ce n'est pas le premier problème
        if i > 0:
            first_line += "    "
            second_line += "    "
            dash_line += "    "
            if display_answers:
                answer_line += "    "

        first_line += top
        second_line += bottom
        dash_line += line
        if display_answers:
            answer_line += result

    # Combine les lignes finales
    if display_answers:
        return first_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line
    else:
        return first_line + "\n" + second_line + "\n" + dash_line
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],True))