from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(vb)

    programming_languages = [ruby, python, vb]

    print("The dynamically type languages are:")

    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
