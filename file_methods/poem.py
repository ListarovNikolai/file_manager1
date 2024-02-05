poem = """Буря мглою небо кроет,
Вихри снежные крутя;
То, как зверь, она завоет, 
То заплачет, как дитя, 
То по кровле обветшалой 
Вдруг соломой зашумит, 
То, как путник запоздалый, 
К нам в окошко застучит."""


def write_poem():
    with open("poem.txt","w", encoding="utf-8") as file:
        file.write(poem)

def change_poem():
    with open("poem.txt","w")