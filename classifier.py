from taipy.gui import Gui

img_path = "logo.png" ##adiciona Logo

index = """ 
<|text-center|
<|{"logo.png"}|image|>

<|{content}|file_selector|>
Selecione uma imagem do seu armazenamento

<|{img_path}|image|>
>
"""

app = Gui (page=index)

if __name__=="__main__":
    app.run(use_reoader=True)